# all computation in bohr distance
import numpy as np
from lib.basis import get_basis
import random
from lib.printing import printing
from lib.hydrogen_molecule import hydrogen_molecule
from lib.hydrogen_atom import hydrogen_atom
from lib.hydrogen_atom_minus import hydrogen_atom_minus
from lib.hydrogen_triatomic import hydrogen_triatomic

Ab = 0.529e-8 # Boltzman radius
amu = 1.66e-24 # atom unity of mass
kbol = 1.38e-16 # Boltzman constant

class lattice(printing):
    def __init__(self, data_string):
        '''
        Read initialisate data in format: 
        "wall_step 10 10 10 wall_size 3.0 3.0 3.0 style sc mol h2"
        Or 
        "n_types 2 h2 100 h+ 100 rho 1.0"
        '''
        self.str_parametrs = data_string
        self.lattice = list()
        self.molecules = []
        self.molecules_count = []
        data_string = data_string.split(" ")
      

        # get basis from data_string
        style = 'sc'
        if 'style' in data_string:
            style = data_string[ data_string.index('style') + 1]
        self.basis, self.a = get_basis(style)

        
        if ( 'wall_step' in data_string ) and ( 'wall_size' in data_string):
            # if we have wall_step and wall_size we will create a strong lattice with that parametrs
            ind = data_string.index('wall_step')
            self.wall_step = [ int(data_string[i]) for i in [ind+1, ind+2, ind+3] ]
            ind = data_string.index('wall_size')
            self.wall_size = [ float(data_string[i]) for i in [ind+1, ind+2, ind+3] ]
            # get molecules info from data_string
            self.get_molecules(data_string = data_string)

            # set normalize lattice vectors as wall_step
            self.a = [self.a[i] * self.wall_step[i] for i in range(3)]
            self.create_lattice()
            self.N = len(self.lattice)
            

            self.rho = self.N / self.wall_size[0]**3

        elif ( 'rho' in data_string) and ( 'n_types' in data_string):
            # if we have rho and number of particles for all types of molecules
            # get molecules info from data_string
            self.get_molecules(data_string = data_string)

            ind = data_string.index('rho')
            # convert rho to number of lattice points, rho in g/cm^3 -> 1/cm^3
            rho = float(data_string[ ind + 1 ])
            rho_n = rho/(self.mass_average * amu)
            atom_unit_rho = rho_n*Ab**3
            self.rho = atom_unit_rho
            N_units = self.N
            # we create a cubic lattice which more then we need, to random placing particles in the units
            wall_count = int( N_units**( 1. / 3 ) )  * 2 # 2 provide random distribution except simple cubic lattice
            self.wall_size = [ (self.N / self.rho) **( 1. / 3 )] * 3
            self.wall_step = [ (self.N / self.rho) **( 1. / 3 ) / wall_count ] * 3
            # set normalize lattice vectors as wall_step
            self.a = [self.a[i] * self.wall_step[i] for i in range(3)]
            self.create_lattice()
            rand_list = random.sample(range(len(self.lattice)), self.N) # choose random place for N atoms
            real_lattice = [ self.lattice[item] for item in rand_list]
            self.lattice = real_lattice
            
        else:
            print ("Error in lattice initialisation, choose ( rho and N) or (wall_step, wall_size)")
            raise ValueError

        # Check the temperature to create momentum distribution
        if 'T' in data_string:
            self.T_flag = True # print velocity to file or not
            T = float(data_string[ data_string.index('T') + 1])
            self.make_velocities(T)

        else:
            self.T_flag = False
            self.velocities = [ np.array([0,0,0]) for i in range(self.N) ]

        self.create_system()

    def __in_box(self, x):
        result = True
        result = result and ( x[0] <= self.wall_size[0] ) and ( x[0] > 0 )
        result = result and ( x[1] <= self.wall_size[1] ) and ( x[1] > 0 )
        result = result and ( x[2] <= self.wall_size[2] ) and ( x[2] > 0 )

        return result

    def create_lattice(self):
        x0 = np.array([self.wall_size[0]/2.0, self.wall_size[1]/2.0, self.wall_size[2]/2.0])

        n_max = int( (self.N / len(self.basis)) ** (1. / 3) )
        n = np.zeros(3)
        for n[0] in range(-n_max, n_max, 1):
            print ("\rcreate lattice {:s}: {:d} %".format(self.str_parametrs, int( (n[0] + n_max) / ( 2. * n_max) * 100)), end="" )
            for n[1] in range(-n_max, n_max, 1):
                for n[2] in range(-n_max, n_max, 1):
                    for basis_vector in self.basis:
                        x = x0 + basis_vector + self.a[0] * n[0] + self.a[1] * n[1] + self.a[2] * n[2]
                        if self.__in_box(x):
                            self.lattice.append(x)
        print ("\rcreate lattice {:s}: 100 %".format(self.str_parametrs))

    

    def coordinates(self):
        return self.lattice

    def wall(self):
        return self.wall_size
    
    def create_system(self):
        self.system = []
        rest_coordinates = self.lattice[:]
        rest_velocities = self.velocities[:]

        for index in range(self.n_types):
            N = self.molecules_count[index]
            molecule = self.molecules[index]
            coordinates = rest_coordinates[:N]
            rest_coordinates = rest_coordinates[N:]
            velocities = rest_velocities[:N]
            rest_velocities = rest_velocities[N:]
            
            spin = 1
            for i in range(N):
                new_data, spin = molecule.get(coordinate = coordinates[i], velocities = velocities[i], spin = spin)
                self.system.extend(new_data)
        
    
    def return_molecule_from_name(self, name):
        if name == 'h2': return hydrogen_molecule()
        if name == 'h': return hydrogen_atom()
        if name == 'h-': return hydrogen_atom_minus()
        if name == 'h3+': return hydrogen_triatomic()

    def make_velocities(self, T):
        # check that number of particles of all type is even, it's neccessary to achieve zero full momentum
        for n in self.molecules_count:
            if (n % 2) == 1:
                print ("Number of particles for all types must be even")
                raise ValueError
        
        most_except_energy = 1.38e-23*T/4.36e-18 # kT in Hartry energy units
        energy_range = np.linspace(0, most_except_energy*3, 1000)
        coeff = 0
        for e in energy_range:
            coeff += np.sqrt(e) * np.exp(-e/most_except_energy)
        coeff = self.N*1000/coeff # we need more than need, to get random value, next we will use two similar energy to make momentum zero
        energy_list = []
        for e in energy_range:
            energy_list += [e] * int( coeff * np.sqrt(e) *  np.exp(-e/most_except_energy))
        
        rand_list = random.sample(range(len(energy_list)), int(self.N/2)) # choose random place for N atoms, next we will use two similar energy to make momentum zero
        energy_list = [ energy_list[item] for item in rand_list]
        # next we will create momentum distribution for all particles type
        rest_energies = energy_list[:]
        self.velocities = []
        for index in range(self.n_types):
            N = self.molecules_count[index]
            N = int(N/2) # two oposite moment
            mass = self.molecules[index].mass_ion()
            energies = rest_energies[:N]
            rest_energies = rest_energies[N:]
            for e in energies:
                v = np.sqrt(2*e/mass) 
                # create random direction of momentum
                vector = np.random.rand(3)
                vector /= np.linalg.norm(vector)
                v = vector*v
                self.velocities.append(v)
                # make momentum zero
                self.velocities.append(-v)

                
    def get_molecules(self, data_string):
        if 'mol' in data_string:
            # if we have only one molecules for lattice we will use this option
            ind = data_string.index('mol') + 1
            name = data_string[ind]
            self.molecules.append(self.return_molecule_from_name(name))
            self.mass_particles = self.molecules[-1].return_mass()
            self.mass_average = self.molecules[-1].mass()
        elif 'n_types' in data_string:
            # if we want to create a system with different count of different molecules type we will use this section
            ind = data_string.index('n_types') + 1
            self.n_types = int( data_string[ind] )
            self.N = 0
            self.mass_average = 0
            self.mass_particles = dict()
            for i in range(self.n_types):
                self.molecules.append(self.return_molecule_from_name(data_string[ ind + i*2 + 1]))
                self.molecules_count.append(int(data_string[ ind + i*2 + 2]))
                self.N += self.molecules_count[-1]
                self.mass_average += self.molecules[-1].mass() * self.molecules_count[-1]
                self.mass_particles = { **self.mass_particles, **self.molecules[-1].return_mass()}
            self.mass_average /= self.N
        else:
            print ("Error reading particles type")
            raise ValueError

