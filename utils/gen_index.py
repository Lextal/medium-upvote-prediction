import numpy as np
import numpy.random as rnd
x = rnd.permutation(np.arange(1415065))
q = np.zeros(1415065)
train = x[:1200000]
test = x[1200000:]
q[test] = 1

with open('train_test_index', 'w') as f:
    s = ' '.join([str(int(x)) for x in q])
    f.write(s + '\n')
    f.close()
