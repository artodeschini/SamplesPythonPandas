import matplotlib.pyplot as plt


x_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_axis = [15, 12, 54, 49, 87, 75, 52, 14, 23, 1]


plt.title("Scatter plot")

# para adicionar uma label ao eixo x
plt.xlabel("Eixo X")

# para adicionar uma label ao eixo y
plt.ylabel("Eixo Y")

plt.scatter(x_axis, y_axis, color='r')

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
