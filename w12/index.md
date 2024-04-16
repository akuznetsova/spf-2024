
# Week 12 Learning Objectives
## Planet-forming Disks: the birthplaces of planets
Motivation: Planet-forming disks are where planets are assembled, in order to understand what determines the composition and architecture of planetary systems, we have to understand how the raw ingredients from the ISM are processed, transformed, and transported within planet-forming environments. 

### I. Beyond the Steady State: Disk Instabilities
What kind of physical regimes could lead to non-linear behavior?  
- Magnetorotational Instability (MRI)
- Gravitational Instability (GI)
- Rossby-Wave Instability (RWI)
- Vertical Shear Instability (VSI)

### II. Gas vs. Dust Dynamics
- Stokes number and dust drift
- Important timescale in dust evolution
- Pressure bumps
- Collision outcomes: Bouncing, Sticking, Fragmentation

    
### Recaps
Apr 15:  
Apr 17:  

### Resources
[Birnstiel+2016](https://ui.adsabs.harvard.edu/abs/2016SSRv..205...41B/abstract): A very comprehensive review of dust dynamical evolution in protoplanetary disks  
[Phil Armitage's Instability Notes](https://indico.nbi.ku.dk/event/764/contributions/5088/attachments/1723/2428/armitage_nbi.pdf)  
[Lesur+2020](https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/magnetohydrodynamics-of-protoplanetary-discs/0557575DE812AAA9DD8324A5E6F6165A): Some notes on epicyclic perturbation and instability analyses for MHD systems  
[Epicyclic motion in the Galaxy](https://web.mit.edu/~lianaiad/Public/OCW/8.284/lec28.pdf)  
[Meheut+2013](https://academic.oup.com/mnras/article/430/3/1988/980053): Primer on the Rossby Wave Instability in disks
[Kratter+Lodato 2016](https://academic.oup.com/mnras/article/430/3/1988/980053): Comprehensive review on the Gravitational Instability in disks

### HW 12 Objectives
Due April 29th (end of spring break)
1. Code up an analytical fiducial model for a protoplanetary disk
2. Learn how to use RADMC-3D to predict the temperature and emission from a disk
3. Test the results of analytical model vs. radiative transfer. 

**Assignment Instructions**
[Last week](../w11/index.md), you were asked to install RADMC-3D - a public piece of astronomical software that utilizes MCMC methods to perform radiative transfer calculations. 
This week, we will take some steps to run and evaluate a disk model using radiative transfer calculations. 

If at this point, you're still having trouble with your installation, the course binder hub has been updated to include an installation of RADMC-3D.  

As a reminder:   
You can access the binder hub for this course at: [https://binder.flatironinstitute.org/~akuznetsova/models](https://binder.flatironinstitute.org/~akuznetsova/models)
or by heading to [https://binder.flatironinstitute.org/](https://binder.flatironinstitute.org/) and entering

owner: `akuznetsova`
project: `models`

The folder will contain the github folder for this course titled `spf-2024` in which you will find copies of the homework notebooks and course materials as well as the libraries installed for running any of the code. Anything you generate with binder is hosted on a server unique to you, the server will run keeping all your notebooks, data, and computations until you shut it down (or after 7 days of inactivity). 

You can download the notebook you ran and any files you generate directly to your computer using the `Download` button. 
*Please remember to rename the notebook from the template name prior to submission*
