import logging
import time

class LogTest:

    def create_log_file():
        my_file = open(str(time.time()) + '.log', "w+")
        logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.DEBUG, filename=my_file)
        logging.info('Test ok')
        logging.error('Test failed')