Ab = 0.529 # our coord in bohr but print in Angstrem
def print_xyz(filename, coordinates, type_names):
    dfile = open(filename, 'w')
    dfile.write("{:d}\n\n".format(len(coordinates)) )
    for item in coordinates:
        dfile.write("{:s} {:.4f} {:.4f} {:.4f}\n".format(type_names[int(item[0])], item[1] * Ab, item[2] * Ab, item[3] * Ab))
    dfile.close()

