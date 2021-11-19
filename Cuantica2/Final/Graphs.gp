##############################################################

#   Author:     Jorge Alejandro Rodriguez Aldana
#   Gnuplot:    Version 5.2 patchlevel 8
#   Date:       Nov 18, 2021

##############################################################

set terminal pdfcairo enhanced
i = {0,1}

##############################################################
######################  Problema 3  ##########################
##############################################################

#####   Graph of P_{-+}

set output 'Prob1-P1.pdf'

set title "Gráfica de P_{+-}"
set xlabel '(ω_o-ω)'
set ylabel "P_{+-}"

# k = 1
w = 1

p(x) = k*w*(1/(k+x**2)**2)
plot for [k=1:5] p(x) t 'v^2/a^2 = '.k

unset output

#####   Graph of P'_{-+}

set output 'Prob3-P2.pdf'

set key opaque
set title "Gráfica de P'_{+-}"
set xlabel '(ω_o-ω)'
set ylabel "P'_{+-}"

k = 1

g(x) = p(x)*abs(1+exp(i*x*b))**2
plot for [b=1:30:10] g(x) t 'b/v = '.b

unset output

##############################################################
######################  Problema 2  ##########################
##############################################################

#####   Graph of cross section 

set output 'Prob2.pdf'

set title "Secciones eficaces de dispersión diferencial"
set xlabel 'θ'
set ylabel 'dσ/dΩ'

k = 1
U = 1
a = 1

q(x) = 2*k*sin(x/2)

Yukawa(x) = U**2*(1/(a**(-2)+q(x)**2)**2)
Coulumb(x) = U**2*(1/q(x)**4)
Exponential(x) = 4*U**2*(a**6/((a**2*q(x)**2)+1)**4)
Pozo(x) = U**2*((sin(q(x)*a)-q(x)*a*cos(q(x)*a))/q(x)**3)**2

plot Yukawa(x) t 'Yukawa', Exponential(x) t 'Exponencial', Pozo(x) t 'Pozo de potencial'

unset output

set output 'Prob2-C.pdf'

plot Yukawa(x) t 'Yukawa', Coulumb(x) t 'Coulumb', Exponential(x) t 'Exponencial', Pozo(x) t 'Pozo de potencial'

unset output