# Use atomic units
Aborh = 0.529177208

class molecule:
    def __init__(self, mass_ions = [], mass_electron = 0):
        '''
        Here we initialisate common molecule structure with ions and electron mass
        We also initialise ions and electron names
        '''
        self.mass_ions = mass_ions
        self.mass_electron = mass_electron
        self.type_names = []

    def mass(self):
        '''
        Return full mass of molecules
        '''
        full_mass = self.mass_electron
        for mass_ion in self.mass_ions:
            full_mass += mass_ion
        return full_mass

    def return_mass(self):
        return {1: 1.008, 2: 0.005}

    def get_datas(self, center_coord=[]):
        '''
        Get coordinates of center of mass, and return list of dicts with property for every particles in molecules
        '''
        data = [ {'x': center_coord[0], 'y': center_coord[1], 'z': center_coord[2]} ]
        return data
'''
    def print(self, filetype, filename):
        if filetype == 'lammps':
            print_lammps(filename, self.coordinates, self.wall, self.mass_ion, self.mass_electron)
        if filetype == 'pdb':
            print_pdb(filename = filename, coordinates = self.coordinates, type_names = self.type_names)
        if filetype == 'poscar':
            print_poscar(filename, self.coordinates, self.wall)
        if filetype == 'xyz':
            print_xyz(filename, self.coordinates, self.type_names)

'''