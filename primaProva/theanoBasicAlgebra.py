from theano import *
import theano.tensor as T
a = theano.tensor.vector();
z = a**2;
f = theano.function([a],z)
out = f([1,2,3,4,5])
print(out)
