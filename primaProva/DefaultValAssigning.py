import theano
import theano.tensor as T
from theano import In

a = T.dscalar('a')
b = T.dscalar('b')
rule = a+b
sum = theano.function([a,In(b,value=10)],rule)
print(sum(1))
print(sum(1,2))



