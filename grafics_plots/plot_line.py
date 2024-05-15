import matplotlib.pyplot as plt


x_axis = [1, 2, 3, 4]
y_axis = [1, 2, 3, 4]

# plt.plot(x_axis, y_axis) linha preta
# plt.plot(x_axis, y_axis, 'r') # linha vermelha
plt.plot(x_axis, y_axis, 'r') # linha vermelha
# plt.interactive()

# para adicionar um titulo ao grafico
plt.title("Primeiro Grafico uma Reta Crescente")

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
