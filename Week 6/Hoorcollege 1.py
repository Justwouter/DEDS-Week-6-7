
import pandas as pd
import pyodbc

sales_conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Coding\SE2\DEDS\Python\GO-databases DEDS-week 4 & 5\go_sales.accdb;')

product = pd.read_sql("SELECT * FROM product", sales_conn)
product

product.loc[:, ['PRODUCT_NAME', 'DESCRIPTION']]

product.dtypes

product['PRODUCTION_COST'] = product['PRODUCTION_COST'].astype(float)
product['MARGIN'] = product['MARGIN'].astype(float)

product.dtypes

product.loc[:, ['LANGUAGE']].drop_duplicates('LANGUAGE')

product.loc[:, ['PRODUCT_NAME', 'LANGUAGE']].drop_duplicates(['PRODUCT_NAME', 'LANGUAGE'])

product.drop('LANGUAGE', axis = 1)

product

product = product.drop('LANGUAGE', axis = 1)
product

product.sort_values('PRODUCTION_COST', ascending = False)

product.sort_values(['PRODUCTION_COST', 'MARGIN'], ascending = [False, True])

product.loc[product['PRODUCTION_COST'] > 350, :]


product.loc[product['PRODUCT_NUMBER'].isna(), :]

product.loc[product['PRODUCT_NAME'].str[0] == 'B', :]

product.loc[product['PRODUCT_NAME'].str[-1] == 'n', :]

product.loc[product['PRODUCT_NAME'].str.contains('e'), :]

product.loc[(product['PRODUCT_NAME'].str[0] == 'B') | (product['PRODUCT_NAME'].str[-1] == 's'), :]

product.shape[0]

product['PRODUCTION_COST'].sum()

round(product['PRODUCTION_COST'].mean(), 2)

product['PRODUCTION_COST'].min()

product['PRODUCTION_COST'].max()

grouped = product.groupby('PRODUCT_TYPE_CODE')['PRODUCTION_COST'].mean().reset_index()
grouped = grouped.rename(columns = {'PRODUCTION_COST' : 'AVG_PRODUCTION_COST'})

grouped

grouped.loc[grouped['AVG_PRODUCTION_COST'] < 100, :]

order_details = pd.read_sql("SELECT * FROM order_details", sales_conn)
order_details

joined = pd.merge(product, order_details, on = 'PRODUCT_NUMBER', how = 'inner')
joined

product.loc[product['PRODUCTION_COST'] == product['PRODUCTION_COST'].min(), :]

product1 = product.iloc[:80]
product2 = product.iloc[80:]
product1

product = product1.append(product2)
product

for index, row in product.iterrows():
    production_cost = product.at[index, 'PRODUCTION_COST']
    
    if(production_cost < 100):
        product.at[index, 'MARGIN_RANKING'] = 'cheap'
    elif(production_cost < 200):
        product.at[index, 'MARGIN_RANKING'] = 'a bit expensive'
    else:
        product.at[index, 'MARGIN_RANKING'] = 'very expensive'

product