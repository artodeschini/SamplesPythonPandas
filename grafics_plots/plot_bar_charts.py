import matplotlib.pyplot as plt


values = [10, 15, 20]
scale = [0.5, 1, 2]

# plt.hist(values) # cor padrao azul
# plt.bar(values, scale, color='r') #, color='b')
plt.bar(values, scale, width=2, color='r') # with aumenta largura da barra
plt.title("um titulo para o grafico")
plt.show()
