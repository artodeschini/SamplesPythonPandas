import matplotlib.pyplot as plt


values = [20, 20, 35, 25]

# plt.pie(values) # so o brafico
# plt.pie(values, labels=['A', 'B', 'C', 'D']) # com legendas para cada fatia
# plt.pie(values, labels=['A', 'B', 'C', 'D'], explode=[0, 0.2, 0, 0]) # explode mostra separados no caso 0 nao separa
plt.pie(values, labels=['A', 'B', 'C', 'D'], explode=[0, 0.2, 0, 0], colors=['r', 'g', 'b', 'y']) # define as cores
plt.show()
