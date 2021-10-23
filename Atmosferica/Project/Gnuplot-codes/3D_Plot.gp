set terminal png font 'arial, 40' size 1280,720 

dx = 0.01   # dx = (x_max - x_min)/n_points
dt = 0.01   # dt = out_every_time
tf = 0.6    # tf = final_time

set xrange [0:1]
set zrange [-2:5]
set yrange [0:0.6]
unset key

# set xlabel "Posición"
# set ylabel "Tiempo"

imax = int(tf/dt)

set output "3D_Rnd3-Pre.png"
set title "Presión - Presión en los extremos"
splot for [i=0:imax:3] 'pres.dat'    u 2:1:3 index i w l lw 3 lc 6

set output "3D_Rnd3-Vel.png"
set title "Velocidad - Presión en los extremos"
splot for [i=0:imax:3] 'vel.dat'     u 2:1:3 index i w l lw 3 lc 2

set output "3D_Rnd3-Den.png"
set title "Densidad - Presión en los extremos"
splot for [i=0:imax:3] 'density.dat' u 2:1:3 index i w l lw 3 lc 4,