# Class Recap: Week No.10 - April 1
## Topic: DISKS!

### Summary
```
In class, on this day, we learned about disk. This included learning a little bit about proto-planetary disk, the sources of energy gain and loss in a disk, and
derivations involving our favorite friends, conservation of mass and conservation of momentum.
```


### Keplerian Velocity, $v_{kep}$

$\frac{v^3_{\phi}}{R} = \frac{\partial \phi}{\partial R}$

$v_{\phi} = \sqrt{\frac{GM}{R}}$

### Surface Density

$\Sigma = \int \rho dz$ $[g]/[cm]^2$

$\dot M = 4 \pi r^2 \rho u_r$ $[g]/[s]$

$\dot M = 4 \pi r \Sigma u_r$ $[g]/[s]$


### 1. Mass Conservation

$\int [\frac{\partial \rho}{\partial t} + \frac{\partial}{\partial r}(\rho u) = 0] * 2 \pi r dz$

$r 2 \pi \frac{\partial \Sigma}{\partial t} + \frac{\partial}{\partial r}(\Sigma u_r r 2 \pi)$

$r 2 \pi \frac{\partial \Sigma}{\partial t} + \frac{\partial \dot M}{\partial r} = 0$



### 2. Angular Momentum

$\frac{\partial Q}{\partial t} + \nabla(fQ) = F_{ext}$, $j = r^2 \Omega$, $\Sigma r^2 \Omega$

$\frac{\partial}{\partial t}(\Sigma r^2 \Omega) + \frac{\partial}{\partial r}(r u_r \Sigma r^2 \Omega) = \frac{1}{2 \pi} \frac{\partial g}{\partial r}$

where $\frac{\partial g}{\partial r}$ is the viscous torque

$g = -2 \pi r \Sigma v r^2 \frac{d \Omega}{d r}$

$\Sigma$ = mass
$v$ = viscocity

### HSEQ 

$\frac{\partial u}{\partial t} + u \cdot \nabla u = -\frac{\nabla P}{\rho} - \nabla \Phi$

$\frac{dP}{dz} = \frac{-GM \rho z}{(r^2 + z^2)^{3/2}}$, where r >> z

EOS = $P = \rho c^2_{s}$, $H = c_s/\Omega$

$\frac{dP}{dz} = \frac{-GM \rho z}{r^3 c^2_s} = \frac{-\Omega^2_* \rho z}{c^2_s}$

$\rho = \rho_0 e^{-z^2/2H^2}$

### * radical force equation (momentum conservtion in th eradial direciton)

$\frac{\partial u}{\partial t} + u \cdot \nabla u = -\frac{\nabla P}{\rho} - \nabla \Phi$

$\frac{\partial u}{\partial t} - \frac{u_{\phi}^2}{r} + u_r \cdot \frac{\partial u_r}{\partial r} = -\frac{1}{\rho} \frac{\partial P}{\partial r} - \frac{\partial \phi}{\partial r}-\frac{GM}{r^2}$

$-\frac{u_{\phi}^2}{r} + \frac{v_{k}^2}{r} = \frac{1}{\rho} \frac{dP}{dr}$ we see from this equation that disks are sub keplarian


#### More HSEQ things

$\frac{\partial \Sigma}{\partial t} = \frac{2}{r} \frac{\partial}{\partial r}(r^{1/2} \frac{\partial}{\partial r}(v \Sigma r^{1/2}))$, $t_v = R^2/v$

$\dot M = 6 \pi r^{1/2} \frac{\partial}{\partial r} (v \Sigma r^{1/2}$

$v \Sigma = \frac{\dot M}{3 \pi} [1 - (R/R_*)^{-1/2}]$

### Shakura-Sunayev 1973

$\nu = \alpha c_s H$ $[cm^2]/[s]$

$\alpha = 0.1-0.01$ this is considered "efficient"

$\alpha = 10^{-4}$

Newtonian shear stresses $\tau = \nu \rho \frac{\partial u}{\partial y} = \frac{[F]}{[A]}$


### Sources of energy gain/loss

1. Passive irradiation
2. viscous energy dissipation

$P_{in} = P_{out}$, where $f = \frac{power}{area}$
   
$P_{in} = \frac{L_*}{4 \pi r^2}A_{in}$, $P_{out} = \sigma T^4 A_{out}$

$T(r) = (\frac{L_*}{4 \pi \sigma})^{1/4} f_A^{1/4} r^{-1/2}$

$\frac{L_{\star}}{4 \pi R_{\star}^{2}} = \sigma T_{\star}^4$

$T_{\star} = (\frac{L_{\star}}{4 \pi \sigma})^{1/4} R_{\star}^{-1/2}$

$T(r) = T_{\star} f_A^{1/4} (r/R_{\star})^{-1/2}$

$D(R) = \dot E = \frac{1}{2} \nu \Sigma (R \frac{d \Omega}{dR})^{2}$

$\nu \Sigma = \frac{\ dot M}{3 \pi} [1 - (R/R_*)^{-1/2}]$, where $\Omega = \Omega_{kep}$

$\int \dot E = \int \frac{3 G M \dot M}{8 \pi R^3} [1-(R/R_*)^{-1/2}]dR$

$L_{acc} = \frac{1}{2} \frac{G M \dot M}{R_*}$

$\frac{L(r)}{4 \pi r^2} = \sigma T^4$

$T_d^4 = \frac{3 G M \dot M}{8 \pi R^3 \sigma} [1 - (R/R_*)^{-1/2}]$, where $T_d \alpha r^{-3/4}$


### PPDs
+ passive radiation
+ HSEQ
+ verticall isothermal
+ $T \rightarrow T_{dust}$

$T \propto r^{-1/2}$

$\Sigma \propto r^{-p}$

$I_{\nu} = B_{\nu}(1 - e^{-\tau_{\nu}})$

where $B_{\nu} = B_{\nu}(T)$ and $\tau = \Sigma \kappa$


### Related Resources
```
Resource contributions can go here.  
[Links]URL can be directly inserted.
You can upload files into the relevant folder and link them with a local relative link: [name][./filename.extension]
(You can even copy paste images straight into the github editor!)
```
