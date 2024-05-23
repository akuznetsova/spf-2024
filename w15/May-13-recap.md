
# Class Recap: Week No. 15 - May 13th, 2024
## Topic: Growing Planetesimals 

### Summary
```
In this lecture we talk about growing planetesimals. We first look at the three body problem involving a star, mass, and the planetesimal, then we solve for the Hill radius - the radius at which the mass will fall onto the planetismal. We then go through two different pathways of growth, collisional and pebble accretion. Finally, we talk about planet migration, and the various cases for where it occurs.
```

### Outline 
  - Previously on S&P
    - Streaming Instability
    - Growing dust through collisions
      - fragmentation or bouncing
  - Growing Planetesimals
    - Aerodynamic Regime
      - Begin with dust [cms]
      - Streaming instability gets the dust past barriers
    - Gravitational Regime
      - Once past barriers, you have planetesimals ~100[kms]
        - $\dot{M} \propto M^P$
      - 3 body problem
        - If you have a planetesimal some distance from some mass to be gained, all some distance from a star:
        - $\frac{GM_p}{r_H^2} - \frac{GM_*}{(a-r_H)^2} + \Omega_k^2(a-r_H) = 0$
        - where $r_H$ is the Hill radius $r_H = (\frac{M_p}{3M_*})^\frac{1}{3}a$
      - "Traditional Collisional Growth" (Armitage, 2010)
        - $\frac{M}{t} = \frac{\sqrt{3}}{2} \Sigma_p \Omega_k \pi R^2(1+\frac{v_{esc}^2}{\sigma^2})$ where $v_{esc} = \sqrt{\frac{2GM}{R}}$
        - $\sigma$ is the velocity dispersion
          - if $\sigma$ is constant and much less than $v_{esc}$, it is the runaway growth regime
          - if $\sigma \propto M$, then it is the oligarchic growth regime
        - $dM = \Sigma_p dA$ where $dA = 2\pi a C r_H$
        - $M_{iso} = \frac{8}{\sqrt{3}} \pi^\frac{3}{2} C^\frac{3}{2} M_*^\frac{-1}{2} \Sigma_p^\frac{3}{2} a^3$
          - Fiducial values
            - $a = 1$au
            - $\Sigma_p = 10 [g/cm^2]$
            - $C = 2\sqrt{3}$
            - $M_{iso} = 0.07$ Earth masses
      - Pebble Accretion (Ormel, Klahr 2007) (Lambrehts and Johansen, 2012)
        - $r_H = (\frac{M}{3M_*})^{1/3} a$
        - $r_B = \frac{GM}{\Delta v^2}$
          - $\Delta v$ is the approach speed $ = \frac{1}{2} \eta v_k$ where $\eta = \frac{1}{2}(\frac{H}{R})^2 \frac{d\ln P}{d\ln R}$
        - Three cases
          - $r_B < r_H$
            - Drift dominated accretion
            - $t_s , t_B$, $t_B = \frac{r_B}{\Delta v}
          - $r_B > r_H$
            - Hill dominated accretion
            - $\Delta v \sim \Delta v_H \sim \frac{-3}{2} \Omega_k r_H$
          - $r_B = r_H$
            - $M_t = \sqrt{\frac{1}{3}} \frac{\Delta v^3}{G\Omega}$ : transition mass
    - Migration
      - $v_K \propto \sqrt{\frac{GM}{r}}$
      - $\Sigma \propto r^{-p}$
      - $T \propto r^{-q}$
      - planet migration
        - Is there a gap opening?
          - type I, no gap
            - $2 \cdot 10^{5} yr ~ 10^{6} yr
            - total migration torque:
              - $\sum_{ILR} T_{LR} + \sum_{OLR} T_{LR} + T_{LR}$
              - ILR gains momentum, OLR loses momentum
              - $T_{LR} \propto \Sigma M_p^2$
              - $K \propto \Omega^2 + \frac{d\Omega}{dR}$
          - type II, yes gap
            - $r_H\geq H$
            - $(\frac{M_p}{3M_*})^{\frac{1}{2}}r_p > H$
            - $q = (\frac{M_p}{M_*}) \geq 3(\frac{H}{r})^3 \sim 10^{-4}$

### Questions 
```
You can put questions that came up in class, or that you have yourself related to the material covered
```

### Related Resources
[(University of Amsterdam) Chris Ormel’s Planet Formation course](https://staff.fnwi.uva.nl/c.w.ormel/Teaching/planet-formation.pdf). Notes from Dr. Ormel’s UvA course on Star and Planet Formation. Sections 1.6 and 1.7 cover the concepts of runaway and oligarchic growth and pebble accretion, providing plots and graphics that demonstrate the differences between growth models, including geometries and timescales involved.
