import numpy as np

def get_basis(style):
    ''' 
    Describe simple unit of lattice
    return: basis (list), lattice_vector(3x3)
    '''
    a = np.array([[1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]])
    basis = []
    if (style == "sc"):
        basis.append(np.array([0.0,0.0,0.0]))
    if (style == "bcc"):
        basis.append(np.array([0.0,0.0,0.0]))
        basis.append(np.array([0.5,0.5,0.5]))
    if (style == "fcc"):
        basis.append(np.array([0.0,0.0,0.0]))
        basis.append(np.array([0.5,0.5,0.0]))
        basis.append(np.array([0.5,0.0,0.5]))
        basis.append(np.array([0.0,0.5,0.5]))
    if (style == "hcp"):
        basis.append(np.array([0.0,0.0,0.0]))
        basis.append(np.array([0.5,0.5,0.0]))
        basis.append(np.array([0.5,5.0/6.0,0.5]))
        basis.append(np.array([0.0,1.0/3.0,0.5]))
        a[1][1] *= 3.0**0.5
        a[2][2] *= (8.0/3.0)**0.5
    if (style == "sq"):
        basis.append(np.array([0.0,0.0,0.0]))
    if (style == "sq2"):
        basis.append(np.array([0.0,0.0,0.0]))
        basis.append(np.array([0.5,0.5,0.0]))
    if (style == "hex"):
        a[1][1] *= 3**0.5
        basis.append(np.array([0.0, 0.0, 0.0]))
        basis.append(np.array([0.5, 0.5, 0.0]))

    return basis, a
