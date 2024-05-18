import xlsxwriter
import numpy as np
import matplotlib.pyplot as plt
import io
from datetime import datetime

x = np.linspace(-10, 10, 100)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)

now = datetime.now()
now_as_str = now.strftime("%Y%m%d%H%M%S")

new_file_name = f'../output/excel_with_plo_{now_as_str}.xlsx'

workbook = xlsxwriter.Workbook(new_file_name)
wks1=workbook.add_worksheet('Test chart')
wks1.write(0, 0,'test')

imgdata=io.BytesIO()
fig.savefig(imgdata, format='png')
wks1.insert_image(2, 2, '', {'image_data': imgdata})

workbook.close()
