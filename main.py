import numpy as np 
from utilsbo import localden
dat1 = np.load('./data.npy'); print( np.shape(dat1) ) 

ra            = dat1[:,0].astype('float32')
dec           = dat1[:,1].astype('float32')
redshift      = dat1[:,2].astype('float32')

igal = None; 
# igal = np.arange(100) # For test, can calculate the first 100 sources if want to test. 
kdd, overBayeskNN, overNeighkNN = localden.overden(ra, dec, redshift, dz = 0.04*(1+redshift), skycov = 1.5*3600, igal = igal)
np.save('overden_BayeskNN.npy', overBayeskNN) 
