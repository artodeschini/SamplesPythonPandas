import matplotlib.pyplot as plt


values = [10, 15, 20]
scale = [0.5, 1, 2]

# é identico ao outro mas usa um a h no final
plt.barh(values, scale, color='r') # with aumenta largura da barra
plt.title("um titulo para o grafico")
plt.show()
