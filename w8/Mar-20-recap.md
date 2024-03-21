# Class Recap: Week No. 8 - Mar. 20, 2024
## Topic: The Protostellar Class System

### Summary
We began with a discussion of actions to take for the upcoming midterm: post paper of chosen observational study; prepare slides to synthesize next week; and set up individual progress meeting by the exam. We then discussed dust opacities in disks, the protostellar class system, corresponding spectral energy distributions, and what our observations tell us about the structure of the systems we study.

### Outline 
Star-forming regions are very dense with gas and dust coupled. As gas density increases, dust density and consequently extinction increases.

$I_\nu = I_{\nu_0}e^{-\tau_\nu} + B_\nu(T)(1 - e^{-\tau_\nu})$

- The first term corresponds to absorption/extinction
- The second term corresponds to thermal emission

We can discuss elements of optical depth with $d\tau_\nu = \kappa_\nu \rho ds$.

- $\rho ds$ reflects dust morphology
- $\kappa$ is dependent on dust properties
    - General behavior of opacity with $\lambda$: extinction(optical) > extinction(IR).

$\kappa_\nu = \kappa_0(\lambda/\lambda_0)^{-\beta}$

- Where $\beta$ encapsulates dust composition, maximum size (amax), power-law (p)

Unlike optical, in IR we can see thermal emission component (e.g. IRAS mission which finally observed "IR excess" sources).

Looking at thermalized dust component, $B_\nu(T)(1 - e^{-\tau_\nu})$:

- $B_\nu$ corresponds to blackbody emission
- $(1 - e^{-\tau_\nu})$ corresponds to attenuation

Wien's law encodes where most emission comes from: $\lambda = \frac{2898 \mu m}{T [K]}$

#### Class 0

- Spherical rotating infall stage
- Hydrostatic core with envelope
- Herbig-Haro object with collimated jets
- $M_* < M_{env}$
- $t < 30,000 yr (< t_{ff})$

#### Class I

- Disk formation
- Less collimated outflows (forming cavities)
- $M_* > M_{env}$
- $t \sim 200,000 yr (\sim t_{ff})$

**It can be difficult to tell the classes apart (attenuation, observational angle, short timescales involved). Often grouped into class 0/I.**

**People posit that "birthline" is between class I and class II. Observationally, the point where you become more likely to see protostar.**

#### Class II

- Classical T-Tauri systems (CTTS)
- Assume no more envelope
- Disk has yet to fully condense/disperse (photoevaporation)
- $M_{disk} \lesssim 0.1 M_{\odot}$ (limit due to self-gravity)
- $t \sim Myr$ 

#### Class III

- "Weak" TTS
- Now a debris disk
- Properties of dust from collisions, no longer coupled to gas
- $M_{disk} \lesssim M_{Jup}$
- $t \sim 10 Myr$

IRAS "IR excess" sources show disk fraction decreases with time. 10 Myr bound comes from observations.

From canonical models:

| Class | $\dot{M}_{accretion}$ | $\dot{M}_{jet}$ |
| --- | --- | --- |
| 0 | $10^{-6}-10^{-5} M_{\odot} /yr$ | $10^{-7}-10^{-6} M_{\odot} /yr$ |
| I | $10^{-7}-10^{-6} M_{\odot} /yr$ | $10^{-8}-10^{-7} M_{\odot} /yr$ |

Outflow spurts can create multiple shocks ("knots"). Relative velocities are used to infer candence/episodic-ness of outflow. Inclination can complicate identification of outflow behavior.

#### SEDs

*Class 0*

From distribution $\rho = \frac{\dot{M}}{4\pi r^2 v_{ff}} = \frac{\dot{M}}{4\pi r^2 \sqrt{\frac{2GM}{r}}}$

Integrating along LOS and making assumptions about $\kappa$ to calculate $\tau$:

$\tau_\lambda = \int \kappa_\lambda \rho dr = \frac{\kappa_\lambda \dot{M} r^{\frac{-1}{2}}}{2\pi (2GM)^{\frac{1}{2}}}$

Assume optically thick regime ($\tau = \frac{2}{3} \sim$ "photosphere" of system). We can fine $r_\lambda = (\frac{9}{4})\frac{\kappa_\lambda^2 \dot{M}^2}{8\pi GM}$

To get the blackbody peak:

$L = 4\pi r_\lambda^2 \sigma T_\lambda^4 \rightarrow$ (plugging in Wien) $\rightarrow \frac{\lambda}{\lambda_0} = (\frac{2898 \mu m}{\lambda_0})(\frac{4\pi \sigma}{L})^\frac{1}{(4 + 4\beta)}(\frac{9\dot{M} \kappa_0}{32\pi GM})^\frac{1}{(2 + 2\beta)}$

With $\kappa_\lambda = 0.2(\frac{\lambda}{100 \mu m})^{-2}$,

$\lambda = 30(\frac{L}{L_{\odot}})^{\frac{-1}{12}}(\frac{\dot{M}}{2\times 10^6 M_{\odot}/yr})^{\frac{1}{3}}(\frac{M}{0.5 M_{\odot}})^{\frac{-1}{6}} \mu m$

Standard values for class 0: $\sim 30 \mu m$ and $100 K$. We don't see the protostar because it's heavily enxtincted in the visual.

How far into the system do we see? Dependent on $\lambda$ (deeper at longer $\lambda$).

$r_\lambda = (\frac{9}{4})0.2^2(\frac{\lambda}{100 \mu m})^{-2} \frac{(2 \times 10^{-6} M_{\odot}/yr)^2}{8\pi G (0.5 M_{\odot})}$

*Class I*

Now we see a conical cavity and can start to see more. Each $\lambda$ mostly probes different T components (short $\lambda \rightarrow$ hottest grains, etc.). Optical/near IR: light can be scattered into LOS from cavity walls. Some will send light back to disk midplane ("backwarming") and thermalize to higher T.

In this class the emission peak moves to smaller $\lambda$, while the shape flares out at longer $\lambda$ due to the (mostly) envelope and disk.

*Class II*

Assume the disk is optically thin, so the SED shape depends on amount of material. The emission peak continues moving to even smaller $\lambda$ (with $10 \mu m$ silicate bump).

- $T \propto (\frac{r}{r_0})^{-q} \rightarrow B_\nu(R)$
    - $q = 1/2$
- $\Sigma \propto (\frac{r}{r_0})^{-p} \rightarrow \tau_\nu(R)$
    - $p = 1-2$

We can divide system into annuli, with each annulus $I_\nu \sim B_\nu(T)\tau_\nu$. We try to recover disk morphology accordingly.

Knowing sublimation $T_{sub} = 1400-1800K$, there must $\lambda_{min}$ describing inner edge of dust disk component ($\lambda_{min} = 1.5 \mu m$).

Trying to recover $M_{disk}$ (assuming optically thin regime): 

$I_\nu = B_\nu(T)\kappa \Sigma R^2 \rightarrow F_\nu = \sum B_\nu(T) \kappa \Sigma R^2 / d^2$

$M_{dust} = \frac{F_\nu d^2}{\kappa_\nu B_\nu(T_{dust})}$

$M_{disk} = M_{dust}/\epsilon$, where $\epsilon$ is ratio of gas/dust (taken from ISM)

**The protostellar class system comes from Andre 1994; backfilled from observations. For diagnostic, $\alpha_{IR} = \frac{dlog(\lambda F_\lambda)}{dlog\lambda}$.**

- $\alpha_{IR} > 0$: class I
- $-1.5 < \alpha_{IR} < 0$: class II

### Related Resources