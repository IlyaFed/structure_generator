# Use atomic units
import numpy as np
from lib.molecule import *
Aborh = 0.529177208

class hydrogen_molecule(molecule):
    def __init__(self, mass_ions = [1.008], mass_electron = 0.005):
        super().__init__(mass_ions = mass_ions, mass_electron = mass_electron)
        self.distance = 0.7416/Aborh
        self.mass_h = self.mass_ions[0]
        self.full_mass = self.mass_h*2 + self.mass_electron*2

    def get(self, coordinate, velocities=np.array([0,0,0]), spin=0):
        """
        Here we define our molecule or atom in structure and return list of coord to print
        :param coordinate: coordinate of center of molecule
        :return: list of coordinates of atom and electrons
        """
        data = []
        mass_full = self.mass_h + self.mass_electron
        # electron properties TODO make it depend on temperature
        electron_r = 1.86
        electron_vr = 0
        # create H2 bond structure with random direction vector
        nucl_vector = np.random.rand(3)
        nucl_vector /= np.linalg.norm(nucl_vector)
        el_vector = np.random.rand(3)
        el_vector -= el_vector.dot(nucl_vector) * nucl_vector #make orthogonal
        el_vector /= np.linalg.norm(el_vector)
        electron_dist = 0
        nucl_vector = nucl_vector*self.distance/2.0
        el_vector = el_vector*electron_dist


        # create structure 2 x electrons, 2 x ions
        # first ion
        our_vect = coordinate - nucl_vector
        data.append( {
            'x':our_vect[0], 'y': our_vect[1], 'z': our_vect[2], 
            'vx': velocities[0], 'vy': velocities[1], 'vz': velocities[2], 
            'name': 'H', 'type': 1, 'charge': 1
            } )

        # second ion
        our_vect = coordinate + nucl_vector
        data.append( {
            'x':our_vect[0], 'y': our_vect[1], 'z': our_vect[2], 
            'vx': velocities[0], 'vy': velocities[1], 'vz': velocities[2], 
            'name': 'H', 'type': 1, 'charge': 1
            } )

        # first electron    
        our_vect = coordinate - el_vector
        data.append( {
            'x':our_vect[0], 'y': our_vect[1], 'z': our_vect[2], 'r': electron_r, 
            'vx': velocities[0], 'vy': velocities[1], 'vz': velocities[2], 'vr': electron_vr, 
            'name': 'e', 'type': 2, 'charge': 0, 's': 1
            } )
        # second electron
        our_vect = coordinate + el_vector
        data.append( {
            'x':our_vect[0], 'y': our_vect[1], 'z': our_vect[2], 'r': electron_r, 
            'vx': velocities[0], 'vy': velocities[1], 'vz': velocities[2], 'vr': electron_vr, 
            'name': 'e', 'type': 2, 'charge': 0, 's': -1
            } )
        
        if spin == 0:
            return data
        else:
            return data, 1


