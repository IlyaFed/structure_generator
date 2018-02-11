def print_pdb(filename, coordinates, type_names, start_n = 0, add_to_file=False, mol = "MOL", residue_n = 1, write_type = "w"):
    '''
    :param fulleren: structure with fulleren
    :param filename: ouput name of file
    :return: 0
    '''
    f = open(filename, write_type)

    for i in range(len(coordinates)):
        type_name = type_names[ int( coordinates[i][0] )]
        f.write("{:<6s}{:5d} {:>4s}{:1s}{:<3s} {:1s}{:<4d}{:1s}   {:8.3f}{:8.3f}{:8.3f}{:>6s}{:6.2f}      {:<4s}{:>2s}\n".format(
            "ATOM", i+1+start_n, type_name + str(i), "", mol, "", residue_n ,"",
            coordinates[i][1], coordinates[i][2], coordinates[i][3], "inf", 1, "", type_name))
    f.write("TER\n")
    f.close()
