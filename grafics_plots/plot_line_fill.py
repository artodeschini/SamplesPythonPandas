import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10)
y = 0.05 * x * x


plt.ylim(0, 5)
plt.plot(x, y)
plt.fill_between(x, y, color='b', alpha=1)
# plt.interactive()

# para adicionar um titulo ao grafico
plt.title("Exemplo preenchendo a area  grafico")

# para adicionar uma label ao eixo x
plt.xlabel("Eixo X")

# para adicionar uma label ao eixo y
plt.ylabel("Eixo Y")

# faz mostrar o grafico
plt.show()

# simple cores para mais info sobre colre https://matplotlib.org/stable/users/explain/colors/
# 'b' as blue
# 'g' as green
# 'r' as red
# 'c' as cyan
# 'm' as magenta
# 'y' as yellow
# 'k' as black
# 'w' as white
