# Class Recap: Week No. 3 - Feb. 14, 2024
## Topic: Shocks! And Supernova Remnants.

### Summary

The lecture began with a recap of fluid dynamics, where we confirmed that non-linear behavior leads to shocks. We also discussed the framework of shock waves, discussing the differences between those that flow upstream and downstream, which led to expressions for Mass Flu, Momentum Flux, and Energy Flux. We then also discussed Adiabatic Shocks and Isothermal Shocks. Finally, we concluded the lecture with a discussion about Supernovae, and their various phases - Free Expansion, Energy Conserving, and Momentum Conserving.


### Outline 

Shocks occur when a wave propagates through a medium at supersonic speed, creating discontinuity.

| Upstream | Downstream | 
|:--------:|:----------:|
| "pre-shock" | "post-shock" | 
| $u_1$| $u_2$ | 
| ${\rho}_1$ | ${\rho}_2$ |
| $P_1$ | $P_2$|

<b>Mass Flux</b>

${\rho}_1u_1={\rho}_2u_2$

<b> Momentum Flux </b>

${\rho}_1u_1 + P_1={\rho}_2u_2 + P_2$

<b> Energy Flux</b>

$E_1u_1 + P_1u_1 = E_2u_2 + P_2u_2$

$u_1(\frac{1}{2}{\rho}_1u_1^2 + \frac{P_1}{{\gamma}-1} + P_1)$
$\frac{1}{2}u_1^2 + \frac{\gamma}{{\gamma}-1} \frac{P_1}{{\rho}_1} = \frac{1}{2}u_2^2 + \frac{\gamma}{{\gamma}-1}\frac{P_2}{{\rho}_2}$

$u_2 = \frac{{\rho}_1}{{\rho}_2} u_2$

$P_2 = P_1 + {\rho}_1u_1^2-{\rho}_2u_2^2$

$\frac {{\gamma}P_1}{{\rho}_1} = \frac{{\gamma}kT}{{\mu}m_H} = c_s1^2 (sound speed)P = \frac {{\rho}kT}{{\mu}m_H}$

Keeping in mind that:

<b> Ideal Gas Law </b>

$P = nkT$
$n = \frac{\rho}{{\mu}m_H}$

Therefore:

$M \equiv \frac{u_1}{c_s1}$

This can be rewritten as:

$\frac{{\rho}_1}{{\rho}_2}$ , which is the <b> compression factor </b>

$\frac{{\rho}_1}{{\rho}_2} = \frac{({\gamma}+1)M_1^2}{({\gamma}+1)({\gamma}-1)(M_1^2-1)}$

<b>Adiabatic Shock:</b>

ex. strong shock limit

$M_1 >> 1$

$\frac {{\rho}_2}{{\rho}_1} = \frac{({\gamma}+1)}{({\gamma}-1)}$

$\frac {{\rho}_2}{{\rho}_1} = 4$

$ P_2 >> P_1$

$\frac{u_2}{u_1} = \frac{1}{4}$

$P_2 = P_1 + {\rho}_1u_2 - {\rho}_2u_2$

$\frac {{\rho}kT_2}{{\mu}m_H} = {\rho}_1u_1^2 - \frac{1}{4}{\rho}_1u_1^2 = \frac {3}{4}{\rho}_1u_1^2$

$T^2 = \frac{{\mu}m}{k} \frac{3}{16}u_1^2$

In the case of adiabatic shock, ${\rho}$ <b> compresses, </b> $u$ <b> decelerates,</b> and $T$ <b> heats</b>

In the case of isothermic shock, 

<b> Supernovae: </b>:

Type II: 
M > $20 M_\odot$

$V_ej \approx 10^4 km/s$

$M_ejn \approx 5-20 M_\odot$

Type 1a:

white dwarf binaries
$M_enj: 4 M_\odot$

<b>Three phases:<b/>

$1$ Free expansion
    
$2$ Energy-conserving
    
$3$ Momentum conserving

<b> In free expansion </b>
    
$E_0v 10^51 ergs = \frac {1}{2}mv^2$
    
$R = V_ej$ x $t (KE_sn \approx KE_amb)$
    
${\rho}_1 = \frac{M_ej}{\frac{4}{3}{\pi}R^3} --> R_fe = (\frac{3M_ej}{4{\pi}{\rho}_1}^\frac{1}{3} \approx 2.2(\frac{M_ej}{M_\odot})(\frac{m_H}{cm^-3})^\frac{-1}{3} pc$
    
<b> In energy conserving </b>
    
$V_ej >> c_s$
    
$T_2 = 2 x 10^9 (\frac {v}{10^4 km/s})^2 K$

- no radiative loss
- adiabatic expansion
- "Sedov-Taylor" phase
    
$E_0 = E(t) \propto {\rho}_1^{\alpha}t^3R^{\gamma}$
    
$R \propto \frac{E_0}{{\rho}_1}^\frac{1}{5}  t^\frac{2}{5} --> R = R_0\frac{E_0}{{\rho}_1}^\frac{1}{5} t^{2}{5}$
    
$R(t_fe) = R_fe$
    
<b> In momentum conserving </b>
    
Remember that:
    
$v \propto \frac{dR}{dt} \alpha t^\frac{-3}{5}

$T < 10^6K$

snowplow phase

mv = constant

$ {\rho}_1R^3\frac{dR}{dt}$ = constant

$\int R^3dR$ = $\int \frac{const.}{{\rho}_1}$ x dt

$R^4 \propto t$

$R \propto t^\frac{1}{4}$

$\frac{dR}{dt}$ $\propto v {\alpha}t^\frac{-3}{4}$

$v \approx c_s$

<b> Some assumptions: </b>

$1. {\rho}_1$ is uniform.

$2. Ly{\alpha}$ cooling is $100$ percent effective when $T = 10^6K$

How do supernovae inject turbulence into the ISM?

Rayleigh-Taylor instability introduces Kevin-Hemholtz instabilkity.

   




```python

```


```python

```
