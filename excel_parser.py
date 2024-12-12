import pandas 
from sqlalchemy import create_engine

# 1. excel_file
##############################################################################

excel_file = './__excel/test_1.xlsx'
df = pandas.read_excel(excel_file           # 파일 경로
                     , skiprows=1           # 읽어들일 row
                     , usecols='B:I'        # 읽어들일 column 범위
                     , header=1)            # 헤더 row

##############################################################################


# 2. database connect
##############################################################################

db_connection_str = 'mysql+pymysql://mkprocs:mkprocs1234%21%40@localhost:3306/mkprocsDB'
engine = create_engine(db_connection_str)

table_name = 'orders'

##############################################################################

# 3. database insert
##############################################################################

df.to_sql(table_name, con=engine, if_exists='append', index=False)

##############################################################################

print(f'{len(df)} rows inserted into the table {table_name} successfully.')