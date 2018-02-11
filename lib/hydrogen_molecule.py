# Use atomic units
import numpy as np
from lib.molecule import *
Aborh = 0.529177208

class hydrogen_molecule(molecule):
    def __init__(self, wall, mass_ion = 1.008, mass_electron = 0.005, electron_flag = 1):
        self.distance = 0.7416/Aborh
        self.coordinates = list()
        self.electron_flag = electron_flag
        if self.electron_flag:
            self.type_names = ['I', 'E']
        else:
            self.type_names = ['H']
        self.wall = wall
        self.mass_ion = mass_ion
        self.mass_electron = mass_electron

    def add(self, coordinates):
#        self.coordinates.extend(self.get(coordinates[0]))
        for item in coordinates:
            self.coordinates.extend(self.get(item))
    def get(self, coordinate):
        """
        Here we define our molecule or atom in structure and return list of coord to print
        :param coordinate: coordinate of center of molecule
        :return: list of coordinates of atom and electrons
        """
        coord = []
        nucl_vector = np.random.rand(3)
        #nucl_vector = np.array([0.0,0.0,1.0])
        nucl_vector /= np.linalg.norm(nucl_vector)
        el_vector = np.random.rand(3)
        el_vector -= el_vector.dot(nucl_vector) * nucl_vector #make orthogonal
        el_vector /= np.linalg.norm(el_vector)
        electron_dist = 0;
        nucl_vector = nucl_vector*self.distance/2.0
        el_vector = el_vector*electron_dist

        our_vect = coordinate - nucl_vector
        coord.append( np.array([0] + list(our_vect) ))

        our_vect = coordinate + nucl_vector
        coord.append( np.array([0] + list(our_vect) ))

        if self.electron_flag:
            our_vect = coordinate - el_vector
            coord.append( np.array([1] + list(our_vect) ))

            our_vect = coordinate + el_vector
            coord.append( np.array([1] + list(our_vect) ))

        return coord # format [type, x, y, z]


