from lib.classes.APICollector import APICollector
from contracts.schema import CompraSchema
from tools.aws.client import S3Client

import time
import schedule

schema = CompraSchema
aws = S3Client()

def apiCollector(schema, aws, num):
    APICollector(schema, aws).start(num)
    print('Dado Coletado e armazenado na AWS.')

schedule.every(1).minutes.do(apiCollector,schema, aws, 50)

while True:
    schedule.run_pending()
    time.sleep(1)
