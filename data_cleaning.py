import pandas as pd
import numpy as np

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

def main():
    cleaning()
    sales.drop(columns=['Delivery Date'], inplace=True)
    customers.drop(columns=['State Code','Zip Code'], inplace=True)
    print(sales.dtypes)

    sales['Order Date'] = pd.to_datetime(sales['Order Date'], infer_datetime_format=True, errors='coerce')
    customers['Birthday']=pd.to_datetime(customers['Birthday'],infer_datetime_format=True,errors='coerce')
    stores['Open Date']=pd.to_datetime(stores['Open Date'],infer_datetime_format=True,errors='coerce')
    exchanges_rates['Date']=pd.to_datetime(exchanges_rates['Date'],infer_datetime_format=True,errors='coerce')
    products['Unit Cost USD']=products['Unit Cost USD'].str.replace('$','').str.replace(',','')
    products['Unit Cost USD'] = pd.to_numeric(products['Unit Cost USD'], errors='coerce')
    products['Unit Price USD']=products['Unit Price USD'].str.replace('$','').str.replace(',','')
    products['Unit Price USD'] = pd.to_numeric(products['Unit Price USD'], errors='coerce')
    stores.fillna(0)
    print(products)

    customers.info()
    sales.info()
    products.info()
    stores.info()
    exchanges_rates.info()
    
    



if __name__ == '__main__':
    main()