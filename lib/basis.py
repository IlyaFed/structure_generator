import numpy as np

class basis:
    def __init__(self):
        self.a = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        self.basis = []
        self.__doc__='Describe simple unit of lattice'

    def get(self, style):
        if (style == "sc"):
            self.basis.append(np.array([0.0,0.0,0.0]))
        if (style == "bcc"):
            self.basis.append(np.array([0.0,0.0,0.0]))
            self.basis.append(np.array([0.5,0.5,0.5]))
        if (style == "fcc"):
            self.basis.append(np.array([0.0,0.0,0.0]))
            self.basis.append(np.array([0.5,0.5,0.0]))
            self.basis.append(np.array([0.5,0.0,0.5]))
            self.basis.append(np.array([0.0,0.5,0.5]))
        if (style == "hcp"):
            self.basis.append(np.array([0.0,0.0,0.0]))
            self.basis.append(np.array([0.5,0.5,0.0]))
            self.basis.append(np.array([0.5,5.0/6.0,0.5]))
            self.basis.append(np.array([0.0,1.0/3.0,0.5]))
            self.a[1][1] *= 3.0**0.5
            self.a[2][2] *= (8.0/3.0)**0.5
        if (style == "sq"):
            self.basis.append(np.array([0.0,0.0,0.0]))
        if (style == "sq2"):
            self.basis.append(np.array([0.0,0.0,0.0]))
            self.basis.append(np.array([0.5,0.5,0.0]))
        if (style == "hex"):
            self.a[1][1] *= 3**0.5
            self.basis.append(np.array([0.0, 0.0, 0.0]))
            self.basis.append(np.array([0.5, 0.5, 0.0]))

        return self.basis, self.a
