import matplotlib.pyplot as plt
from datetime import datetime


values = [10, 15, 20, 10, 15]

# plt.hist(values) # cor padrao azul
plt.hist(values, color='b')
plt.title('titulo')
# plt.show()

now = datetime.now()
now_as_str = now.strftime("%Y%m%d%H%M%S")

new_file_name = f'../output/savegrafico_{now_as_str}.png'

# saving image
plt.savefig(new_file_name)

