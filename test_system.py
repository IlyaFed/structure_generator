from lib.lattice import lattice

system = lattice("n_types 1 h2 432 rho 0.6")
system.print_lattice()
system.print_lammps("output/data.lammps")