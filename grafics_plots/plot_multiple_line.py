import matplotlib.pyplot as plt


x1 = [1, 2, 3, 24]
y1 = [1, 2, 3, 4]

x2 = [5, 10, 20, 22]
y2 = [1, 7, 9, 13]

x3 = [3, 9, 12, 15, 21]
y3 = [1, 4, 6, 7, 8]

plt.plot(x1, y1, 'r') # linha vermelha
plt.plot(x2, y2, 'b') # linha azul
plt.plot(x3, y3, 'g') # linha azul
# plt.interactive()

# para adicionar um titulo ao grafico
plt.title("Primeiro Grafico uma Reta Crescente")

# para adicionar uma label ao eixo x
plt.xlabel("Eixo X")

# para adicionar uma label ao eixo y
plt.ylabel("Eixo Y")

# adiciona uma legenda com as cores correspondentes
plt.legend(['Primeiro', 'Segundo', 'Terceiro'])

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
