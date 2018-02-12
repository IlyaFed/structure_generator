# all computation in bohr distance
import numpy as np
from lib.basis import *
import random

class lattice:
    def __init__(self):
        self.__doc__ = 'Here we build system for lammps, VASP and TerachemAll data present in atomic units'
        self.lattice = list()
        self.Ab = 0.529

    def from_wall(self, wall_step, wall_size, style = 'sc'):
        buf = basis()
        self.basis, self.a = buf.get(style)
        self.wall_step = wall_step
        self.wall_size = wall_size
        self.a *= self.wall_step
        self.create_lattice()
        self.N = lattice[0]
        self.rho = self.N / self.wall_size**3

    def from_rho(self, rho, N):
        buf = basis()
        self.N = N
        self.rho = rho
        self.basis, self.a = buf.get('sc')
        N_units = self.N
        wall_count = int( N_units**( 1. / 3 ) )  * 2 # 2 provide random destribution except simple cubic lattice
        self.wall_size = (self.N / self.rho) **( 1. / 3 )
        self.wall_step = self.wall_size / wall_count
        self.a = self.a * self.wall_step
        self.create_lattice()
        rand_list = random.sample(range(len(self.lattice)), self.N) # choose random place for N atoms
        real_lattice = [ self.lattice[item] for item in rand_list]
        self.lattice = real_lattice

    def __in_box(self, x):
        result = True
        result = result and ( x[0] <= self.wall_size ) and ( x[0] > 0 )
        result = result and ( x[1] <= self.wall_size ) and ( x[1] > 0 )
        result = result and ( x[2] <= self.wall_size ) and ( x[2] > 0 )

        return result

    def create_lattice(self):
        x0 = np.array([self.wall_size/2.0, self.wall_size/2.0, self.wall_size/2.0])

        n_max = int( (self.N / len(self.basis)) ** (1. / 3) )
        n = np.zeros(3)
        for n[0] in range(-n_max, n_max, 1):
            print ("\rcreate lattice: {:d} %".format(int( (n[0] + n_max) / ( 2. * n_max) * 100)), end="" )
            for n[1] in range(-n_max, n_max, 1):
                for n[2] in range(-n_max, n_max, 1):
                    for basis_vector in self.basis:
                        x = x0 + basis_vector + self.a[0] * n[0] + self.a[1] * n[1] + self.a[2] * n[2]
                        if self.__in_box(x):
                            self.lattice.append(x)
        print ("\rcreate lattice: 100 %")
    def print(self):
        print ("rho = {:.2f} 1/bohr**3, N = {:d}".format(self.rho, self.N) )
        print ("wall size = {:.2f} bohr ( {:.2f} A )".format(self.wall_size, self.wall_size * self.Ab))
        print ("")
        print ("----------------------")
        print ("| {:4s} | {:4s} | {:4s} |".format("X", "Y", "Z"))
        print ("----------------------")
        for item in self.lattice:
            print ("| {:2.2f} | {:2.2f} | {:2.2f} |".format(item[0], item[1], item[2]))
        print ("----------------------")

    def coordinates(self):
        return self.lattice

    def wall(self):
        return self.wall_size

