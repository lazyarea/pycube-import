import csv
import os
import sys
from django.core.management.base import BaseCommand
from lib.utils import *
from django.conf import settings
from importtxt.management.commands.lib.product import *

class Command(BaseCommand):

    def handle(self, *args, **options):

        data_dir = "/tmp"
        filter   = 'FCH_Product'
        if utils().exists_dir(data_dir) == False:
            print(data_dir + ' is not directory.')
            sys.exit()

        file = utils().getdirs(data_dir,filter)
        if (not file):
            utils().log_info('file is not found.',[])
            sys.exit()
        else:
            utils().log_info('%s %s' % (file,'is found.'),[])

        fpath = data_dir + '/' + file

        # read csv
        product().load_csv(fpath)

        # read yml
        #ypath = \
        #'/home/sites/eccube.example.com/src/Eccube/Resource/doctrine/Eccube.Entity.Product.dcm.yml'
        #yml = utils().read_yaml(ypath)
        #utils().read_entity(yml)

        # end
        utils().log_info('end',[])
