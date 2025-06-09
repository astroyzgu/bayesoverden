## bayesoverden

Modify `python main.py` to compute **Bayesian Overdensity** following the methodology from [Gu et al. 2021](https://ui.adsabs.harvard.edu/abs/2021ApJ...921...60G/abstract).   

 The data format of input and output catalog can be seen as follow. 

The details are described in this paper: [Gu et al, 2021, ApJ, 921, 60](https://ui.adsabs.harvard.edu/abs/2021ApJ...921...60G/abstract).

### Input/Output Specifications  

#### Input Catalog Format "data.npy"
- **File Format**: npy (n,3)
- **Required Columns**:  
  `RA` (Right Ascension), `Dec` (Declination), `z` (Redshift) 
#### Output Catalog Format "BayeskNN_overden.npy"
- **File Format**: npy (n,10)
- **Required Columns**:  
   1-10. BayeskNN_overden: log(1+δ'_k), k = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

##### How to read '*.npy'? Use python "numpy.load" 

Example: 

	import numpy as np
 	z   = np.random.uniform(  0,0.1,1000)
  	ra  = np.random.uniform(100,150,1000)
     	dec = np.random.uniform(100,150,1000)
      	np.save('data.npy', np.array([ra, dec, z]).T) 
	data = np.load('BayeskNN_overden.npy')
	print(data.shape)  
	overbayes10NN = data[:,9] 
