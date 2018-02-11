from lib.lattice import *
from lib.hydrogen_molecule import *

test_lattice = lattice()
rho = 1 # g/cc
N = 10
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

# Terachem test
hydrogen_no_electron = hydrogen_molecule(lattice_wall, electron_flag = 0)
hydrogen_no_electron.add(lattice_coordinates)
hydrogen_no_electron.print(filetype = 'xyz', filename = 'output/H2.xyz')

