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

**Three phases:** 

1. Free expansion  
2. Energy-conserving  
3. Momentum conserving  

**In free expansion**  
    
$E_0 =  10^51 ergs = \frac{1}{2} mv^2$  
    
$R = V_{ej} \times t (KE_{sn} \sim KE_{amb})$
    
$\rho_1 = \frac{M_{ej}}{\frac{4}{3}\pi R^3} \rightarrow R_fe = \left(\frac{3 M_{ej}}{4 \pi\rho_1}^{\frac{1}{3}} \sim 2.2(\frac{M_{ej}}{M_\odot}\right) \left(\frac{m_H}{cm^-3} \right)^{\frac{-1}{3}} pc$
    
**In energy conserving**  
    
$V_{ej} >> c_s$
    
$T_2 = 2 \times 10^9 \left(\frac{v}{10^4 km/s}\right)^2 K$  

- no radiative loss  
- adiabatic expansion  
- "Sedov-Taylor" phase  
    
$E_0 = E(t) \propto \rho_1^{\alpha} t^3 R^{\gamma}$
    
$R \propto \frac{E_0}{\rho_1}^{\frac{1}{5}}  t^{\frac{2}{5}} \rightarrow R = R_0 \frac{E_0}{\rho_1}^{\frac{1}{5}} t^{\frac{2}{5}}$  
    
$R(t_{fe}) = R_{fe}$
    
**In momentum conserving**  
    
Remember that:  
    
$v \propto \frac{dR}{dt} \alpha t^{\frac{-3}{5}}$
  
$T < 10^6K$

snowplow phase  

mv = constant  

$\rho_1 R^3 \frac{dR}{dt}$ = constant

$\int R^3 dR$ = $\int \frac{\mathrm{const.}}{\rho_1} \times dt$

$R^4 \propto t$

$R \propto t^{\frac{1}{4}}$  

$\frac{dR}{dt}$ $\propto v {\alpha} t^{\frac{-3}{4}}$  

$v \sim c_s $

**Some assumptions:**  
1. ${\rho}_1$ is uniform.  
2. $Ly_{\alpha}$ cooling is 100 percent effective when $T \lessim 10^6 K$  

How do supernovae inject turbulence into the ISM?

Rayleigh-Taylor instability introduces Kevin-Hemholtz instabilkity.


### Related Resources
[(University of Maryland) Benedict Diemer’s ASTRO 670 Hydrodynamics, Chapter 8: Shocks](http://www.benediktdiemer.com/wp-content/uploads/astr670_hydro_notes.pdf). Notes from Dr. Diemer’s UMD course on The ISM and Hydrodynamics. Chapter 8 introduces shocks and, starting in 8.2, provides images alongside the equations discussed in class (Mach number, Rankine-Hugoniot conditions, etc.) as well as plots visualizing properties of supernova blast waves.

[Bamba & Williams, 2022. Supernova Remnants: Types and Evolution](https://ui.adsabs.harvard.edu/abs/2022hxga.book...77B/abstract) Handbook chapter summarizing the evolution of supernova remnants (SNR) through the free expansion, blast wave, and snowplow phases as well as dissipation, providing images to accompany the relevant equations governing the processes. Also discusses and displays various SNR types with examples.
