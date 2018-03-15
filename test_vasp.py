from lib.lattice import *
from lib.hydrogen_molecule import *
from lib.hydrogen_atom import *
from lib.hydrogen_atom_minus import *
from lib.hydrogen_triatomic import *
import numpy as np

'''
def velocity_generate(Temp, m, N):
    def func(v):
        k = 1
        return 4. * np.pi * v**2 * ( m / 2 / np.pi / k / Temp)**(3./2) * np.exp( - m * v**2 / 2 / k / Temp)

    velocity = []
    for i in range()
'''
############# H2 #############
test_lattice = lattice()
rho = 0.6 # g/cc
N = 216
m = 2 # mass of one unit ( H2 )
aem = 1.66e-24
ab = 0.529e-8
rho_n = rho/(m * aem)
atom_unit_rho = rho_n*ab**3
test_lattice.from_rho(rho = atom_unit_rho, N = N)
test_lattice.print()
lattice_coordinates = test_lattice.coordinates()
lattice_wall = test_lattice.wall()

hydrogen = hydrogen_molecule(lattice_wall)
hydrogen.add(lattice_coordinates)
hydrogen.print(filetype = 'pdb', filename = 'output/H2.pdb')
hydrogen.print(filetype = 'lammps', filename = 'output/H2.lammps')
hydrogen.print(filetype = 'poscar', filename = 'output/H2.poscar')

