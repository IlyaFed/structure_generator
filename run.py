from lib.lattice import lattice
import os
rho = 0.8
N = 1000

com_folder = "output/to_publish/rho" + str(rho)
try:
    os.stat(com_folder)
except:
    os.mkdir(com_folder)

T_list = [2000]#, 5000, 8000, 12000, 15000, 20000, 25000, 30000, 35000, 40000, 45000]

dir = com_folder + "/h2/"
try:
    os.stat(dir)
except:
    os.mkdir(dir)

for T in T_list:
    system = lattice("n_types 1 h2 " + str(N) + " rho " + str(rho) + " T " + str(T))
    system.print_lammps(dir + "T"+str(T)+".lammps")
    system.print_xyz(dir + "T"+str(T)+".xyz")


#dir = com_folder + "/h/"
#try:
#    os.stat(dir)
#except:
#    os.mkdir(dir)
#for T in T_list:
#    system = lattice("n_types 1 h 432 rho " + str(rho) + " T " + str(T))
#    system.print_lammps(dir + "T"+str(T)+".lammps")
#    system.print_xyz(dir + "T"+str(T)+".xyz")
#
#dir = com_folder + "/h_h3/"
#try:
#    os.stat(dir)
#except:
#    os.mkdir(dir)
#for T in T_list:
#    system = lattice("n_types 2 h- 108 h3+ 108 rho " + str(rho) + " T " + str(T))
#    system.print_lammps(dir + "T"+str(T)+".lammps")
#    system.print_xyz(dir + "T"+str(T)+".xyz")
