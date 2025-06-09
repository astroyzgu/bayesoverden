## bayesoverden

Modify "python main.py" to calculate Bayesian Overdensity. The data format of input and output catalog can be seen as follow. 

The details are described in this paper: [Gu et al, 2021, ApJ, 921, 60](https://ui.adsabs.harvard.edu/abs/2021ApJ...921...60G/abstract).

#### Data format 

input:  data format of "data.npy":  

1-2.  ra, dec
3.    z
4.    ID

output: data format of "BayeskNN_overden.npy":

1-10. BayeskNN_overden: log(1+δ'_k), k = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#### How to read '*.npy'? Use python "numpy.load" 

Example: 

	import numpy as np
	data = np.load('BayeskNN_overden.npy')
	print(data.shape)  
	overbayes10NN = data[:,9] 
