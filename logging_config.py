import logging

root_path = './logs/';
levels = [
            logging.DEBUG, 
            logging.INFO, 
            logging.WARNING, 
            logging.ERROR, 
            logging.CRITICAL
         ];


def set_init_log(log_name, file_name, lv):
    level = levels[lv]

    # logger 생성
    logger = logging.getLogger(log_name)
    logger.setLevel(level)
    
    # fileHandler 설정
    file_hd = logging.FileHandler(root_path+file_name)
    file_hd.setLevel(level)

    # consoleHandler 설정
    console_hd = logging.StreamHandler()
    console_hd.setLevel(level)

    # 포맷 설정
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_hd.setFormatter(formatter)
    console_hd.setFormatter(formatter)

    # 핸들러 추가
    logger.addHandler(file_hd)
    logger.addHandler(console_hd)

    return logger
