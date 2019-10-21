def fibo(n):
    a = 1
    b = 1
    yield a
    for i in range(n):
        a, b = a + b, a
        yield b

import math
def primer_digito(n):
    return int(n / 10 ** int(math.log(n)/math.log(10)))

digitos = [0,0,0,0,0,0,0,0,0]
for i in fibo(10000):
    digitos[primer_digito(i)-1]+=1

import matplotlib.pyplot as plt
%matplotlib inline

#plt.xscale("log")
#plt.yscale("log")
plt.plot(range(1,10), digitos)
