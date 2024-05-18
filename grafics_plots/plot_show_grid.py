import matplotlib.pyplot as plt
import numpy as np


x = [1, 2, 3, 4, 5]
y = [1, 2, 4, 6, 16]

plt.plot(x, y, 'ro--', label='Estudantes')
plt.legend(loc='best')
plt.title('Titulo do grafico')
plt.xlabel('Eixo horizontal')
plt.ylabel('Eixo vertical')
# plt.grid(True) # ja mostra porem solida
# plt.grid(linestyle='-.') # mostra tracejada
plt.grid(which='major', linestyle='-', color='black')
plt.minorticks_on()
plt.grid(which='minor', linestyle='-.', color='gray', alpha=0.2)

plt.show()
