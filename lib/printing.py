Ab = 0.529

class printing:
    def __init__(self):
        self.system = []
        self.wall_size = [0,0,0]
        self.mass_ions = []
        self.mass_electron = 0
        self.T_flag = False
        self.mass_particles = dict()
        self.system = []
        self.lattice = []
        self.rho = 0
        self.N = 0
        self.str_parametrs = ""

    def print(self):
        print ("rho = {:.2f} 1/bohr**3, N = {:d}".format(self.rho, self.N) )
        print ("wall size = {:.2f} bohr ( {:.2f} A )".format(self.wall_size[0], self.wall_size[0] * Ab))
        print ("")
        print ("----------------------")
        print ("| {:4s} | {:4s} | {:4s} |".format("X", "Y", "Z"))
        print ("----------------------")
        for item in self.system:
            print ("| {:2.2f} | {:2.2f} | {:2.2f} |".format(item['x'], item['y'], item['z']))
        print ("----------------------")

    def print_lattice(self):
        print ("----------------------")
        print ("| {:4s} | {:4s} | {:4s} |".format("X", "Y", "Z"))
        print ("----------------------")
        for item in self.lattice:
            print ("| {:2.2f} | {:2.2f} | {:2.2f} |".format(item[0], item[1], item[2]))
        print ("----------------------")

    def print_lammps(self, filename):
        dfile = open(filename, "w")
        dfile.write("Date_file to box block, parametrs: {:s}\n\n".format(self.str_parametrs)+
                    "{:d} atoms\n".format(len(self.system))+
                    "2 atom types\n\n"
                    "0 {:f} xlo xhi\n".format(self.wall_size[0])+
                    "0 {:f} ylo yhi\n".format(self.wall_size[1])+
                    "0 {:f} zlo zhi\n".format(self.wall_size[2])+
                    "\nMasses\n\n")

        for key in self.mass_particles.keys():
            dfile.write("{:d} {:f}\n".format(key, self.mass_particles[key]))
        
        dfile.write("\nAtoms\n\n")

        number = 1
        for item in self.system:
            if item['type'] == 1:
                dfile.write("{:4d} {:4d} {:4f} {:4d} {:4f} {:.4f} {:.4f} {:.4f}\n".format(number, item['type'], item['charge'], 0, 0.0, item['x'], item['y'], item['z']))
            if item['type'] == 2:
                dfile.write("{:4d} {:4d} {:4f} {:4d} {:4f} {:.4f} {:.4f} {:.4f}\n".format(number, item['type'], item['charge'], item['s'], item['r'], item['x'], item['y'], item['z']))
            number += 1
        if self.T_flag:
            dfile.write("\nVelocities\n\n")
            number = 1
            for item in self.system:
                if item['type'] == 1:
                    dfile.write("{:d} {:4f} {:4f} {:4f} {:4f}\n".format(number, item['vx'], item['vy'], item['vz'], 0.000))
                if item['type'] == 2:
                    dfile.write("{:d} {:4f} {:4f} {:4f} {:4f}\n".format(number, item['vx'], item['vy'], item['vz'], item['vr']))
                number += 1
        dfile.close()

    def print_xyz(self, filename, type_names = ['H', 'e']):
        dfile = open(filename, 'w')
        dfile.write("{:d}\n\n".format(len(self.system)) )
        for item in self.system:
            dfile.write("{:s} {:.4f} {:.4f} {:.4f}\n".format(type_names[item['type']-1], item['x'] * Ab, item['y'] * Ab, item['z'] * Ab))
        dfile.close()
