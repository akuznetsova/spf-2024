# Class Recap: Week No. 1 - Jan. 31, 2024
## Topic: What is Star Stuff?

### Summary

We learned about what star stuff is made of by dividing it into 
two categories - dust and gas. We further discussed how to detect 
gas in the interstellar medium, and how to detect dust, and the 
complexities of dust distributions. We went through multiple 
radiative transfer-related calculations relevant to the homework
due next week.


### Outline 

Star Stuff (ISM):
- Gas:  
    + line emission detection  
      - neutral H  
      - ionized H  
    + integrated line intensity: $J_{line}=\frac{1}{4\pi}\int\ \int\ I_{\nu} \phi(\nu)d\nu d\Omega$  
        + atomic H $\lambda$ = 21 cm  
        + Local thermodyanic equilibrium: absorption = emission  
- Dust:  
      + continuum ~ 1 micron  
      + absorbs @ short $\lambda$, emits at long $\lambda$  
      + Mie theory:   
          - $m = n(\lambda) - ik(\lambda)$, where m is an index of refraction  
          - for $x=\frac{2\pi a}{\lambda}$;  
              + x << 1: Rayleigh scattering  
              + x = ??: Mie theory  
              + x >> 1: optics regime
          + Efficiency factor:   
              - $Q_i =\frac{\sigma_i}{\pi*a^2}$  
                  - refers to how much like coming into a dust grain makes its way out  
            + Wien's law: $\lambda_{max} = \frac{2898\mu m k_B}{T}$  
            + Size distributions: $n(a)da = n_0(\frac{a}{a_{min}})^{-P} da$  
                - P = power law index  
- Radiative transfer equation: $\frac{dI_\nu}{d\tau_\nu} = S_\nu - I_\nu$  
    + gas (line emission):  
      - $\tau_\nu = \kappa_\nu dS$  
      - $S_\nu = \frac{j_\nu}{\kappa}$  
    + dust (Continuum):  
      - $\kappa_\nu = \rho_d\kappa_\nu^{dust}$  
      - $\rho_d = n_d m_d$  
- Dust to gas ratio of ISM: 1%  

### Related Resources
```
Resource contributions can go here.  
[Links]URL can be directly inserted.
You can upload files into the relevant folder and link them with a local relative link: [name][./filename.extension]
(You can even copy paste images straight into the github editor!)
```

