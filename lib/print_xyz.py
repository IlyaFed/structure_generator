def print_xyz(filename, coordinates, type_names):
    dfile = open(filename, 'w')
    dfile.write("{:d}\n\n".format(len(coordinates)) )
    for item in coordinates:
        dfile.write("{:s} {:.4f} {:.4f} {:.4f}\n".format(type_names[int(item[0])], item[1], item[2], item[3]))
    dfile.close()

