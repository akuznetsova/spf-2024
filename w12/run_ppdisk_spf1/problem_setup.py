#
# Import NumPy for array handling
#
import numpy as np
#
# Some natural constants
#
au  = 1.49598e13     # Astronomical Unit       [cm]
pc  = 3.08572e18     # Parsec                  [cm]
ms  = 1.98892e33     # Solar mass              [g]
ts  = 5.78e3         # Solar temperature       [K]
ls  = 3.8525e33      # Solar luminosity        [erg/s]
rs  = 6.96e10        # Solar radius            [cm]
#
# Monte Carlo parameters
#
nphot    = 1000000
#
# Grid parameters
#
nr       = 64
ntheta   = 32
nphi     = 1
rin      = 1*au
rout     = 100*au
thetaup  = np.pi*0.5 - 0.7e0
#
# Disk parameters
#
sigmag0  = 1973.0 # Sigma gas at 1 AU
sigmad0  = sigmag0 * 0.01    # Sigma dust at 1 AU
fracbig  = 0.99              # Fraction of dust that is the big grain dust
plsig    = -1.0e0            # Powerlaw of the surface density
hr0      = 0.04              # H_p/r at 1 AU
plh      = 0.25               # Powerlaw of flaring
hrbigsett= 0.02              # The big grains are settled a bit more than the small grains
rd 	 = 90.0*au 	     # disk size 
#
# Star parameters
#
mstar    = ms
rstar    = rs*2.0
tstar    = 4000.0
pstar    = np.array([0.,0.,0.])
#
# Make the coordinates
#
ri       = np.logspace(np.log10(rin),np.log10(rout),nr+1)
thetai   = np.linspace(thetaup,0.5e0*np.pi,ntheta+1)
phii     = np.linspace(0.e0,np.pi*2.e0,nphi+1)
rc       = 0.5 * ( ri[0:nr] + ri[1:nr+1] )
thetac   = 0.5 * ( thetai[0:ntheta] + thetai[1:ntheta+1] )
phic     = 0.5 * ( phii[0:nphi] + phii[1:nphi+1] )
#
# Make the grid
#
qq       = np.meshgrid(rc,thetac,phic,indexing='ij')
rr       = qq[0]
tt       = qq[1]
zr       = np.pi/2.e0 - qq[1]
#
# Make the dust density model
#
sigmad   = sigmad0 * (rr/au)**plsig * np.exp(-rr/rd)
sigmadsm = sigmad*(1.-fracbig)
sigmadbg = sigmad*fracbig
hhrsm    = hr0 * (rr/au)**plh
hhrbg    = hrbigsett * (rr/au)**plh
hhsm     = hhrsm * rr
hhbg     = hhrbg * rr
rhodsm   = ( sigmadsm / (np.sqrt(2.e0*np.pi)*hhsm) ) * np.exp(-(zr**2/hhrsm**2)/2.e0)
rhodbg   = ( sigmadbg / (np.sqrt(2.e0*np.pi)*hhbg) ) * np.exp(-(zr**2/hhrbg**2)/2.e0)
#
# Write the wavelength_micron.inp file
#
lam1     = 0.1e0
lam2     = 7.0e0
lam3     = 25.e0
lam4     = 1.0e4
n12      = 20
n23      = 100
n34      = 30
lam12    = np.logspace(np.log10(lam1),np.log10(lam2),n12,endpoint=False)
lam23    = np.logspace(np.log10(lam2),np.log10(lam3),n23,endpoint=False)
lam34    = np.logspace(np.log10(lam3),np.log10(lam4),n34,endpoint=True)
lam      = np.concatenate([lam12,lam23,lam34])
nlam     = lam.size
#
# Write the wavelength file
#
with open('wavelength_micron.inp','w+') as f:
    f.write('%d\n'%(nlam))
    np.savetxt(f,lam.T,fmt=['%13.6e'])
#
#
# Write the stars.inp file
#
with open('stars.inp','w+') as f:
    f.write('2\n')
    f.write('1 %d\n\n'%(nlam))
    f.write('%13.6e %13.6e %13.6e %13.6e %13.6e\n\n'%(rstar,mstar,pstar[0],pstar[1],pstar[2]))
    np.savetxt(f,lam.T,fmt=['%13.6e'])
    f.write('\n%13.6e\n'%(-tstar))
#
# Write the grid file
#
with open('amr_grid.inp','w+') as f:
    f.write('1\n')                       # iformat
    f.write('0\n')                       # AMR grid style  (0=regular grid, no AMR)
    f.write('100\n')                     # Coordinate system: spherical
    f.write('0\n')                       # gridinfo
    f.write('1 1 0\n')                   # Include r,theta coordinates
    f.write('%d %d %d\n'%(nr,ntheta,1))  # Size of grid
    np.savetxt(f,ri.T,fmt=['%21.14e'])    # R coordinates (cell walls)
    np.savetxt(f,thetai.T,fmt=['%21.14e'])# Theta coordinates (cell walls)
    np.savetxt(f,phii.T,fmt=['%21.14e'])  # Phi coordinates (cell walls)
#
# Write the density file
#
with open('dust_density.inp','w+') as f:
    f.write('1\n')                       # Format number
    f.write('%d\n'%(nr*ntheta*nphi))     # Nr of cells
    f.write('2\n')                       # Nr of dust species
    data = rhodsm.ravel(order='F')         # Create a 1-D view, fortran-style indexing
    np.savetxt(f,data.T,fmt=['%13.6e'])  # The data
    data = rhodbg.ravel(order='F')         # Create a 1-D view, fortran-style indexing
    np.savetxt(f,data.T,fmt=['%13.6e'])  # The data
#
# Dust opacity control file
#
with open('dustopac.inp','w+') as f:
    f.write('2               Format number of this file\n')
    f.write('2               Nr of dust species\n')
    f.write('============================================================================\n')
    f.write('1               Way in which this dust species is read\n')
    f.write('0               0=Thermal grain\n')
    f.write('0.1_micron      Extension of name of dustkappa_***.inp file\n')
    f.write('----------------------------------------------------------------------------\n')
    f.write('1               Way in which this dust species is read\n')
    f.write('0               0=Thermal grain\n')
    f.write('100_micron      Extension of name of dustkappa_***.inp file\n')
    f.write('----------------------------------------------------------------------------\n')
#
# Write the radmc3d.inp control file
#
with open('radmc3d.inp','w+') as f:
    f.write('nphot = %d\n'%(nphot))
    f.write('scattering_mode_max = 1\n')
    f.write('iranfreqmode = 1\n')

