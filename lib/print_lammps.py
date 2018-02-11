def print_lammps(filename, coordinates, wall, mass_ion, mass_electron):
    dfile = open(filename, "w")
    dfile.write("Date_file to box block\n\n"+
                "{:d} atoms\n".format(len(coordinates))+
                "2 atom types\n\n"
                "0 {:f} xlo xhi\n".format(wall)+
                "0 {:f} ylo yhi\n".format(wall)+
                "0 {:f} zlo zhi\n".format(wall)+
                "\nMasses\n\n"+
                "1 {:f}\n".format(mass_ion)+
                "2 {:f}\n".format(mass_electron)+
                "\nAtoms\n\n")

    spin = 1
    r_electron = 1.823572
    number = 1
    for item in coordinates:
        if item[0] == 0:
            dfile.write("{:4d} {:4d} {:4f} {:4d} {:4f} {:.4f} {:.4f} {:.4f}\n".format(number, 1, 1.0, 0, 0.0, item[1], item[2], item[3]))
        if item[0] == 1:
            dfile.write("{:4d} {:4d} {:4f} {:4d} {:4f} {:.4f} {:.4f} {:.4f}\n".format(number, 2, 0.0, spin, r_electron, item[1], item[2], item[3]))
            spin *= -1
        number += 1
    dfile.close()
