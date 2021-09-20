import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
level = input('请输入日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）：')
message = input('请输入消息：')
if level == 'DEBUG':
    logger.log(logging.DEBUG,message)
elif level == 'INFO':
    logger.log(logging.INFO,message)
elif level == 'WARNING':
    logger.log(logging.WARNING,message)
elif level == 'ERROR':
    logger.log(logging.ERROR,message)
elif level == 'CRITICAL':
    logger.log(logging.CRITICAL,message)
