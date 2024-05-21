# Class Recap: Week No. 7 - March 11, 2024
## Topic: Magnetohydrodynamics

### Summary
```
In this lecture, we were introduced to ideal magnetohydrodynamics, and the equations that drive these processes. Those equations included conservation of mass, conservation of momentum, Ohm's law, and Maxwell's equations. We then had a brief run through magnetic flux and polarization of grains. The magnetic flux comes into play because, in order for stars to form, gravity must be able to overcome the magnetic forces as play.
```

### Outline 
#### MHD Equations
  - Valid for highly magnetized plasmas and large scale motions
  - Mass Conservation
    - $\frac{\partial \rho}{\partial \tau} + \nabla \cdot (\rho u) = 0$
    - $\rho$ is
  - Momentum Conservation
    - $\rho(\frac{\partial u}{\partial t} + u \cdot \nabla u) = -\nabla P + \overrightarrow{j} \times \overrightarrow{B}$
      - $\overrightarrow{j}$ is current density, $\overrightarrow{B}$ is magnetic field, and their cross product is the Lorentz force
  - Ohm's Law
    - $j = \sigma E'_{r}$
      - $\sigma$ is the conductivity of the medium, and $E'_{r}$ is the displacement field
      - The displacement field is the electric field in the frame of the fluid.
        - To change the frame of reference, use a Lorentzian transform, so $E' = \overrightarrow{E} + \overrightarrow{u} \times \overrightarrow{B}$
  - Maxwell's Equations
    - $\overrightarrow{\nabla} \times \overrightarrow{E} = -\frac{\partial \overrightarrow{B}}{\partial t}$
      - $-\frac{\partial \overrightarrow{B}}{\partial t} = \overrightarrow{\nabla} \times (\overrightarrow{u} \times \overrightarrow{B})$
    - $\overrightarrow{\nabla} \times \overrightarrow{B} - \frac{1}{c^2} \frac{\partial \overrightarrow{E}}{\partial t} = \mu_0 \overrightarrow{j}$
      - $\overrightarrow{j} = -\rho e (\overrightarrow{u_e} - \overrightarrow{u_i})$
  - Combining the momentum equation and second Maxwell equation:
    - $\frac{\overrightarrow{j} \times \overrightarrow{B}}{c} = \frac{(\overrightarrow{\nabla} \times \overrightarrow{B}) \times \overrightarrow{B}}{4\pi}$
    - Using a vector identitiy, this becomes:
      - $\frac{\overrightarrow{j} \times \overrightarrow{B}}{c} = \frac{\nabla |B|^2}{8\pi} + \frac{1}{4\pi} (\overrightarrow{B} \cdot \nabla \overrightarrow{B})$
        - The first term describes the magnetic pressure, which resists compression perpendicular to field lines
        - The second term describes the magnetic tension, which seeks to flatten the field's curvature
  - Magnetic Flux
    - $\psi = \int_{s} \overrightarrow{B} \cdot d\overrightarrow{s}$
      -  Solving this:
      -  $\frac{\partial \psi}{\partial t} = \int_{s} \frac{\partial \overrightarrow{B}}{\partial t} \cdot d\overrightarrow{s} + \int_{C} \overrightarrow{B} \cdot \overrightarrow{u} \times dr$
      -  $= \int \overrightarrow{\nabla} \times \overrightarrow{E}d\overrightarrow{s} + \int \overrightarrow{\nabla} \times (\overrightarrow{B} \times \overrightarrow{u}) \cdot d\overrightarrow{s}$
      -  $\frac{\partial \psi}{\partial t} = \int \overrightarrow{\nabla} \times (E + \overrightarrow{u} \times \overrightarrow{B}) \cdot d\overrightarrow{s}$
      -  For ideal MHD, $\frac{\partial \psi}{\partial t} = 0$ (constant) which is refered to as Flux Freezing
        - There are two options to beat flux freezing
          - Dissipative processes
          - Ambipolar diffusion

#### Some star formation stuff
  - To form stars, gravity must be greater than magnetic pressure
    - $\nabla \Phi > \frac{\nabla B^2}{8\pi}$
    - $\frac{GM^2}{R} > \frac{B^2}{8\pi} \cdot \frac{4\pi}{3}R^3$
    - From this we find the mass to flux ratio's critical value to be $\frac{M}{\Phi} = \frac{0.12}{\sqrt{G}}$
#### Ended on a short note about grain polarization
  - A grain will align with a magnetic field due to its non-spherical shape
    - Absoprtion leads to polarization that is parallel to the magnetic field
    - Emission leads to polarization that is perpendicular to the magnetic field
  - On large scales, the magnetic field is perpendicular to the filament, but the opposite is true for small scales


### Questions 
```
A question came up about the form of Ohm's law being used, with the one used in class being the original statment, vs. what is taught for circuitry. 
```

### Related Resources
```

```

