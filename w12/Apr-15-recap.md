# Class Recap: Week No. 12 - 4/15/2024
## Topic: Proto-Star & Disk Formation

### Summary

###This lecture concerned the modes of angular momentum transport between a cloud/disk and it's central star/core.###

In this lecture we covered turbulence and broke down all the different physical mechanisms that can cause turbelence in star forming sytems.  We can model the kinetic turbulence through shearing boxes/sheets.  There are also physical affects from the global magnetic field-- the Magnetorotational Instability (MRI), and the gravitational field-- the Gravitational Instability (GI).

### Outline 

We reviewed the astrochemistry of disks:

$\quad \quad \dot{M} = constant \sim v\sigma$

$\quad \quad \nu = \alpha c_{s}H$

$\quad \quad H = \alpha \frac{c_{s}}{\Omega}$

$\quad \quad v = v_{kep} = \sqrt{\frac{GM}{R}}$

$\quad \quad \Sigma = \Sigma_{\circ} \frac{r/r_{\circ}^-P} e^{\frac{-r}{r_{d}}}$

$\quad \quad T = T_{\circ} \frac{r}{r_{\circ}^{-q}}$ , $q = \frac{1}{2}$ (for disks)

$\quad \quad M = 2\pi r_{\circ}r_{d} \Sigma_{\circ}$



## Turbulence

- Mode of angular momentum transport
- Growth of solids
- Characterized by $ \alpha $ parameter

Rayleigh Criterion: $\frac{d}{dr} (r^{2}\Omega) > 0$ (for stability)

$\Omega \propto r^{-q}, q = \frac{3}{2}$ for $\Omega = \Omega_{kep},  \Omega \propto  -qr^{-(q + 1)} \propto  \frac{q\Omega}{r}$

$r^(2)\Omega ' + 2r\Omega  > 0  \Rightarrow  \Omega (2-q) > 0  \Rightarrow  |q| < 2$ (linearly stable)

# Shearing Box/Sheet

$\ddot{\vec{r}} =  -\triangledown \Phi  -  2\vec{\Omega}_{\circ} \times \vec{v}  -  \vec{\Omega} \times (\vec{\Omega} \times \vec{r}) \quad \quad$ , where " $2\vec{\Omega}_{\circ} \times \vec{v}$ " corresponds to the Coriolis Force and " $\vec{\Omega} \times (\vec{\Omega} \times \vec{r})$ " corresponds to the Centrigugal Force

$x = x_{\circ}sin(kt + \phi), y = y_{\circ}cos(kt + \phi)  \rightarrow  k^{2} \equiv  4\Omega^{2} + 2\Omega r\frac{d\Omega}{dr}$: the Epicyclic Frequency

$k^{2} > 0$ for stability $\rightarrow$ for $\Omega = \Omega_{kep}  \rightarrow  k^{2} = 4\Omega^{2} - 2\Omega^{2}q  \rightarrow  k^{2} = \Omega^{2}$



## Magnetoroational Instability (MRI)

$\frac{\partial \rho}{\partial t} + \triangledown\cdot(\rho u) = 0$

$\frac{\partial u}{\partial t} + (u\cdot\triangledown)u   =   \cancel{-\frac{1}{\rho}\triangledown P} - \cancel{\triangledown \Phi} + \frac{1}{4\pi\rho}(\triangledown\times\vec{B})\times\vec{B} - 2\Omega_{\circ}\times u  +  2q\Omega_{\circ}^{2}x\hat{x}$ , where $\rho = \rho_{circ} ,  \vec{B} = (0\hat{x}, 0\hat{x}, B\hat{x}),  \Omega_{circ} \propto  r^{-q}, u = (0\hat{x}, -q\Omega x\hat{y}, 0\hat{z})$ 

$\frac{\partial B}{\partial t} = \triangledown\times(\vec{u}\times\vec{B})$

### Perturbations

$\quad u_{x} = u'_{x}(z_{o}t) \quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad \frac{\partial u'_{x}}{\partial t} = \frac{B_{\circ}}{4\pi\rho_{o}}\frac{\partial B'_{x}}{\partial z} + 2\Omega_{\circ}u'_{y}, 
\newline \quad  u_{y} = -q\Omega_{circ}x + u'_{y}(z_{o}t) \quad\quad\quad\quad\quad\quad\quad\quad\quad\quad \frac{\partial u'_{y}}{\partial t} = -q\Omega_{circ}u'_{x} = \frac{B_{\circ}}{4\pi\rho_{\circ}}\frac{\partial B'_{y}}{\partial z} - 2\Omega_{\circ}u'_{y}
\newline \quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\Rightarrow$ into MRI $\Rightarrow$
$\newline \quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad$ (Linearized Equations)
$\newline\quad u_{z} = u'_{z}(z_{o}t)  \quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad \frac{\partial B'_{x}}{\partial t} = B_{\circ}\frac{\partial u'_{z}}{\partial z}
\newline\quad  B'_{x} = B_{x}e^{i\omega t - kx} \quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\space\space\space \frac{\partial B'_{y}}{\partial t} = B_{\circ}\frac{\partial u'_{y}}{\partial z} - q\Omega_{\circ}B'_{x}$

$i\omega u'_{x} = \frac{-ikB_{\circ}B'_{x}}{4\pi\rho_{\circ}} + 2\Omega_{\circ}u'_{y}$

