valid = {"flag" : False, "msg" : ''}

def chkData(type, data):
    if type == 'orders':
        chkOrders(type, data)
    return valid

def chkOrders(type, data):
    #chkOrders DATA
    valid['flag'] = True
    valid['msg'] = f'VALIDATION - SUCCESS, {type}, {data}'