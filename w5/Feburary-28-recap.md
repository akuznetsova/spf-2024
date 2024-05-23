# Class Recap: Week No.5 - 2024/02/28
## Topic: 

### Summary
In this lecture, we covered the mechanisms and observations behind the stellar initial mass function as well as what dominates the upper mass initial mass function. We also covered Bondi accretion, and star formation at different scales (in theory): in the Milky Way and at extragalactic scales. This includes coverage of the Kennicutt-Schmidt "law" (or relation). 

### Outline 

Let's really get to know a friend: the initial mass function (IMF)

$\zeta(M)  = \zeta_0 M^{-2.35} = \frac{dN}{dM} = N_0 M^{-2.35} $

The stellar initial mass function was originally measured by Salpeter. 

$N = \int_{m_1}^{m_2} \zeta(m) dM = \int_{m_1}^{m_2} \frac{dN}{dM} dM  = \int_{m_1}^{m_2} dN $

Key notes: 
* the hydrogen buning limit is approximately $0.08 \ {\rm M}_\odot$, which makes it difficult to find brown dwarves.
* roughly 30% of cores translates to mass in stars. The remaining 70% is active research.
* most of the mass is in small stars while most of the luminosity is in large stars

Important caveat: Observations to constrain the IMF are done on the Milky Way are are then extrapolated to galaxies in both observations and simulations. 

What affects the upper mass IMF?
* turbulent fragmentation
* feedback (see: numerical simulations) (requires knob turning)
* structure inheritance (see: Chabrier) (note: can have too much feedback)
* magnetic fields (see: simulations) (note: fields can be too strong)
* gravitational (competitive) accretion scenario

Re: gravitational accretion scenario - If $\dot{M} = \alpha M^2$, $\frac{dN}{dM} \propto M^{-2}$, thus $\alpha = \frac{4 \pi G \rho (\infty)}{(c_{\rm s}(\infty) + v(\infty) )^{3/2}} $. This is known as Bondi-Hoyle-Littleton Accrition. 

Using linear analysis and perturbation theory, we can come up with a formalism for Bondi Accretion: 

$\frac{1 }{2 } (1 - \frac{c_s^2}{u^2}) \frac{\delta }{\delta r } u^2 = \frac{- GM }{ r^2 } \left( 1 -  \frac{2 c_s r }{ G M } \right)  $ 

$\dot{M} = 4 \pi r \rho u$

Describing the velocity flow field around a point mass in spherical coordinates in 1D given the following cases: 
1. transonic :
  i. $u^2$ -> 0, r -> 0 
  ii. $u^2$ -> $\infty$, $r$ -> $\infty$
2. $\frac{\delta }{\delta r} u^2 \rvert_{r = r_{s}} = 0 $
   iii. subsonic ($u^2 < c_s^2$)
   iv. supersonic ($u^2 > c_s^2$)

And that gives us the solution: 

$\dot{M} = 4 pi q_s \frac{G^2 M^2 \rho(\infty)}{c_s^3(\infty)}$ where $q_s = \frac{1}{4} (\frac{2}{5-3\gamma})^{\frac{5 - 3\gamma }{2\gamma - 2}} $

How to model star formation (in theory)? Can represent it simply as following: 

$\dot{M}_* = \frac{ \sum M }{ \Delta t }$ for all the stars formed at that time. 

We need to consider this at various scales.
1. Milky Way scales we can count and plot the number of YSOs against molecular cloud mass above an extention limit of $A_v > 0.05$. Mostly dependent on O and B star observations, so leaves some out ...
2. Extragalactic scales need a proxy measurement due to being unable to resolve individual stars. Kennicutt suggested using H$\alpha$ maps to constrain $\Sigma_{\rm SFR}$. 

Consider the following information. If the stellar mass of the Milky Way is $m_* \sim 6 \times 10^{10} M_\odot$, and the SFR is approximately $1.7 M_\odot / yr$, $\sum M_{\rm GMC} / t_{ff} = 450 M_\odot$ / yr. That is way too high, thus motivates the idea that in theory, star formation rate is regulated by some efficiency factor: 

${\rm SFR} = \epsilon \frac{m_{\rm gas}}{\Delta t} $

But this efficiency also depends on your gas tracer. CO emission is considered a lower limit estimate due to being optically thick emission. if $t_{ff} \propto 1 / \sqrt{G \rho}$, what density do you choose? 

Enter: Kennicutt-Schmidt "Law" - $\Sigma_{\rm SFR} \propto \Sigma_{\rm gas}^N$. Neat. But what gas do you use? the molecular stuff (N ~ 1.5)? You need a mapping between CO and H2, giving us X(CO) calibrated on gas rich spirals, need dust-gas corrections... very, very messy.  

### Questions 
