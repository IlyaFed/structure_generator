# Use atomic units
from lib.print_lammps import *
from lib.print_pdb import *
from lib.print_poscar import *
from lib.print_xyz import *
from lib.molecule import *
Aborh = 0.529177208

class molecule:
    def __init__(self):
        self.coordinates = list()

    def add(self, coordinates):
        for item in coordinates:
            self.coordinates.extend(self.get(item))

    def get(self, coordinate):
        """
        Here we define our molecule or atom in structure and return list of coord to print
        :param coordinate: coordinate of center of molecule
        :return: list of coordinates of atom and electrons
        """

        return coordinate

    def print(self, filetype, filename):
        if filetype == 'lammps':
            print_lammps(filename, self.coordinates, self.wall, self.mass_ion, self.mass_electron)
        if filetype == 'pdb':
            print_pdb(filename = filename, coordinates = self.coordinates, type_names = self.type_names)
        if filetype == 'POSCAR':
            print_poscar(filename, self.coordinates)
        if filetype == 'xyz':
            print_xyz(filename, self.coordinates, self.type_names)

