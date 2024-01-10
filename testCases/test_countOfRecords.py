import pandas as pd
import pyodbc

# Replace these variables with your actual connection details
server = "ABHIJITH_LAPTOP\SQLEXPRESS"
database = 'ACA_CRR_STG'
# username = 'abhij'  # You may need to provide a username even if there is no password

# Create a connection string without password
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database}'

sql_query ="SELECT * FROM ACA_CRR_STG..STG_DDA_1212"


with pyodbc.connect(connection_string) as connection:
    # Execute the query and load result into a DataFrame
    df = pd.read_sql(sql_query, connection)

# Now df contains the result of your SQL query
print(df)
assert True
