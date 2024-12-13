import sys
import pandas 
from sqlalchemy import create_engine

# 1. excel_file
##############################################################################

excel_file = sys.argv[0] # 파일 경로
first_rows = sys.argv[1] # 읽어들일 시작 row
col_ranges = sys.argv[2] # 읽어들일 column 범위
col_header = sys.argv[3] # 헤더 row

df = pandas.read_excel( excel_file , skiprows = first_rows , usecols = col_ranges , header = col_header )

##############################################################################


# 2. database connect
##############################################################################

db_connection_str = 'mysql+pymysql://mkprocs:mkprocs1234%21%40@localhost:3306/mkprocsDB'
engine = create_engine(db_connection_str)

table_name = 'orders'

##############################################################################


# 3. validation
##############################################################################



##############################################################################


# 4. database insert
##############################################################################

# df.to_sql(table_name, con=engine, if_exists='append', index=False)

##############################################################################

# print(f'{len(df)} rows inserted into the table {table_name} successfully.')