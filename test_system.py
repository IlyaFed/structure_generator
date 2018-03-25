from lib.lattice import lattice

T_list = [2000, 5000, 8000, 12000, 15000, 20000, 25000, 30000, 35000, 40000, 45000]
for T in T_list:
    system = lattice("n_types 1 h2 216 rho 0.6 T " + str(T))
    system.print_lammps("output/h2/data/T"+str(T)+".lammps")
    system.print_xyz("output/h2/data/T"+str(T)+".xyz")

for T in T_list:
    system = lattice("n_types 1 h 432 rho 0.6 T " + str(T))
    system.print_lammps("output/h/data/T"+str(T)+".lammps")
    system.print_xyz("output/h/data/T"+str(T)+".xyz")

for T in T_list:
    system = lattice("n_types 2 h- 108 h3+ 108 rho 0.6 T " + str(T))
    system.print_lammps("output/h_h3/data/T"+str(T)+".lammps")
    system.print_xyz("output/h_h3/data/T"+str(T)+".xyz")