
# 1. setup
##############################################################################
import datetime

global log, valid
valid = {"flag" : False, "msg" : ''}

def write_log(): # valid_flag에 따라 debug or error로 기록
    global log, valid
    if log != None :
        if valid['flag']: 
            log.debug(valid['msg'])
        else:
            log.error(valid['msg'])

##############################################################################


# 2. chkData() : validate 시작점, type 별로 validate 수행
##############################################################################
def chkData(type, data, logger):
    global log, valid
    log = logger            # logger 설정
    
    log.debug(f"/*------------------------[chkData(type={type})] Start : {str(datetime.datetime.now())}------------------------*/")
    
    # type 별 valdiate method 수행
    if type == 'orders':
        chkOrders(type, data)

    log.debug(f"/*------------------------[chkData(type={type})] E n d : {str(datetime.datetime.now())}------------------------*/")
    
    return valid            # valid return
##############################################################################


# 3-1. chkOrders() : type='orders' validate
##############################################################################

def chkOrders(type, data):
    global log, valid
    log.debug(f'[chkOrders(type={type})] data length : {len(data)} rows')
    
    """
    #----Validation 로직 구현----#
    
    
    
    
    """

    #chkOrders DATA
    valid['flag'] = True
    valid['msg'] = f'[chkOrders(type={type})] - SUCCESS'
    write_log()

##############################################################################