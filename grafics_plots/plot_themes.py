import matplotlib.pyplot as plt


values = [10, 15, 20]
scale = [0.5, 1, 2]

print(plt.style.available)
plt.style.use('ggplot')

# plt.hist(values) # cor padrao azul
# plt.bar(values, scale, color='r') #, color='b')
plt.bar(values, scale) # with aumenta largura da barra
plt.title("um titulo para o grafico")
plt.show()
