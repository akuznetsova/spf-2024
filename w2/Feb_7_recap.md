

# Class Recap: Week No. 2 - Feb. 07, 2024
## Topic: Fluid Dynamics

## Summary

In this lecture we began with a recap of fluid dynamics which consists of the conservation of mass, conservation of momentum as well as the conservation of energy in which the conservation of energy lead us to the wave equation once it was derived. This lead us to the virial theorem in order to describe the behavior. Further, we went over an equation made by Larson in 1981 which concluded that the observed behavior was due to turbulence. 

## Outline 

Consider a cube of length $dv$, where $\overline{v}$ 
and $\rho$ is the mass density of the cube and $dm = \rho * dv$

### Conservation of Mass
$\Mass = mass_{in} - mass_{out}$

### Mass Flux equation:
$\int\int\int\rho * mu \cdot \hat{n} dA$
$\int\nabla \cdot(rho*u)=0$

$\frac{\partial \rho}{\partial t} + \nabla \cdot(rho*u)=0$  Continity equation

### Lagrangian/ Convective Derivative:

$\frac{D \rho}{Dt}  = \frac{\partial \rho}{\partial t} + \nabla \cdot(rho*u)=0$

### Conservation of momentum:

$\rho \left( \frac{dv}{dt} + \mathbf{v} \cdot \nabla \mathbf{u} \right) = - \nabla \mathbf{P} - \rho \nabla \mathbf{\Phi} + \nabla \cdot \mathbf{\Pi}$
 
 Where $\ - \nabla \mathbf{P}$ is the pressure gradient and

$\mathbf{\Phi} = -\nabla \mathbf{\Phi}

Recall:
$\nabla \cdot (\rho \mu) = \mu \nabla \cdot (\rho \mu) + \rho\mathbf{u}\mathbf{v} \mathbf{u}$

Which is the same as 

$\left (\frac{dpu}{\partial t}\right) = \frac{\partial \rho\mu }{\partial t} +  \frac{\rho \, dv}{\partial t}$

$\=-\nabla \cdot (\rho \u) + \frac{\rho \, dv}{\partial t}$

Finally, we have
$ \rho \left( \frac{dv}{dt} + \mathbf{u} \cdot \nabla \mathbf{u} \right)$

### Conservation of Energy:
Equation of State (EOS) relates $\( P(\rho) \)$ to pressure by
$\P = \rho \cdot C_s^2$

$\P \propto \frac{1}{\rho^\gamma}$

where $\( \gamma = \frac{5}{3} \)$ for atoms or $\( \frac{7}{5} \)$ for molecules (barotropic equation of state).

$\E = \frac{1}{2} \rho \cdot y^2$

which is defined as
$\E = \frac{1}{2} \rho \cdot y^2$


### The Wave Equation

Starting from
$\frac{\partial \rho}{\partial t} + \frac{\partial pu}{\partial x} = 0$

Which becomes
$\frac{\rho du}{\partial t} + \frac{\rho u du}{\partial x} + \frac{\partial \rho}{\partial x}$

where
$\rho = \bar{\rho} + \rho' \cdot \frac{\rho'}{\rho} \ll 1$

and $\rho = \bar{\rho} + \rho'$ is the same as $u = \bar{u} + u'.$

Equation (17) becomes
$\frac{\partial}{\partial t} (\bar{\rho} + \rho') + \frac{\partial}{\partial x} ((\bar{\rho} + \rho') u') = 0$

After this we have
$\2t \left( \frac{\partial \rho'}{\partial t} + \bar{\rho} \frac{\partial u'}{\partial x} \right) = 0$

which becomes
$\(\rho' + \rho) \frac{du'}{dt} + u'(\bar{\rho} + \rho') = \frac{du'}{\partial x} + \frac{\partial(\bar{\rho} \rho')}{\partial x} < 0$

which then becomes
$\frac{\partial u'}{\partial t} + \frac{1}{\bar{\rho}} \frac{\partial \rho'}{\partial x} = 0$

where $\rho = c_s^2$ which is the sound speed. Further
$\frac{\partial}{\partial x} \left( \frac{\partial u'}{\partial t} + \frac{c_s^2}{\rho} \frac{\partial \rho'}{\partial x} \right) = 0$

almost there
$\frac{\partial^2 \rho}{\partial t^2} + \bar{\rho} \frac{\partial}{\partial t} \left( \frac{\partial u'}{\partial x} \right) = 0$

which then becomes
$\frac{\partial}{\partial x} \left( \frac{\partial u'}{\partial t} \right) + c_s^2 \frac{\partial^2 \rho}{\partial x^2} = 0$

which results in our wave equation
$\frac{\partial^2 \rho}{\partial t^2} + c_s^2 \frac{\partial^2 \rho}{\partial x^2} = 0$

### Virial Theorem
In Virial Theorem you have a group of of things that behave in a certain way.

$\C_1 = \sum_{i} \mathbf{P}_i \cdot \mathbf{r}_i = \int \rho \, dV$

If you integrate

$\\frac{dG}{dt} = \int \rho \frac{du}{dt} \cdot \mathbf{r} \, dv + \int \rho u \, dv + 2 \text{KE}$ where $r = \frac{dr}{d\phi} = (n+1) \phi$

=$\int (F_{\text{ex}} + F_{\text{ext}} + \ldots) \cdot \mathbf{r} \, dv$

=$\int \nabla \cdot \mathbf{P} \cdot \mathbf{r} \, dv - \int\rho \nabla \cdot \mathbf{\Phi} \cdot \mathbf{r} \, dv$

 =$\int \rho (\nabla \cdot \mathbf{r}) \, dv$

 = $\int\int\rho (\mathbf{r} \cdot \mathbf{\hat{n}}) \, ds = \int 3 \rho \, dN$ where $ds = -s \rho (n+1) \phi \, dv$

= $\frac{du}{dt} = 3pv - (n+1)v + 2KE$

= $\frac{1}{\tau} \int_{0}^{\tau} \frac{dG}{dt} t \, dt = \frac{G(\tau) - G(0)}{\tau} = 0$ 

This is the Virial Equilibrium.
We sum up all stat. Averages in a system and they add up to 0.

$\0 = \langle 2KE \rangle + \langle 3PV \rangle - (n+1) \langle U \rangle$

### Example 1
If (n+1) is not given:
$\frac{3}{2} NKT = 3 NKT \Rightarrow NKT = PV$
$\Rightarrow NKT = PV$

### Example 2
$\0 = \langle 2KE \rangle - \langle 3PV \rangle - (n+1) \langle U \rangle$
$\\langle 2KE \rangle + \langle U \rangle = 0$

To describe equilibrium state of clouds:
$\sum_{i} = \frac{\mu}{R^2}$

$\<U> \sim \frac{GMm}{R}$


$\<2KE> \sim \kappa \langle v \rangle^2 \langle v \rangle \sim GR\sum$

$\langle v \rangle^2 = GR\sum$

$\langle V \rangle = \left(GR\sum\right)^{1/2}$

In freefall $E_{\text{total}} = 0$

$\0 = \mu + KE$

$\nu = \left(2GR\sum R\right)^{1/2}$
