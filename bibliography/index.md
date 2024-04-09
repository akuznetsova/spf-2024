# Annotated Bibliography

*Instructions:*
Using the template below (you can copy/paste) add an entry to this annotated bibliography. A good annotated bibliography entry synthesizes the paper's message, rather than re-wording the abstract. This is a good place to practice reading papers critically. Most papers are motivating and presenting an argument, they tend to have a message and a point of view. Even if the details are highly technical, papers are still required to present a logical argument. As you read, try to identify what claims are being made and assess the validity of the claims. A good starting point is looking for self-consistency between what the paper states as its goals and what is actually being done -- i.e. does it hang together?

Some questions to ask as you read:

1. Are the starting assumptions appropriate for the questions the paper wishes to address?
2. Are the methods/measurements representative of the system described by the starting assumptions? For ex, are they comparing apples to apples?
3. Do the results support the claims being put forth? Are there alternative interpretations you can come up with?
4. Are the claims relevant to the motivation?

> To be eligible for points, uploads should be committed with a commit message title "BIB CONTRIBUTION - [NAME]" with a brief commit description of topic keywords. You are welcome to split the work and credit with a classmate, simply put multiple names in the commit title so that total points can be split between contributors. 

Template:
```
[(Author et. al, year)](url to ads abstract link) *Paper Title*

Paragraph: Summary of the main point of the paper, in your view.
Insights/things of interest in the contents. 

Paragraph: Relationship to the course material (be specific as possible).
 
(Optional Paragraph: Questions you had while reading,
 salient connections to other papers we've talked about)
```

