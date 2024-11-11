import pandas as pd
import numpy as np
from sqlalchemy import create_engine

#reading the csv files
sales=pd.read_csv('data/Sales.csv',)
products=pd.read_csv('data/Products.csv')
customers=pd.read_csv('data/Customers.csv' ,encoding='ISO-8859-1')
stores=pd.read_csv('data/Stores.csv')
exchanges_rates=pd.read_csv('data/Exchange_Rates.csv')
def cleaning():
    print(sales.isnull().sum())
    print(products.isnull().sum())
    print(customers.isnull().sum())
    print(stores.isnull().sum())
    print(exchanges_rates.isnull().sum())
    sales.drop(columns=['Delivery Date'], inplace=True)
    customers.drop(columns=['State Code','Zip Code'], inplace=True)
    print(sales.dtypes)

    sales['Order Date'] = pd.to_datetime(sales['Order Date'], errors='coerce')

    customers['Birthday'] = pd.to_datetime(customers['Birthday'], errors='coerce')

    stores['Open Date'] = pd.to_datetime(stores['Open Date'], errors='coerce')
    stores['Square Meters'] = stores['Square Meters'].fillna(0)

    exchanges_rates['Date'] = pd.to_datetime(exchanges_rates['Date'], errors='coerce')
    exchanges_rates.rename(columns={'Currency': 'Currency Code'}, inplace=True)

    products['Unit Cost USD']=products['Unit Cost USD'].str.replace('$','').str.replace(',','')
    products['Unit Cost USD'] = pd.to_numeric(products['Unit Cost USD'], errors='coerce')
    products['Unit Price USD']=products['Unit Price USD'].str.replace('$','').str.replace(',','')
    products['Unit Price USD'] = pd.to_numeric(products['Unit Price USD'], errors='coerce')

    customers.info()
    sales.info()
    products.info()
    stores.info()
    exchanges_rates.info()

def main():
    cleaning()
    
    #joining tables based on common column
    final_df=sales
    final_df=pd.merge(final_df,customers,on='CustomerKey',how='inner')
    final_df=pd.merge(final_df,products,on='ProductKey',how='inner')
    final_df=pd.merge(final_df,stores,on='StoreKey',how='inner')
    final_df=pd.merge(final_df,exchanges_rates,left_on=['Currency Code','Order Date'],right_on=['Currency Code','Date'],how='inner')
    final_df.to_csv('final.csv', index=False)

    print(final_df.isnull().sum())

    engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/dataspark')
    customers.to_sql('customers', engine, if_exists='replace', index=False)
    sales.to_sql('sales', engine, if_exists='replace', index=False)
    products.to_sql('products', engine, if_exists='replace', index=False)
    stores.to_sql('stores', engine, if_exists='replace', index=False)
    exchanges_rates.to_sql('exchange_rates', engine, if_exists='replace', index=False)
    final_df.to_sql('final_df', engine, if_exists='replace',index=False)

    print("Data successfully uploaded to the SQL database")

if __name__ == '__main__':
    main()