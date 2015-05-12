#fft_inverse.py
from scipy.linalg import toeplitz
from  numpy.fft import fft,ifft
from numpy import flipud,arange,exp
import numpy
import matplotlib.pyplot as plt
x=arange(200);y=exp(-0.5*x**2/8**2)
#make correlation matrix.  add a bit of noise
mat=toeplitz(y)+0.01*numpy.eye(x.size)
plt.ion()
plt.clf()
plt.imshow(mat)
plt.show();plt.savefig('kriging_mat.png')

#take eigenvalues.  Should be real, so force numpy 
e,v=numpy.linalg.eig(mat)
e=numpy.real(e);v=numpy.real(v)
x=v.dot(numpy.sqrt(e)*numpy.random.randn(e.size))

#do kriging estimate
mat_inv=numpy.linalg.inv(mat)
x_pred=-numpy.dot(mat_inv[0,1:],x[1:])/mat_inv[0,0]
plt.clf()
plt.plot(x)
plt.plot(0,x_pred,'r*')
plt.show();plt.savefig('kriging_output.png')
print (x[0]-x_pred)/numpy.std(x)



