# bayesoverden

Modify "python main.py" to calculate Bayesian Overdensity.

The details are described in this paper: [Gu et al, 2021, ApJ, 921, 60](https://ui.adsabs.harvard.edu/abs/2021ApJ...921...60G/abstract).

input:  data format of "data.npy":  

1-2.  ra, dec: from COSMOS2020
3.    z: redshift from COSMOS2020, have been replaced by zbest from X-ray catalog 
4.    FARMER_ID:
5.    ID: from J_ApJ_817_34_catalog.dat.gz.fits, or -99.0

output: data format of "BayeskNN_overden.npy":

1-10. BayeskNN_overden: log(1+δ'_k), k = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

How to read '*.npy'? Use python "numpy.load" 

Example: 

	import numpy as np
	data = np.load('BayeskNN_overden.npy')
	print(data.shape)  
	overbayes10NN = data[:,9] 
