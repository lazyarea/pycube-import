import datetime
import os.path
import re
import logging
import yaml
import pymysql
from django.conf import settings

class utils:
    def sample(self):
        print("utils.sample()")

    def get_conn(self):
        dbconf = settings.DATABASES['default']
        return pymysql.connect(host=dbconf['HOST'], port=3306, user=dbconf['USER'], passwd=dbconf['PASSWORD'], db=dbconf['NAME'])

    # def close_db(self,conn=[]):
    #     conn.close()

    def log_info(self,msg,data):
        logging.basicConfig(filename='example.log',level=logging.DEBUG)
        logging.info('[%s] %s [%s]' % (datetime.datetime.today(), msg, ",".join(data)))


    def exists_dir(self,dpath):
        return os.path.exists(dpath)

    def exists_file(self,fpath):
        return os.path.exists(fpath)

    def getdirs(self,target,filter):
        dirs = []
        for item in os.listdir(target):
            if re.match(filter, item):
                return item

        return None

    def read_yaml(self,fpath):
        if not self.exists_file(fpath):
            return None

        f = open(fpath, 'r')
        data = yaml.load(f)
        f.close()
        return data

    def read_entity(self,data):
        keynm = None
        for key in data:
            if(re.match('^Eccube', key)):
                return data[key]['fields']
