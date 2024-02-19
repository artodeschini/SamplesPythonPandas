import pandas as pd
from datetime import datetime


df = pd.read_csv('ventas.csv', sep=';') # sep casa o delimitador seja diferente o padrao é ','
df.fillna(0, inplace=True)

# adicionar coluna resultado de quantidade e preco unitario
df['Ingrecos'] = df['Cantidad'] * df['Precio_Unitario']
print(df)

ingresso_loja_produto = df.groupby(['Tienda', 'Producto'])['Ingrecos'].sum().reset_index()
print(ingresso_loja_produto)

produto_top_por_loja = ingresso_loja_produto.sort_values(['Tienda', 'Ingrecos'], ascending=[True, False]).groupby(['Tienda']).first().reset_index()
print(produto_top_por_loja)

resumo_qtde = df.groupby('Producto')['Cantidad'].sum().reset_index()
print(resumo_qtde)

now = datetime.now()
now_as_str = now.strftime("%Y%m%d%H%M%S")

new_file_name = f'output/generate_resumo_vendas_{now_as_str}.csv'

resumo_qtde.to_csv(new_file_name, index=False)
