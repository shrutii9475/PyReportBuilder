# import pandas as pd
# import mysql.connector

# # Connect to the MySQL database
# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='Shruti098%',
#     database='training_database'
# )
# cursor = conn.cursor()

# # Create a table (if it doesn't exist)
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS excel_data (
#     column1 TEXT,
#     column2 INTEGER,
#     column3 FLOAT
# )
# '''
# cursor.execute(create_table_query)

# # Sample DataFrame
# data = {
#     'column1': ['Value 1', 'Value 2', 'Value 3'],
#     'column2': [10, 20, 30],
#     'column3': [1.1, 2.2, 3.3]
# }
# df = pd.DataFrame(data)

# # Send the DataFrame to the MySQL database
# for _, row in df.iterrows():
#     values = tuple(row)
#     insert_query = '''
#     INSERT INTO excel_data (column1, column2, column3)
#     VALUES (%s, %s, %s)
#     '''
#     cursor.execute(insert_query, values)

# conn.commit()
# print("DataFrame data uploaded successfully!")

# # Close the database connection
# conn.close()

# +====================+++====================================
# import pandas as pd
# import mysql.connector

# # Connect to the MySQL database
# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='Shruti098%',
#     database='training_database'
# )
# cursor = conn.cursor()

# # Create a table (if it doesn't exist)
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS excel_data2 (
#     db_column1 TEXT,
#     db_column2 INTEGER,
#     db_column3 FLOAT
# )
# '''
# cursor.execute(create_table_query)

# # Map Excel column names to database column names
# column_mapping = {
#     'column1': 'db_column1',
#     'column2': 'db_column2',
#     'column3': 'db_column3'
# }

# # Read the Excel file into a DataFrame
# file_path = "try.xlsx"
# df = pd.read_excel(file_path)

# # Create a list of database column names
# db_columns = list(column_mapping.values())
# print (db_columns)

# # Filter the DataFrame to include only the mapped columns
# df_filtered = df[list(column_mapping.keys())]
# print(df_filtered)

# # Rename the DataFrame columns based on the mapping
# df_filtered.rename(columns=column_mapping, inplace=True)

# print (df)

# # Send the DataFrame to the MySQL database
# for _, row in df.iterrows():
#     values = tuple(row)
#     insert_query = '''
#     INSERT INTO excel_data2 (column1, column2, column3)
#     VALUES (%s, %s, %s)
#     '''
#     cursor.execute(insert_query, values)

# conn.commit()
# print("Excel data uploaded successfully!")

# # Close the database connection
# conn.close()

import pandas as pd
import mysql.connector

# Step 1: Install required packages:
# !pip install pandas mysql-connector-python

# Step 2: Import libraries

# Step 3: Read Excel file into a DataFrame
df = pd.read_excel('C:\CODE Files\REPORT GENERATOR\samenamedb.xlsx')

print (df.head(5))

# Step 4: Establish a connection to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Shruti098%',
    database='userdata'
)

# Step 5: Create a cursor object
cursor = conn.cursor()

# Step 6: Create table in the database (if needed)
create_table_query = '''
    CREATE TABLE IF NOT EXISTS sampledb (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    SNo VARCHAR(10),
    TrainingProgramName VARCHAR(255),
    TrainingProgramDate VARCHAR(10),
    Name VARCHAR(255),
    Designation VARCHAR(255),
    Gender VARCHAR(10),
    Email VARCHAR(255),
    MobileNumber VARCHAR(15),
    Organization VARCHAR(255),
    OfficeAddress VARCHAR(255),
    State VARCHAR(255),
    OrganizationSector VARCHAR(50),
    OrganizationCategorySMEorNonSME VARCHAR(10),
    OfficerBelongsToSCOrST VARCHAR(10),
    OfficerBelongsToPWD VARCHAR(10)
);
'''
cursor.execute(create_table_query)

# Step 7: insert query 
insert_query = ''' INSERT INTO sampledb (
    
    TrainingProgramName,
    TrainingProgramDate,
    Name,
    Designation,
    Gender,
    Email,
    MobileNumber,
    Organization,
    OfficeAddress,
    State,
    OrganizationSector,
    OrganizationCategorySMEorNonSME,
    OfficerBelongsToSCOrST,
    OfficerBelongsToPWD
) values (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
'''


# Iterate over the DataFrame rows and insert records into the database, all the columns are uploaded
# for index, row in df.iterrows():
#     record_data = []
#     for value in row:
#         if pd.isnull(value):
#             record_data.append(None)  # Convert NaN values to None (null)
#         else:
#             record_data.append(value)
        
#     # print('index = ',index)
#     # print('row = ',row)
#     # print('record_data = ',record_data)

#     cursor.execute(insert_query, record_data)  # Execute the query
#     conn.commit()  # Commit the changes for each record


# Iterate over the DataFrame rows and insert records into the database ( removing the sno in database)
for index, row in df.iterrows():
    record_data = []
    # for value in row:
    for column_name, value in row.items():
        if column_name != 'SNo':  # Skip the 'SNo' column
            if pd.isnull(value):
                record_data.append(None)  # Convert NaN values to None (null)
            else:
                record_data.append(value)
        
    # print('index = ',index)
    # print('row = ',row)
    # print('record_data = ',record_data)

    cursor.execute(insert_query, record_data)  # Execute the query
    conn.commit() 


# cursor.executemany(insert_query, values)



# Step 9: Commit changes and close cursor and connection
# conn.commit()
cursor.close()
conn.close()
