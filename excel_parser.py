
# 1. setup
##############################################################################
import sys
import datetime
from logging_config import set_init_log

# 전역변수
global logger, valid, df
logger = None
valid = {"flag" : True, "msg" : ''}
df = None

def write_log(): # valid_flag에 따라 debug or error로 기록
    global logger, valid
    if logger != None:
        if valid['flag']: 
            logger.debug(valid['msg'])
        else:
            logger.error(valid['msg'])

try: # logger 생성
    log_file = f"excel_parse_{str(datetime.date.today())}.log"
    logger = set_init_log(log_name="excel_parser", file_name=log_file, lv=0)
    logger.debug(f"/*------------------------[ExcelParser] Start : {str(datetime.datetime.now())}------------------------*/")

except Exception as e: # logger 생성 실패 시
    valid['flag'] = False
    print('logger setup failed.')

##############################################################################


# 2. excel_file find
##############################################################################

if logger != None: # logger 생성 성공 시에만 실행
    import pandas 

    try: 
        # 파라미터 변수 매핑
        """
        table_name = sys.argv[0] # 테이블 명
        excel_file = sys.argv[1] # 파일 경로
        first_rows = sys.argv[2] # 읽어들일 시작 row
        col_ranges = sys.argv[3] # 읽어들일 column 범위
        col_header = sys.argv[4] # 헤더 row
        """
        # TEST-VARIANT
        #"""
        table_name = "orders"
        excel_file = "C:/Users/jinwoong/IdeaProjects/sixtdev/python_modules/excel_parse/__excel/40d50fe2-520d-4b26-977c-455f9d0be1a4.xlsx" # 파일 경로
        first_rows = "2" # 읽어들일 시작 row
        col_ranges = "C:I" # 읽어들일 column 범위
        col_header = "0" # 헤더 row
        #"""
        
        # excel parsing
        df = pandas.read_excel(excel_file,skiprows=int(first_rows),usecols=col_ranges,header=int(col_header) )
        valid['msg'] = f'[STEP-1] EXCEL_LOAD : file={excel_file}, skiprows={first_rows}, usecols={col_ranges}, headerrow={col_header}'

    except IndexError | ValueError as ve: # sys.args 매핑 오류 시
        valid['flag'] = False
        valid['msg'] = f'[STEP-1] VARIANT_MAPPING : FAIL - {ve}'

    except Exception as e: # exception 발생 시
        valid['flag'] = False
        valid['msg'] = f'[STEP-1] EXCEL_LOAD : FAIL - {e}'

    finally:
        write_log()

##############################################################################


# 2. database connect
##############################################################################
if valid['flag']:
    from sqlalchemy import create_engine

    try: # DB Connection
        db_connection_str = 'postgresql://mkprocs:mkprocs1234%21%40@localhost:5432/mkprocsDB'
        engine = create_engine(db_connection_str)
        valid['msg'] = f'[STEP-2] DB Connect : {db_connection_str}'

    except Exception as e: # DB Connection 실패 시
        valid['msg'] = f'[STEP-2] DB Connect : FAIL - {e}'
        valid['flag'] = False

    finally:
        write_log()

##############################################################################


# 3. validation
##############################################################################

if valid['flag'] :
    from excel_validate import chkData

    try: # data validation
        valid = chkData(table_name, df, logger)
    
    except Exception as e: # data validation 실패 시
        valid['msg'] = f'[STEP-3] VALIDATION : FAIL - {e}'
        valid['flag'] = False
    
    finally:
        write_log()

##############################################################################


# 4. database insert
##############################################################################

if valid['flag']:

    try: # parsing data insert
        # df.to_sql(table_name, con=engine, if_exists='append', index=False)
        valid['msg'] = (f'[STEP-4] DATA_INSERT : {len(df)} rows inserted into the table [{table_name}].')
    
    except Exception as e: # insert 실패 시
        valid['msg'] = f'[STEP-4] DATA_INSERT : FAIL - {e}'
        valid['flag'] = False
    
    finally:
        write_log()

##############################################################################


# 5. database update
##############################################################################

if logger != None: # logger 생성 성공 시에만

    try: # 최종 상태 변경 및 로그 기록
        if valid['flag']:
            # 상태 변경 로직 구현 필요
            valid['msg'] = '[STEP-5] EXCELPARSE : SUCCESS'
        else:
            # 상태 변경 로직 구현 필요
            valid['msg'] = '[STEP-5] EXCELPARSE : FAIL'
    
    except Exception as e: # 최종 상태 변경 실패 시
        valid['msg'] = f'[STEP-5] STATUS_UPDATE : FAIL - {e}'
    
    finally:
        write_log()

##############################################################################


# 6. module exit
##############################################################################

if logger != None:
    logger.debug(f"/*------------------------[ExcelParser] E n d : {str(datetime.datetime.now())}------------------------*/")

##############################################################################