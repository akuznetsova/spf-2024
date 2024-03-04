# Class Recap Feb 26

In class we learned about the Bonner-Ebert Speheres, deriving the equations related to them. That eventually led us to the Singular Isothermal Solution of said equation,
while also looking at edge cases. We also learned about cores in extinction, HII region expansion, and isothermal shock

##### mass : $\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho u) = 0$ 

##### momentum : $\frac{\partial u}{\partial t} + (u \cdot \nabla)u =  -\frac{1}{\rho} \nabla P - \nabla \Phi$

##### EOS: $P = \rho c^{2}_{s}$

##### HSEQ (u $\rightarrow$ 0): $\nabla P = -\rho \nabla \Phi$

##### $\overrightarrow{\nabla}_{r} \implies \frac{1}{r^2} \frac{d}{dr},  -\rho \frac{dP}{dr}$

With these we can then use:
##### Poisson's Equation: $\nabla^{2} \Phi = 4 \pi G \rho$

##### Making use of the equations just above Poisson's, we can sub them in, ending up with:
$\frac{1}{r^2} \frac{d}{dr} (r^2 \frac{d\phi}{dr}) = 4 \pi G \rho$

$\frac{1}{r^2} \frac{d}{dr} (-\frac{r^2}{\rho} \frac{dP}{dr}) = 4 \pi G \rho$

$\frac{1}{r^2} \frac{d}{dr} (-\frac{r^2}{\rho} c^{2}_{s}\frac{d\rho}{dr}) = 4 \pi G \rho$

##### We can make use of this identity:
$\frac{d}{dx} (ln(x)) = \frac{1}{x}$

$\frac{1}{\rho} \frac{d\rho}{dr} = \frac{d ln(\rho)}{dr}$


variable $\rightarrow$ -u = $ln(\frac{\rho}{\rho_c})$

###### Boundary Conditions:
$\rho(r=0)=\rho_c$

$\xi = r/(c^{2}_{s}/4 \pi G \rho_c)^{1/2}$

##### More math manipulations:

$\frac{d\rho}{dr} \rightarrow \frac{du}{d\xi}$

$\frac{d\rho}{dr} (\frac{dr}{d\xi}) (\frac{du}{d\rho}) = \frac{du}{d\xi}$ several of the terms cancel here

##### we also want to make use of these:
$-du = \frac{d\rho}{\rho}$, $\rho= \rho_c e^{-u}$ <br/>

$\frac{du}{d\rho} = -\frac{1}{\rho} = -\frac{1}{\rho} e^{u}$

##### Continuing:

$d\xi = dr/(c^{2}_{s}/4 \pi G \rho_c)^{1/2}$ <br/>

$(\frac{c^{2}}{4 \pi G \rho})^{1/2} = \frac{dr}{d\xi}$

##### We end up with the Lane-Emden Equation via:
$\frac{1}{\xi^2} \frac{d}{d\xi} (\xi^{2} \frac{du}{d\xi}) = e^{-u}$

##### We then end up with:
$\xi_1 = r_{core}/(c^{2}_{s} / 4 \pi G \rho)$ (Bonner, 1956)

$\rho(\xi_1) = \rho_{amb} (\rho_c/\rho_{amb}$ (Ebert, 1955)

##### Edge case:
$\xi_1 \rightarrow \infty$, $\rho_c \rightarrow \infty$

$\rho = c^{2}_{s} r^{-2}/2 \pi G$ known as the Singular Isothermal Solution (SIS)
