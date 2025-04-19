import pandas as pd
# from sqlalchemy import create_engine

# Load CSV file
file_path = r"C:\Users\HP\OneDrive\Documents\Hadisa's\Data Analyst Journey\Tata's Task\CSV Cleaned Online Retail Data Set.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1', dtype={'InvoiceNo': str})
# print(df.dtypes)

# print(df.isnull().values.any()) # if this returns true, means there are missing values in the dataset
# print(df.isnull().sum().sum()) # this tells the total number of empty cells
#print(df[df.isnull().any(axis=1)].shape[0]) # this tells how many rows have at least one missing value.

df.columns = df.columns.str.strip().str.replace(" ", "_") 
    # removes dataset's column names' trailing and leading white spaces and provides a "_" if there is space in a 
    # column's name, such as "Unit Price" will be converted into "Unit_Price"
 
#  Q U E S T I O N - 1

df_tata_q1 = df.dropna(subset = ['InvoiceDate', 'Quantity', 'UnitPrice'])
df_tata_q1['InvoiceDate'] = pd.to_datetime(df_tata_q1['InvoiceDate'], errors='coerce') # this converts the data type of InvoiceDate from Object to datetime datatype making it useful for preparing time based visuals
df_tata_q1['Revenue'] = df_tata_q1['Quantity'] * df_tata_q1['UnitPrice'] # this create a new column named revenue within Tata_q1.csv dataset
df_q1_2011 = df_tata_q1[df_tata_q1['InvoiceDate'].dt.year == 2011] # this makes a new dataframe for the year 2011 only
df_q1_monthly_revenue = df_q1_2011.groupby(df_q1_2011['InvoiceDate'].dt.to_period('M'))['Revenue'].sum().reset_index() # this calculates the monthly revenue for the year 2011 and then restores the index
df_q1_monthly_revenue['InvoiceDate'] = df_q1_monthly_revenue['InvoiceDate'].dt.to_timestamp() # for plotting time based data, visualization tools require data in timestamp format which is why its necessary
df_q1_monthly_revenue.to_csv("Tata_q1.csv", index = False)


#   Q U E S T I O N - 2

df_tata_q2 = df.dropna(subset = ['Country', 'Quantity', 'UnitPrice'])
df_tata_q2['Revenue'] = df_tata_q2['Quantity'] * df_tata_q2['UnitPrice']
country_stats_q2 = df_tata_q2.groupby('Country').agg({'Revenue' : 'sum', 'Quantity' : 'sum'}).reset_index()
country_stats_no_uk_q2 = country_stats_q2[country_stats_q2['Country'] != 'United Kingdom']
top_10_countries_q2 = country_stats_no_uk_q2.sort_values(by = 'Revenue', ascending = False).head(10)
top_10_countries_q2.to_csv("Tata_q2.csv", index = False)



#   Q U E S T I O N - 3

df_tata_q3 = df.dropna(subset = ['CustomerID', 'Quantity', 'UnitPrice'])
df_tata_q3['Revenue'] = df_tata_q3['Quantity'] * df_tata_q3['UnitPrice']
customer_stats_q3 = df_tata_q3.groupby('CustomerID').agg({'Revenue' : 'sum'}).reset_index()
top_10_customers_q3 = customer_stats_q3.sort_values('Revenue', ascending = False).head(10)
top_10_customers_q3.to_csv('Tata_q3.csv', index = False)



#   Q U E S T I O N - 4
df_tata_q4 = df.dropna(subset = ['Country', 'Quantity'])
top_demand = df_tata_q4.groupby('Country').agg({'Quantity' : 'sum'}).reset_index()
top_demand_without_uk = top_demand[top_demand['Country'] != 'United Kingdom']
top_demand_without_uk.to_csv("Tata_q4.csv", index = False)