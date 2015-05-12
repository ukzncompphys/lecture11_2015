#fft_inverse.py
from scipy.linalg import toeplitz
from  numpy.fft import fft,ifft
from numpy import flipud
import numpy
#make a circulant correlation function
x=1./numpy.arange(1,5);x[1:]=x[1:]+flipud(x[1:])
mat=toeplitz(x)
xinv=numpy.real(ifft(1/fft(x)))
matinv=toeplitz(xinv)
print mat
print mat.dot(matinv)
