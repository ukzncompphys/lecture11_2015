#correlated_random.py
import numpy
from matplotlib import pyplot as plt

nn=200; # # of data points
cov=numpy.zeros([nn,nn])
for i in range(0,nn):
    for j in range(0,nn):
        #make up a covariance function
        cov[i,j]=1./(50+numpy.abs(i-j))
plt.ion()
plt.clf()
plt.plot(cov[nn/2,:])
plt.savefig('cov_slice.png')
#Take eigenvalues/eigenvectors
lam,v=numpy.linalg.eig(cov)
#make random data with noise from eigenvalues.
#rotate back with eigenvectors
x=numpy.sqrt(lam)*numpy.random.randn(nn)
y=v.dot(x)
plt.clf()
plt.plot(y)
plt.savefig('corrdata_matrix.png')
