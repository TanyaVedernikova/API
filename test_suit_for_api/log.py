import logging
import datetime

class LogTest:
    name_log = str(datetime.datetime.now())
    name_log = name_log.replace(' ', '_')
    name_log = name_log.replace('.', '_')
    name_log = name_log.replace(':', '_')
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.DEBUG, filename=name_log + '.log')

    def create_log_file():
        my_file = open(str(LogTest.name_log + '.log'), "w+")



LogTest.create_log_file()