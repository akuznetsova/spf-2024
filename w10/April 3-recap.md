
# Class Recap: Week No. 10 - April 3
## Topic: Accretion Parameters

### Summary
Discussed how all the different accretion parameters are related and which ones depend on eachother. Did the same for Flux of the accretion disc. We then created a Fiducial model for Radition, $\nu_{isc}, and a Minimum Mass Solar Nebula (MMSN).

### Outline 
### Fiducial Values
$T_\star = 4000K$ \
$R_\star = 2 R_\odot$ \
$M_\star = M_\odot$ \
$f_A = 0.5$ \
$r_0 = 1 Au$ \
$q = \frac{1}{2} \quad Radiation$ \
$q = \frac{3}{4} \quad  \nu_{isc}$ \
$\dot{M} = 10^{-8} \frac{M_\odot}{yr}$ \
$\Sigma _0 = 1700 \frac{g}{cm^2}$ \
$p = 1$ \
$r_d = 100 Au$ \
$1 Au = 1.496 \times 10^{13} cm$ \
$R_\odot = 69.6 \times 10^9 cm$ \
$\mu =24$ \
$\gamma = \frac{7}{5}$
$km = 10^5 cm$ \
$\frac{km}{s} \approx \frac{1pc}{Myr}$ \
$h = 0.05 - 0.1$ \
$\alpha = 10^{-4}$ \
$1yr = 3.14 \times 10^7 s$ 

### Model
#### Radiation
$I_\nu = B_\nu(T)(1-\tau)$ \
$\Sigma = \Sigma _0(\frac{r}{r_0})^{-p}$ \
$T = T_0(\frac{r}{r_0})^{-q}$ \
$T(r) = T_0(\frac{r}{r_0})^{-q}$ \
$T_{eq,rad}(r)=T_\star f_A^{\frac{1}{4}}(\frac{r}{R_\star})^{-\frac{1}{2}}$ \
$T_(r_0)=T_0=T_\star f_A^{\frac{1}{4}}(\frac{r}{R_\star})^{-\frac{1}{2}}$ \
$T_0 = 324K(\frac{T_\star}{4000K})(\frac{f_A}{0.5})^{\frac{1}{4}}(\frac{R_\star}{2R_\odot})^{-\frac{1}{2}}$ \
$T_{0,\oplus} = 278K = 14^\circ C$
#### $\nu_{isc}$
$T_{\nu_{isc}}^4 = \frac{3GM \dot{M}}{8\pi R^2 \sigma}[1 -(\frac{R}{R_\star})^{-\frac{1}{2}}]$ \
$T_{\nu_{isc}}(r_0) = T_0$ \
$T_0 = 83K(\frac{M_\star}{M_0})^{\frac{1}{4}}(\frac{\dot{M}}{10^{-8}\frac{M_\odot}{yr}})^{\frac{1}{4}}(\frac{f}{0.9})^{\frac{1}{4}}$

#### Minimum Mass Solar Nebula (MMSN)
$\Sigma = \Sigma _0 (\frac{r}{r_0})^{-p}e^{(\frac{-r}{r_d})}$ \
$\nu  \propto R^\gamma$ \
$\Sigma (r) = \Sigma _c (\frac{r}{r_c})^{-\gamma}e^{-(\frac{r}{r_d})^{2-\gamma}}$ \
$\int dM = \int \Sigma (r)2\pi rdr$ \
$p=1 \rightarrow M_d = \Sigma _0 2\pi r_0 \int e^{\frac{-r}{r_d}}dr = 2\pi r_0 r_d (0.63) \Sigma _0$ \
$M_d = 0.075M_\odot(\frac{r_d}{100Au})(\frac{\Sigma _0}{1700\frac{g}{cm^2}})$ \
$c_s = \sqrt{\frac{\gamma kT}{\mu m_H}}$ \
$c_s = 1.2\frac{km}{s} (\frac{T_0}{324K})^{\frac{1}{2}}(\frac{r}{r_0})^{\frac{-q}{2}}$ \
$\nu _{kep} = \sqrt{\frac{GM}{r}} = 30 \frac{km}{s}(\frac{M_\star}{M_\odot})^{\frac{1}{2}}(\frac{r}{r_0})^{-\frac{1}{2}}$ \
$\Omega _{kep} =\sqrt{\frac{GM}{r^3}} =2s^{-1}(\frac{M_\star}{M_0})^{\frac{1}{2}}(\frac{r}{r_0})^{-\frac{3}{2}}$ \
$t_{orb} = p = \frac{2\pi}{\Omega _{kep}} =1yr(\frac{M_\star}{M_\odot})^{\frac{1}{2}}(\frac{r}{r_0})^{\frac{3}{2}}$ \
$H = \frac{c_s}{\Omega _{kep}}$\
$h= \frac{c_s}{\nu _{kep}} = 0.04(\frac{M_\star}{M_\odot})^{-\frac{1}{2}}(\frac{r}{r_0})^{\frac{1-q}{2}}$ \
$\nu = \alpha c_s H$ \
$\nu _0 = 10^{-4} \times 1.25 \frac{km}{s} \times 0.04Au$ \
$\nu _0 = 7.5 \times 10^{12} \frac{cm^2}{s}$ \
$t_\nu = \frac{r^2}{\nu} = 3 \times 10^{13}s = 1Myr(\frac{r}{r_0})^2$

### Questions 
```
You can put questions that came up in class, or that you have yourself related to the material covered
```

### Related Resources
```
Resource contributions can go here.  
[Links]URL can be directly inserted.
You can upload files into the relevant folder and link them with a local relative link: [name][./filename.extension]
(You can even copy paste images straight into the github editor!)
```

