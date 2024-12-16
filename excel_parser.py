import sys
import datetime
import pandas 
from sqlalchemy import create_engine
from logging_config import set_init_log
from excel_validate import chkData

# 로그 설정
log_file = "excel_parse_" + str(datetime.date.today()) + ".log"
logger = set_init_log(log_name="excel_parser", file_name=log_file, lv=0)
logger.debug(f"/*------------------------[ExcelParser] Start : {str(datetime.datetime.now())}------------------------*/")

# valid 처리
valid = {"flag" : True, "msg" : ''}

def write_log(): # valid_flag에 따라 debug or error로 기록
    if valid['flag']: 
        logger.debug(valid['msg'])
    else:
        logger.error(valid['msg'])

# 1. excel_file
##############################################################################

try:
    #"""
    table_name = sys.argv[0] # 테이블 명
    excel_file = sys.argv[1] # 파일 경로
    first_rows = sys.argv[2] # 읽어들일 시작 row
    col_ranges = sys.argv[3] # 읽어들일 column 범위
    col_header = sys.argv[4] # 헤더 row
    #"""
    # TEST-VARIANT
    """
    table_name = "orders"
    excel_file = "C:/Users/jinwoong/IdeaProjects/sixtdev/python_modules/excel_parse/__excel/40d50fe2-520d-4b26-977c-455f9d0be1a4.xlsx" # 파일 경로
    first_rows = "2" # 읽어들일 시작 row
    col_ranges = "B:I" # 읽어들일 column 범위
    col_header = "0" # 헤더 row
    """
    
    df = pandas.read_excel(excel_file,skiprows=int(first_rows),usecols=col_ranges,header=int(col_header) )
    valid['msg'] = (f'[STEP-1] EXCEL_LOAD : file={excel_file}, skiprows={first_rows}, usecols={col_ranges}, headerrow={col_header}') 

except Exception as e:
    valid['msg'] = '[STEP-1] EXCEL_LOAD : FAIL'
    valid['flag'] = False
finally:
    write_log()

##############################################################################


# 2. database connect
##############################################################################
if valid['flag'] :
    try:
        db_connection_str = 'mysql+pymysql://mkprocs:mkprocs1234%21%40@localhost:3306/mkprocsDB'
        engine = create_engine(db_connection_str)
        valid['msg'] = f'[STEP-2] DB Connect : {db_connection_str}'
    except Exception as e:
        valid['msg'] = '[STEP-2] DB Connect : FAIL'
        valid['flag'] = False
    finally:
        write_log()

##############################################################################


# 3. validation
##############################################################################
if valid['flag'] :
    try:
        valid = chkData(table_name, df)
    except Exception as e:
        valid['msg'] = '[STEP-3] VALIDATION : FAIL'
        valid['flag'] = False
    finally:
        write_log()

##############################################################################


# 4. database insert
##############################################################################

if valid['flag']:
    try:
        # df.to_sql(table_name, con=engine, if_exists='append', index=False)
        valid['msg'] = (f'[STEP-4] INSERT : {len(df)} rows inserted into the table [{table_name}].')
    except Exception as e:
        valid['msg'] = '[STEP-4] INSERT : FAIL'
        valid['flag'] = False
    finally:
        write_log()

##############################################################################


# 5. database update
##############################################################################

try:
    if valid['flag']:
        # 상태 변경 
        valid['msg'] = '[STEP-5] EXCELPARSE : SUCCESS'
    else:
        # 상태 변경 
        valid['msg'] = '[STEP-5] EXCELPARSE : FAIL'
except Exception as e:
    valid['msg'] = '[STEP-5] UPDATE : FAIL'
finally:
    write_log()

##############################################################################

logger.debug(f"/*------------------------[ExcelParser] E n d : {str(datetime.datetime.now())}------------------------*/")
sys.exit(1)