$i\omega u'_{y} = \frac{-ikB_{\circ}B'_{y}}{4\pi\rho_{\circ}} + (q-2)\Omega_{\circ}u'_{x}$

$i\omega B'_{x} = -ikB_{\circ}u'_{x}$

$i\omega B'_{y} = -ikB_{\circ}u'_{y} - q\Omega_{\circ}B'_{x}$



### Dispersion Relationship

For stability: $ \omega^{2} > 0  \quad, \quad v_{A}^{2} = \frac{B_{\circ}^{2}}{4\pi\rho_{\circ}}$

$ \quad k^{2}v_{A}^{2} - 2q\Omega_{\circ}^{2} > 0  \rightarrow  q < 0$ (MRI can be unstable whenever)

$k^{2}v_{A}^{2} = 3\Omega_{\circ}^{2}\space, \space L_{crit} = \frac{2\pi}{k_{crit}} \quad \rightarrow \quad k_{crit} = \frac{\sqrt{3}\Omega_{\circ}}{v_{A}}\quad$, unstable for $k < k_{crit}$

$H = \frac{c_{s}}{\Omega}\space,\space L_{crit} > 2H \quad \Rightarrow \quad$ MRI is suppressed $\quad \Rightarrow \quad B_{\circ}^{2} > \frac{12}{\pi}\rho c_{s}^{2}$

$P_{B} = \frac{B_{\circ}^{2}}{8\pi}\space,\space P_{G} = \rho c_{s}^{2} \quad \Rightarrow \quad \beta = \frac{P_{G}}{P_{B}}\space$, for MRI: $\space \beta > \frac{2\pi^{2}}{3}$



### Non-Ideal MHD (Magneto-Hydrodynamics)

Resistivity: $\space\eta\space$ cm/s

$\frac{d(\omega^{2})}{d(kv_{A})} = 0 \quad\rightarrow\space$ growth rate $\space\rightarrow\quad$ weak field: $\space kv_{A} << \Omega$

$\Rightarrow\space\frac{d(\omega^{2})}{d(kv_{A})} = |\omega|_{MRI} \simeq \frac{2\pi\sqrt{3}v_{A}}{L}\space\quad \leftarrow |\omega|_{\eta} \simeq \frac{\eta}{L^{2}}\space,\space L=H$

Dissipation: $\quad\rightarrow\quad\eta > 2\pi\sqrt{3}v_{A}H$

Suppression: $\quad\rightarrow\quad \frac{v_{A}H}{\eta} < 1\space,\quad$ Magnetic Reynold's Number: $\space R_{eM} < 1\space,\quad \alpha = \frac{v_{A}^{2}}{c_{s}^{2}}\space,\space R_{eM} = \sqrt{\alpha}\frac{c_{s}^{2}}{\eta H}$

### Gravitational Instability

$\frac{\partial{u}}{\partial{t}} + (u\cdot\triangledown)u = -\frac{\triangledown P}{\rho} - \triangledown\Phi - 2\Omega\times u + 2q\Omega x\hat{x}$

$m = \space$ azimuthal wave number $\quad k = \space$ radial wave number

Dispersion in rotating frames: $\quad \tilde{\omega} \equiv \omega - m\Omega(r)\space,\space \frac{GM}{R} \sim G\Sigma$

$(\omega - m\Omega(r))^{2} = c_{s}^{2}k^{2} - 2\pi G\Sigma |k| + k^{2}$

$Q = \frac{c_{s}k}{\pi G\Sigma} \space >\space 1\space$ (for stability)

Potential Dead Zone Solutions:
    - Rossby Wave Instability (RWI)
    - Vertical Shear Instability (VSI)

Brunt-Vaïsälä Frequency: $\quad N_{r}^{2} = \frac{1}{\gamma\rho}\frac{dP}{dr}\frac{d}{dr}(\ln(\frac{P}{\rho\gamma}))$


