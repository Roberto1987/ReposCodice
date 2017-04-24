from theano import *
from theano import tensor as T

state = shared(0)
inc = T.iscalar('inc')              #integer scalar
add = function([inc], state, updates=[(state, state+inc)] , on_unused_input='ignore')
add(1)
print('var state',state.get_value())
bool = True
addCopy = add.copy(delete_updates=bool)
addCopy(40)
print(state.get_value())

#copiamo ora add cambiando la sua variabile interna
new_state = shared(0)
secAddCopy = add.copy(swap={state:new_state})
secAddCopy(300)
print(state.get_value(),new_state.get_value())