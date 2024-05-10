
# Class Recap: Week No.4 - Feb 21
## Topic: Molecular Clouds

### Summary
In class, we dicussed Molecular Clouds as they are where star can form and when self-gravitating becomes important. We discussed Thermal Pressure v Gravity and derived the dispersion relation. We also discussed the how to formation and destruction of Neutral Hydrogen. It is formed on grains (very slowly). It is destroyed by dissociation; Thermal or Photoelectric. We talked about the Interstellar Radiation Field introduced by Habing (1968) and the concept of self-shielding. We ended the class with a brief introduction to Orion Complex.

### Outline 

###### Thermal Pressure v Gravity:
###### Mass:
$\frac{\partial \rho'}{\partial t} + \bar{p} \frac{\partial u'}{\partial x} = 0$
###### Momentum:
$\frac{\partial u'}{\partial t} + \frac{1}{\bar\rho} \frac{\partial p'}{\partial x} = - \frac{\partial \Phi}{\partial x}$

###### We then take the time derivation of Mass and the spatial derivation of momentum and plug in the Poisson equation:
###### Poisson:
$\Delta^2 \Phi = 4\pi G \rho$ 

###### We end up with:
$\frac{\partial^2 \rho'}{\partial t^2} -c_s^s \frac{\partial^2 P'}{\partial x^2} = 4 \pi G \bar{\rho} \rho'$
###### Using the relationship:
$\rho (x,t) \propto e^{i(wt-kx)}$ 
###### The equations goes to :
$-w^2 e^{i(wt-kx)} - c_s^2 k^2 e^{i(wt-kx)} = 4 \pi G \bar{\rho}e^{i(wt-kx)}$ 
###### Solving for $w^2$ we get the dispersion relation:
$w^2 = k^2c_s^2 - 4 \pi G \bar{\rho}$\
If $w^2>0$ we get a wave\
If $w^2<0$ we get a growth (instability) 

###### To find the thresholds for the unstable modes:
$k_j=(\frac{ 4 \pi G \bar{\rho}}{c_s^2})^{\frac{1}{2}}$  \
$L = \frac{2\pi}{k}$ where $L>L_j> (\frac{\pi}{G\bar{\rho}})^{\frac{1}{2}}c_s$  Jean's Length \
$p_{th} = \rho c_s^2$ \
$p_{grav} \sim \frac{\partial \rho}{\partial R}R \sim \rho \Delta \Phi R \sim \rho \frac{GMR}{R_2^2}$ \
$R_j \sim \frac{c_s}{\rho^{\frac{1}{2}}}$ \
$M_j \sim  \frac{4\pi}{3}(\frac{L_j}{2})^2 \bar{\rho} = \frac{1}{a}(\frac{\pi^5}{G^3 \bar{\rho}})^{\frac{1}{2}} c_s^2$ 

###### The Real values:
$R_j = 1.2pc(\frac{T}{10})^{\frac{1}{2}} (\frac{n}{100cm^3})^{-\frac{1}{2}}$ \
$M_j = 10M_{\odot}(\frac{T}{10})^{\frac{3}{2}} (\frac{n}{100cm^3})^{-\frac{1}{2}}$ \
$n =4 \times 10^4 cm^{-3}$ 

###### Formation:
* On dust grains (very slow)

###### Destruction: Dissociation
* binding energy : 4.5eV
* 1 eV = $1.6 \times 10^{-12}$ ergs
* $k_b$ = $1.37 \times 10^{-16}$ ergs
###### Thermal Dissociation (collisions):\
$\frac{5}{2}kT = 4.5 eV$\
$T \approx 10^4 K$
###### Photo Dissociation:
$\frac{hc}{\lambda} = 4.5eV$ \
$\lambda = 0.2 \mu m$ [UV] \
$\lambda = \frac{2898 \mu m}{T}$  where $T= 20000K$
###### Interstellar Radiation Field (ISRF)
* Habing (1968)
* $1G_0 = 1.6 \times 10^{-3}$ ergs\ $cm^2$ \s
###### Self-Shielding
* $A_{\nu} > 0.3 for H_2$
* $A_{\nu} \sim \frac{N_H}{1.8 \times 10^{21}cm^{-2}}$ where $N_H = 6 \times 10^{20}$
* $\Delta S \cong 200pc$ >> molecular clouds








### Questions 
```
You can put questions that came up in class, or that you have yourself related to the material covered
```

### Related Resources
[(University of Amsterdam) Carsten Dominik & Inga Kamp’s Star and Planet Formation, Chapter 3: Molecular Clouds](https://staff.fnwi.uva.nl/c.dominik/Teaching/SPF/syllabus.pdf) Lecture notes from Dr. Dominik and Dr. Kamp’s UvA Master Course on Star and Planet Formation. Chapter 3 discusses the observational aspects, physical processes, and chemical composition of molecular clouds with images, tables, sky maps, and plots.

[https://academic.oup.com/mnras/article/413/4/2935/965474] This paper demonstrates how cloud collision and stellar feedback effect the gas content by allowing gravitational forces to be dominant. They found that the observations, concerning the distributions of virial parameters and cloud structures, can be effectively simulated if the star formation efficiency within these confined areas is approximately 5 to 10 percent. [Manuel Ramirez]

[http://astro1.physics.utoledo.edu/~megeath/ph6820/lecture3_ph6820.pdf] A slideshow containing all that encompass molecular clouds. [Manuel Ramirez]

