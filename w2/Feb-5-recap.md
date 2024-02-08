# Class Recap: Week No. 2 - Feb. 5, 2024
## Topic: Introduction to pressure sources in the ISM

### Summary
We began with a recap of the emission and absorption mechanisms of gas and dust before discussing the properties of the clouds observed throughout the Milky Way (MW) and why they appear in two distinct phases: the warm neutral medium (WNM) and cold neutral medium (CNM). We covered heating and cooling mechanisms within clouds and predicted scale heights within the galaxy, only to find a discrepancy between theoretical and observed scale heights which indicates that the ISM cannot be considered static. We finished with a brief consideration of extra pressure sources in the ISM.

### Outline 
If we observe 1 cloud:
- brightness temperature $T_B$ = source temperature $T_s(1-e^{-\tau})$

However, we usually see multiple clouds:
- cloud a (emitting) -> $T_a(1-e^{-\tau_a})$
- cloud b (background) -> $T_b(1-e^{-\tau_b})e^{-\tau_a}$

The total brightness temperature $T_B: T_a(1-e^{-\tau_a}) + T_b(1-e^{-\tau_b})e^{-\tau_a}$
- For small $\tau_a, \tau_b: T_B \simeq T_a\tau_a + T_b\tau_b$
- $T_B$ = some average source $\overline{T_s} = \frac{T_a\tau_a + T_b\tau_b}{\tau_a + \tau_b}$

We receive emission proportional to the amount of "stuff" in clouds.
- $\tau_{HI} \propto \frac{N_H}{T}$
- $\frac{N_{H_{total}}}{T_s} = \frac{N_{H_a}}{T_a} + \frac{N_{H_b}}{T_b}$

If $T_a << T_b$, cloud b's thermal emission is more intense but we get attenuation from cloud a, with which we calculate how much of an absorber is present (typically done with bright background quasar and not multiple clouds which requires modeling).

When we do absorption studies around the MW, we find cloud populations at two temperature regimes.

| Medium | $T$ ($K$) | $n_H$ ($cm^{-3}$) |
| --- | --- | --- |
| CNM | 30-100 | 1-10|
| WNM | 5000-8000 | 0.1 |

(Within MW, we use pressure unit $\frac{P}{k_b}$ ($cm^{-3} K$).) Both CNM/WNM are ~3000 $cm^{-3} K$ given their respective pressure equilibrum.

What controls T in neutral medium? T is an ensemble property representative of where most velocities of atoms sit: $\textlangle v\textrangle = \sqrt{\frac{3kT}{m_p}}$

To cool, remove energy from the system.
1. COOLING: Collisional excitation ("radiative line cooling")
- $n_cn_1q_{12} = n_cn_2q_{21} + n_2A_{21}$
    - $n_c$: # density of collision partners
    - $n_1$: # density in ground state
    - $q_{12}$: collisional excitation rate
    - $n_2$: # density in excited state
    - $q_{21}$: de-excitation rate
    - $A_{21}$: spontaneous emission coefficient

Some de-excite collisionally and some radiatively. Not in equilibrium with excitation, so temperature cools; radiative line cooling assumed in optically thin LTE. Often the collision partners are free electrons.

What sets the rate?
- Boltzmann eq. and collisional eq.
    - $q_{12} = \frac{g_1}{g_2}q_{21}e^{\frac{-E_{21}}{kT_c}}$

How much energy is lost? Radiative loss $L_R = n_2A_{21}E_{21}$

This is encoded in cooling rate: $\Lambda(T)$, sometimes written: $n^2\Lambda(T)$
- Powerful ISM coolants: CI, CII, OI
- Cooling time $t_{cool}$ = energy/loss rate $\simeq \frac{nkT}{n^2\Lambda(T)}$
    - CNM: 1.4 x $10^5$ yr
    - WNM: 4.6 x $10^7$ yr

Short timescale implies something is reintroducing energy. Other cooling: recombination line cooling (e.g. Lyman-alpha)

2. HEATING: Photoeletric effect (high energy photon frees $e^-$ from dust particle, added collision partner and kinetic energy)
- Related to number of dust, rescaled to $n_H$
    - $n_{dust} = \epsilon n_H$ (valid enough for most of ISM)

This is encoded in heating rate: $n\Gamma$. Other heating: X-rays, cosmic rays

If in thermal equilibrium (heating = cooling), we get the equilibrium pressure $P_{eq}$ and investigate as a function of density. We see two distinct ISM phases because thermal stability requires $\frac{dP}{dn} > 0$. We see two stable solutions, hard to perturb and long-lived enough to observe, which correspond to two cloud populations.

If we are looking through the galaxy at gas columns, we derive:
- $\rho(z) = \rho_0e^{\frac{-z^2}{2H^2}}$
    - z: height above disk
    - H: scale height = $\frac{c_sR}{v_c}$

Density is exponentially varying; when we move by another scale height, density becomes diffuse.

Scale height at the solar circle using calculations from hydrostatic equilibrium (HSEQ) and observations:
| Medium | HSEQ | Observed |
| --- | --- | --- |
| HNM | ~85pc | 400pc |
| CNM | ~40pc | 135pc |

What does it mean that $H_{obs} > H_{HSEQ}$?
- ISM is dynamic, seems to have more pressure support than just thermal pressure?
    - Cosmic rays?
    - Turbulence??
    - Magnetic fields?

Open question: what is moving ISM around?  

### Related Resources
```
Resource contributions can go here.  
[Links]URL can be directly inserted.
You can upload files into the relevant folder and link them with a local relative link: [name][./filename.extension]
(You can even copy paste images straight into the github editor!)
```

