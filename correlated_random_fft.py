#correlated_random_fft.py
import numpy
from matplotlib import pyplot as plt

nn=401; # # of data points
#now just make the first row of covariance matrix
cov=numpy.zeros(nn)
i=0
for j in range(0,nn):
    cov[j]=1./(50+numpy.abs(i-j))
#but since correlation has to be symmetric left-right, need to 
#make sure negative indices are same as positive:
cov[1:]=cov[1:]+numpy.flipud(cov[1:])

covft=numpy.real(numpy.fft.fft(cov))
covft[covft<0]=0.0
covft=numpy.sqrt(covft)

xft=numpy.random.randn(nn)+numpy.complex(0,1)*numpy.random.randn(nn)
xft[1:]=xft[1:]+numpy.conj(numpy.flipud(xft[1:]))
xft[0]=numpy.real(xft[0]) #explicitly make offset real
xft=xft*covft


noisy_dat=numpy.fft.ifft(xft)
noisy_dat=numpy.real(noisy_dat)
plt.ion()
plt.clf()
plt.plot(noisy_dat)
plt.show()

#plt.savefig('corrdata_matrix.png')
