'''
tools for Bayesian overdensity (BO)

Written by Gu Yizhou
'''

import numpy as np 
from astropy.coordinates import SkyCoord
from astropy.coordinates import match_coordinates_sky
from scipy.spatial import cKDTree, KDTree
from sklearn.neighbors import BallTree 
class localden(object): 
    def __init__(self): 
        pass
    
    @classmethod
    def NeighkNN_factor(cls, kk): 
        NeighkNN_factor = np.array([4.45, 1.82, 1.14, 0.83, 0.65, 0.65, 0.45, 0.39, 0.34, 0.31])
        return NeighkNN_factor[kk-1]
    
    @classmethod
    def BayeskNN_factor(cls, kk):
        BayeskNN_factor = np.array([4.45, 1.25, 0.59, 0.34, 0.22, 0.16, 0.12, 0.09, 0.07, 0.06])
        return BayeskNN_factor[kk-1]
    
    @classmethod
    def Nth_distance(cls, ra1, dec1, ra2, dec2, nmax_neighbor = 10): 
        obj1  = SkyCoord( ra1,  dec1,  unit='deg')
        obj2  = SkyCoord( ra2,  dec2,  unit='deg')
        distances = []; indx = []
        for k in range(1, nmax_neighbor + 1):
            idx,  sep2d, sep3d = match_coordinates_sky(obj1, obj2, nthneighbor= k );
            distances.append(sep2d[0].arcmin)
            indx.append(idx)
        distances = np.array(distances).T
        indx      = np.array( indx ).T
        return distances, indx

    @classmethod
    def overden(cls, ra, dec, z, dz, skycov, kNN = 10, igal = None):
        ngal = len(ra)
        if igal is None: 
            igal = np.arange(ngal)
        else: 
            igal = np.arange(ngal)[igal]
        kdd  = np.zeros((ngal, kNN)) + np.nan  
        sigma_surface = np.zeros(ngal)  

        try:
            import tqdm
            igal = tqdm.tqdm(igal)
        finally: 
            pass
        for igal_ in igal: 
            a0 = ra[igal_]; d0 = dec[igal_]
            z0 = z[igal_]; dz0 = dz[igal_] 
            indx = (z > z0 - dz0)&(z < z0 + dz0)
            a1 = ra[indx]; d1 = dec[indx]
            sep, idx = localden.Nth_distance(a0, d0, a1, d1, nmax_neighbor = 11)
            sep = sep[1:] # arcmin^2
            sigma_surface[igal_] = 1.0*len(a1)
            # print(1.0*len(a1)) 
            kdd[igal_, :len(sep)] = sep

        sigma_surface = sigma_surface/skycov
        data     = kdd**2
        NeighkNN = 1.0/data
                     
        for ii in range(1, data.shape[1]): data[:, ii] = data[:, ii-1] + data[:, ii] 
        BayeskNN = 1.0/data
        #--------- overdensity 
        for kk in range(kNN): 
            factor  = localden.BayeskNN_factor(kk+1)
            BayeskNN[:,kk] = BayeskNN[:, kk]/(sigma_surface[:]*factor)
        
            factor  = localden.NeighkNN_factor(kk+1)
            NeighkNN[:,kk] = NeighkNN[:, kk]/(sigma_surface[:]*factor)
        return kdd, np.log10(BayeskNN), np.log10(NeighkNN)  

