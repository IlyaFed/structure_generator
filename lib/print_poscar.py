def print_poscar(filename, coordinates, wall):
    ab = 0.529
    dfile = open(filename, "w")
    dfile.write("H\n" +
                "1.0000000000000000\n" +
                "{:.6f}       0.000000        0.000000\n".format(wall*0.529) +
                "0.000000        {:.6f}       0.000000\n".format(wall*0.529) +
                "0.000000        0.000000        {:.6f}\n".format(wall*0.529) +
                "{:d}\n".format(int(len(coordinates)/2.)) +
                "Cartesian\n"
                )
    number = 1
    for item in coordinates:
        if item[0] == 0:
            dfile.write("{:d} {:.4f} {:.4f} {:.4f}\n".format(number, item[1]*ab, item[2]*ab, item[3]*ab))
        number += 1
    dfile.close()