# Class Recap: Week No. 12 - 4/17/2024
## Topic: Proto-Star & Disk Formation

### Summary

This lecture concerned the modes of angular momentum transport between a cloud/disk and it's central star/core.  Specifically we went over how there is a distinction to be made in the processes that determine the physics of the gas versus the dust in the system and when these two regimes become coupled/decoupled.

### Outline 

We reviewed the angular momentum transport between the different parts of the disk and our core star:

Dust to Gas Ratio: $\epsilon_{ISM} = 0.01$

1)  Molecular Cloud Core (Gas + Dust): 
    $\newline \quad L = 10$ pc $\space,\space n_{H} \sim 10^{3}$ cm $^{-3}$
    $\newline \quad t_{ff} \space\leq\space 1$ Myr

2)  Diffuse Disk (Gas + Dust): 
    $\newline \quad L = 0.1$ pc $\space , \space n_{H} \sim 10^{5}$ cm $^{-3}$
    $\newline \quad t_{ff} \space\sim\space 10^{5}$ yrs

3)  Disk: 
    $\newline \quad L = 100$ au $\space , \space n_{H} \sim 10^{11} - 10^{13}$ cm $^{-3}$
    $\newline \quad t_{\nu} \space\sim\space 3-10$ Myrs

For Dust: $\quad v = v_{kep} = \sqrt{\frac{GM}{R}}$

For Gas: $\cancel{\frac{\partial u}{\partial t}} + (u\cdot\triangledown)u = {-\frac{1}{\rho}\triangledown P} - \triangledown\Phi \quad, \quad$ " $ \space \frac{\partial u}{\partial t}$ " canceled because Steady-State Cylindrical Radial Force Equation

$\Rightarrow \quad \cancel{u_{r}\frac{\partial u_{r}}{\partial r}} - \frac{u_{\phi}^{2}}{r} = \frac{1}{\rho}\frac{dP}{dr} - \frac{GM}{r^{2}} \space\leftarrow\space \frac{v_{kep}^{2}}{r}$
$\newline\quad\quad M = 4\pi r\Sigma\space , \space P = \rho c_{s}^{2}\space , \space \Omega_{k} = \frac{v_{kep}}{r} \space , \space H = \frac{c_{s}}{\Omega_{k}} \quad\rightarrow\quad \frac{H}{R} = \frac{c_{s}}{v_{kep}} \space , \space h = \frac{H}{r}\space$ (Aspect Ratio) 

$\Sigma = \Sigma_{\circ}(\frac{r}{r_{\circ}})^{-P} \space\space , \space\space T = T_{\circ}(\frac{r}{r_{\circ}})^{-q} \quad \leftarrow \quad$ where: $\space P = 1 \space, \space q = \frac{1}{2}$

$\frac{u_{\phi}-v{k}}{v_{k}} \space\equiv\space\eta\space\equiv\space \frac{1}{2}(\frac{H}{r})^{2}\frac{d\ln{P}}{d\ln{r}}\quad,\space$ where: $\quad \eta < 0\space$: sub-keplerian, $\quad \eta > 0\space$: super-keplerian


Drag: $F_{D} = \frac{1}{2}\rho u^{2}c_{D}A$

Epstein Drag Regime: $F_{D} = -\frac{4\pi}{3}\rho_{g}a^{2}v_{th}v_{rel} \quad\Leftarrow\quad v_{th} \rightarrow \sqrt{\frac{8}{\pi}}c_{s} \space\space , \space\space v_{rel} \rightarrow (u_{d} - u{g})$

Stopping Time: $t_{stop} \space\rightarrow\space \frac{d\rho}{dt} = F_{D}\space , \space m = \frac{4\pi}{3}a^{3}\rho_{s} \quad\leftarrow\quad \rho_{s} = $ particle density

$t_{stop} = dt = \frac{d\rho}{F_{D}} = \frac{mu_{rel}}{F_{D}} \space\Rightarrow\space \frac{\rho_{s}}{\rho_{g}}\frac{a}{v_{th}} \quad\Rightarrow\quad $ as $\space a\uparrow\space , \space t_{stop}\uparrow \quad$ and as $\quad \rho_{g}\uparrow\space , \space t_{stop}\downarrow$

Stoke's Number: $S_{t} = t_{stop}\Omega_{k} = \frac{\rho_{s}}{\rho_{g}}\frac{a}{\sqrt{\frac{8}{\pi}c_{s}}}\Omega_{k} \quad$ , where $\space " \rho_{s}a"\space$ correlates to the dust and  $\space " \frac{\Omega_{k}}{\rho_{g}\sqrt{\frac{8}{\pi}}c_{s}} " \space$ correlates to the gaseous disk

H.S.E.Q.: $\quad\rho_{g}(r,z) = \rho_{mid}e^{-(\frac{z^{2}}{2H^{2}})}$

$\quad\quad\quad\quad\Sigma = \sqrt{2\pi}H\rho_{mid}$

$\quad\quad\quad\quad S_{t} = \frac{\rho_{s}a\sqrt{2\pi}}{\Sigma_{g}\sqrt{\frac{8}{\pi}}} = \frac{a\rho_{s}}{\Sigma_{g}}\frac{\pi}{2} \quad\Rightarrow\quad S_{t} \gg 1 \space = \space$ well-coupled

Example Values: $\newline\quad r_{\circ} = 1$ au
$\newline\quad\Sigma_{\circ} = 1700$ g/cm $^{2}$
$\newline\quad\rho_{s} = 1.7$ g/cm $^{2}$
$\newline\quad S_{t} = \frac{a}{1\text{cm}} = 0.002 \quad\Rightarrow\quad r\space$ @ $\space 100$ au: $\quad S_{t} \simeq 0.2$


### Gas-Dust Feedback

$ u_{r,d} = \frac{u_{g,r}}{1 + S_{t}^{2}} + \frac{2\eta v_{k}}{S_{t} + \frac{1}{S_{t}}} \quad\Leftarrow\quad \eta > 0\space$ : super-keplerian $\space , \space\eta < 0\space$ : sub-keplerian

For a 1mm particle:
$\newline\quad$ Drift time: $\quad t_{drift} = \frac{r}{u_{r,d}} = \frac{r(S_{t} + \frac{1}{S_{t}})}{2\eta v_{k}} \space , \space t_{orb} = \frac{2\pi r}{v_{k}} \quad\Rightarrow\quad t_{drift} \simeq 5\times 10^{5}$ yrs
$\newline\quad\quad\quad S_{t, 1mm} = 2\times 10^{-4}(\frac{r}{r_{\circ}})$
$\newline\quad\quad\quad\rightarrow\space$ So... $\space \epsilon \neq \epsilon_{ISM}\space , \space r_{d,g} \neq r_{d,d}\space , \space S_{t} = 0.002(\frac{a}{\text{cm}}) \space\leftarrow\space$ Radial Drift Barrier

### Questions 


### Related Resources