[Kritsuk et. al. 2021](https://arxiv.org/abs/1309.5926) 
*A supersonic turbulence origin of Larson's laws*

The paper takes measurements made out of ISM simulations and attempts to understand how Larson's law hold up. It describes the simulations in detail, and discusses specific effects such as gravity, and their relevance to the outcomes of the simulations. The paper determines that Larson's laws do indeed hold up at larger scales on the 0.1 - 50 pc order, and are a sign of kinetic energy entering a system. It takes the importance of molecular clouds in star formation theory, and works to understand how turbulence and gravity align with Larson's laws, 

This paper obviously discusses Larson's laws, of which we discussed the size-linewidth relation in class. As discussed in class, Larson found the relation as a result of a molecular cloud's internal velocity dispersion, cloud size, and mass. The clouds are theorized to have formed due to regular gravitational turbulence, as well as supersonic turbulence, which we were better able to understand through the example of a SNe remnant.


[Bonilla-Barroso et. al. 2022](https://ui.adsabs.harvard.edu/abs/2022MNRAS.511.4801B/abstract) 
*Gravity or turbulence V: star-forming regions undergoing violent relaxation*

In this paper, Bonilla-Barroso et. al. explore star cluster formation through simulations, particularly testing two different formation scenarios - a turbulent scenario (TC), and a chaotic collapse scenario. The authors take these scenarios and model them against data of the Orion Nebula Cluster (ONC), of Stars and Planet Formation classroom fame. This is relevant as there is a predominant idea that the formation of the stars in the ONC occurred through a turbulent process. To compare the star cluster formation scenarios, the authors took types of simulations, three runs for each scenario, and used empirical data selected a total of 1989 stars from a selected ONC region, noting their parallax, proper motions, masses, ages, and effective temperatures, using the GAIA-EDR3.
they found that the the global collapse simulations had a relatively flat velocity dispersion. The turbulence simulations showed a range in velocity dispersions, with higher velocity dispersions being associated with higher mass stars, showing a clear difference between the collapse and turbulence scenarios! The ONC histograms also show relatively flat velocity dispersion with no relationship to the masses binned, which visually looked a lot like the collapse scenario. 

I found this paper to be extremely clear to read (thanks Aleksandra!) The paper itself discusses the gravitational collapse vs turbulence star formation scenarios that we discussed in class, and puts them to the test against empirical data (from the ONC which we also learned about in class). This method of comparison is a lot easier on my brain than having to explicitly try and interpret results from a simulation standing on its own. The paper also briefly touches on concepts that are integral to understanding how overdensities play a role in forming stars, namely Larson's law and the Jeans mass. The paper had a clear goal and took the reader from start to finish, and I would highly recommend reading this to see how what we have learned practically applies.


[(Ballesteros-Paredes et. al, 2020)](https://ui.adsabs.harvard.edu/abs/2020SSRv..216...76B/abstract) *From Diffuse Gas to Dense Molecular Cloud Cores*

This paper summarizes current knowledge of molecular clouds (MC) by describing cloud formation, discussing the tools to understand their dynamics, and describing their connection to star formation. The authors link MC properties and lifecycles to their galactic environments, explore the calculations and numerical simulations that investigate MC formation, break down cloud statistics, and look at cloud substructure. The paper supplements and expands on several topics we’ve covered in the course so far, including H2 molecule formation; the use of the virial theorem to describe MC physical states and associated caveats; some MC ensemble properties; interstellar radiation and Habing units; the Salpeter power IMF; the prestellar core mass function; and more. The inclusion of observational and simulation data to visualize certain concepts helps drive them home. Since this paper is in the form of a review, it doesn’t necessarily present a singular argument but uses historical and recent literature to critically discuss hypotheses about MC formation, morphology, link to star formation, etc. I found it to be dense with information but helpful for reviewing our class discussions in a little more detail.


[(Elia et al, 2022)](https://ui.adsabs.harvard.edu/abs/2022ApJ...941..162E/abstract) *The Star Formation Rate of the Milky Way as seen by Herschel*

In this paper the authors use protostellar clump catalog data from the Herschel Infrared Galactic Plane (Hi-GAL) survey to present a new calculation of the Milky Way’s current star formation rate (SFR), as well as its distribution across the Galactic plane. They select targets whose spectral energy distributions have shapes eligible for a modified black body in the range $160-500 \mu m$ and checked for detection of an emission excess within these targets at $70 \mu m$ for classification as star forming or starless. The authors consider both a few ten thousand protostellar clumps with heliocentric distance determinations and an additional few thousand targets without. To determine each target’s contribution to the SFR, they use theoretical evolutionary tracks from bolometric luminosity vs. mass relations to calculate the final mass of the internal protostar and total elapsed time, accounting for potential distance biases. Using the sources with determined distances, they find the lower limit of the global SFR to be $1.7 \pm 0.6 M_\odot yr^{-1}$, with 84% from within the solar circle and 16% from without. For the targets without distances, they simulate an equivalent number of distances whose distribution follows the one of the known distances and randomly assign them to the sources without distances, repeated 100 times; taking these additional sources into account, the SFR becomes $2.0 \pm 0.7 M_\odot yr^{-1}$. This value is fairly consistent with SFRs in previous literature. The authors also analyze the behavior of the SFR density averaged in concentric rings vs. Galactocentric radius, finding an inner peak at the Central Molecular Zone, followed by a dip corresponding to a shortage of sources, another peak around 5kpc, and a systematic decrease at larger distances; this behavior is qualitatively similar to profiles found in previous work. Ultimately the authors find that the relation between SFR density and molecular gas surface density Galactocentric profile follows a Kennicutt-Schmidt behavior (beyond 3 kpc).

This paper covers a few topics that we’ve discussed in class, such as emission from clouds, the Kennicutt relation, the discrepancy between theoretical Milky Way star formation efficiency and observations, and the complexity of calculating SFR with proxy measurements, not just with the method used to tally source contributions to the global SFR used in this paper but also various other methods mentioned by the authors. This paper seems good for referencing methods and results in historical and recent literature.

[(Brinch, C., et. al, 200Y)](https://www.aanda.org/articles/aa/abs/2007/45/aa8249-07/aa8249-07.html) *A deeply embedded young protoplanetary disk around L1489 IRS observed by the Submillimeter Array**

In this paper, Brinch et. al observationally probe the L1489 IRS system's protostar to search for a Keplerian circumstellar disk. Written in 2007, this paper was one of the earlier proponents of pointing observational tools to low-mass protostars to check for circumstellar disks. They selected this protostar for observation based on the mass of the envelope seen. The authors observed the $HCO^+$ tracer using the Submillimeter Array at Mauna Kea, evidence of a collapsing envelope with an embedded Keplerian disk.      

This paper discusses a couple of relevant topics to our course and is a wonderful way of seeing how observations can lead to theoretical work to further prove the existence of theorized objects. The authors use SEDs and dust continuum observations to put together an image of the disk's shape, as well as find emission peaks for $HCO^+$. Their analysis of the spectra includes discussions of the wings of the emission and the resolution of their data relative to the scales they would expect to see disk structures at!

[(Ohashi, N., et. al, 2023)](https://iopscience.iop.org/article/10.3847/1538-4357/acd384) *Early Planet Formation in Embedded Disks (eDisk). I. Overview of the Program and First Results*

This is the introductory paper to the Early Planet Formation in Embedded Disks (eDisk) program. The goal of this paper is to act as a primer for the multiple papers published out of this survey by discussing the background motivations, the selected protostellar disks, the observations and data reduction, and some exciting novel results.

I used this paper as my first resource when writing for the midterm as it held relevance and recency for Class 0/I disks. I found that this was a good paper to broadly go through. It has discussions of the rotational velocities of disks, showing the importance of Keplerian velocities/rotation to prove that they researchers are looking at disks, and further for seeing the regions that tracers outline (within/outside of the disk region). It further discusses the way in which they selected their observational areas, which were star forming regions, and how they selected sources with available SEDs to grasp whether they were looking at Class 0 or Class I protostars.  
