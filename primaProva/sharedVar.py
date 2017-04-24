from theano import *
from theano import tensor as T

# Utilizzo di una variabile shared, condivisibile tra più funzioni. I suoi valori sono ottenibili tramite
# la funzione get_value() e modificabili tramite set_value().
#


state = shared(0)
inc = T.iscalar('inc')              #integer scalar
add = function([inc], state, updates=[(state, state+inc)])

print(state.get_value())

add(1)
print(state.get_value())

add(50)
print(state.get_value())

state.set_value(3)
print(state.get_value())

dec = T.iscalar('dec')
subtract = function([dec], state , updates=[(state,state-dec)])
subtract(24)

print(state.get_value())