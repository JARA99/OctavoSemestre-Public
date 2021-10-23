set terminal gif font 'arial' 20 size 1280,720 animate delay 10
set output "Rnd2.gif"

set title "Presión en los extremos"

set key outside
set grid

set font ",12"

#============================================
#
# Set these variables before plotting!
#
#============================================

# dx = (x_max - x_min)/n_points
dx = 0.01

# dt = out_every_time
dt = 0.01

# tf = final_time
tf = 1

set xrange [0:1]
set yrange [-2:5]

set grid mytics mxtics
set mytics 3
set mxtics 3



imax = int(tf/dt)
print imax

do for [it=0:10] {
    t=0
    plot \
	 'pres.dat'    u 2:3 index 0 w l lw 3 lc 6 t sprintf( "Presión, t=%.3f", t ), \
	 'vel.dat'     u 2:3 index 0 w l lw 3 lc 2 t sprintf( "Velocidad, t=%.3f", t ), \
	 'density.dat' u 2:3 index 0 w l lw 3 lc 4 t sprintf( "Densidad, t=%.3f", t )	 
    # print t
    # pause -1
}

do for [it=0:imax] {
    t=it*dt
    plot \
	 'pres.dat'    u 2:3 index it w l lw 3 lc 6 smooth csplines t sprintf( "Presión, t=%.3f", t ), \
	 'vel.dat'     u 2:3 index it w l lw 3 lc 2 t sprintf( "Velocidad, t=%.3f", t ), \
	 'density.dat' u 2:3 index it w l lw 3 lc 4 t sprintf( "Densidad, t=%.3f", t )	 
    # print t
    # pause -1
}

# do for [it=0:5] {
#     t=tf
#     plot \
# 	 'pres.dat'    u 2:3 index imax w l lw 3 lc 6 t sprintf( "Presión, t=%.3f", t ), \
# 	 'vel.dat'     u 2:3 index imax w l lw 3 lc 2 t sprintf( "Velocidad, t=%.3f", t ), \
# 	 'density.dat' u 2:3 index imax w l lw 3 lc 4 t sprintf( "Densidad, t=%.3f", t )	 
#     # print t
#     # pause -1
# }