
from pyspark import SparkConf
from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, collect_list
from enum import Enum
import traceback
import time
import sys
import logging
#import boto3
#import pandas as pd
from datetime import date

# set logger to stdout
logger = logging.getLogger(__name__) 
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#AWS_ACCESS_KEY_ID = {AWS_ACCESS_KEY_ID}
#AWS_SECRET_ACCESS_KEY= {AWS_SECRET_ACCESS_KEY}


class RECON_CODES(Enum):
    A_EQUALS_B = 0
    A_COLS_NOT_IN_B = 1
    B_COLS_NOT_IN_A = 2
    A_COLS_DT_NOT_EQUALS_B = 3
    A_ROWS_NOT_IN_B = 4
    B_ROWS_NOT_IN_A = 5

class SparkWrapper:
    def __init__(self, appname:str, conf:SparkConf):
        self._spark = None
        self._appname = appname
        self._conf = conf

    def __del__(self):
        self._spark.stop()

    def __enter__(self):
        #self._spark = SparkSession.builder.master("local[*]").config(conf = self._conf).appName(self._appname).getOrCreate()
        self._spark = SparkSession.builder.master("yarn").config(conf = self._conf).appName(self._appname).getOrCreate()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
            # return False # uncomment to pass exception through
        self._spark.stop()
        return True


        

    @property
    def spark(self):
        return self._spark    



def reconcile(fileA, fileB) -> any:
    

    # dataA = []
    columnsA = ["cd","name","gender","age","div","salary"]
    # with open(fileA, "r") as fp:
    #     while True:
    #         l = fp.readline()
    #         if not l:
    #             break
    #         t = tuple(l.strip("\n").split(","))
    #         dataA.append( tuple([t[0], t[1], t[2], t[3], t[4], int(t[5])]) )  

    # dataB = []
    columnsB = ["cd","name","gender","age","div","salary"]
    # with open(fileB, "r") as fp:
    #     while True:
    #         l = fp.readline()
    #         if not l:
    #             break
    #         t = tuple(l.strip("\n").split(","))
    #         dataB.append( tuple([t[0], t[1], t[2], t[3], t[4], int(t[5])]) )    

    # s3 = boto3.client('s3') 
    # obj = s3.get_object(Bucket= "my-emr-bucket-raikhovn", Key= "emr-input/" + fileA) 
    # dataA = pd.read_csv(obj['Body'])

    # obj = s3.get_object(Bucket= "my-emr-bucket-raikhovn", Key= "emr-input/" + fileB) 
    # dataB = pd.read_csv(obj['Body'])
              
    logger.info ("prepare spark conf")
  
    # AMD 6 cores, 7GB memory
    conf = SparkConf()
    conf.set("spark.executor.cores", 2) # keep one core for daemon process
    conf.set("spark.executor.instances", 2)
    conf.set("spark.executor.memory", "2g")
    conf.set("spark.executor.memoryOverhead", "200m") # 10% of executor memory
    conf.set("spark.driver.memory", "2g")
    conf.set("spark.driver.cores", 2)
    conf.set("spark.default.parallelism", 6 * 1 * 12) # number cores per node * number of nodes * number of tasks per core

    # add account keys for s3 access

    
  

    # Compare columns first
    try:
        with SparkWrapper("recon", conf) as sw:
            #dfA = sw.spark.createDataFrame(data = dataA, schema = columnsA)
            #dfB = sw.spark.createDataFrame(data = dataB, schema = columnsB)
            logger.info ("creating dataA.csv")
            key = 's3a://my-emr-bucket-raikhovn/emr-input/dataA.csv'
            dfA = sw.spark.read.format('csv').option('header','true').load(key)
            logger.info ("creating dataB.csv")
            key = 's3a://my-emr-bucket-raikhovn/emr-input/dataB.csv'
            dfB = sw.spark.read.format('csv').option('header','true').load(key)

            logger.info ("running col recon")
            # Compare names
            lA = dfA.columns.sort()
            lB = dfB.columns.sort()
            
            if (lA != lB):
                s = set(lB)
                inAnotB = [x for x in lA if x not in s] 
                if len(inAnotB) != 0:
                    return RECON_CODES.A_COLS_NOT_IN_B
            
                s = set(lA)
            
                inBnotA = [x for x in lB if x not in s]
                if len(inBnotA) != 0:
                    return RECON_CODES.B_COLS_NOT_IN_A
                
            

        
            
            
            # Compare data types
            if (dfA.dtypes.sort() != dfB.dtypes.sort()):
                return RECON_CODES.A_COLS_DT_NOT_EQUALS_B
            
            logger.info ("saving data stats")
            # calculate salary aggregate for selected  by gender
            salA = dfA.groupBy("gender").agg(F.sum("salary").alias("salary_sum"), F.avg("salary").alias("salary_avg"), F.min("salary").alias("salary_min"), F.min("salary").alias("salary_max"))
            salB = dfB.groupBy("gender").agg(F.sum("salary").alias("salary_sum"), F.avg("salary").alias("salary_avg"), F.min("salary").alias("salary_min"), F.min("salary").alias("salary_max"))
            key = 's3a://my-emr-bucket-raikhovn/emr-output/%s/dataAstats.csv'%(date.today())
            salA.write.format('csv').option('header','true').save(key,mode='overwrite')
            key = 's3a://my-emr-bucket-raikhovn/emr-output/%s/dataBstats.csv'%(date.today())
            salB.write.format('csv').option('header','true').save(key,mode='overwrite')
        
            
            

        
            # 

            #salA.show()
            #salB.show()

            #print(dfA.rdd.getNumPartitions())
            #print(dfB.rdd.getNumPartitions())
            logger.info ("running recon")
            # Compare rows
            diffAB = dfA.exceptAll(dfB)
            if diffAB.count() != 0:
                #diffAB.show()
                key = 's3a://my-emr-bucket-raikhovn/emr-output/%s/dataABrecon.csv'%(date.today())
                diffAB.write.format('csv').option('header','true').save(key,mode='overwrite')
                return RECON_CODES.A_ROWS_NOT_IN_B

            diffBA = dfB.exceptAll(dfA)
            if diffBA.count() != 0:
                #diffBA.show()
                return RECON_CODES.B_ROWS_NOT_IN_A
    
            #time.sleep(10000)
    except Exception as ex:
        logger.error("error occured executing job: %s", str(ex))

    return RECON_CODES.A_EQUALS_B

def sample():
    spark = SparkSession.builder.master("local[*]").appName("shit").getOrCreate()

    data = [('001','Smith','M',40,'DA',4000),
            ('002','Rose','M',35,'DA',3000),
            ('003','Williams','M',30,'DE',2500),
            ('004','Anne','F',30,'DE',3000),
            ('005','Mary','F',35,'BE',4000),
            ('006','James','M',30,'FE',3500)]

    columns = ["cd","name","gender","age","div","salary"]
    df = spark.createDataFrame(data = data, schema = columns)
    

    df.printSchema()
    df.show()

    spark.stop()

if __name__ == "__main__":

    inputA = "dataA.txt"
    inputB = "dataB.txt"
    if len(sys.argv) - 1  == 2:
        inputA = sys.argv[1]
        inputA = sys.argv[2]
    
    logger.info("args: %s %s", inputA, inputB)

    r = reconcile(inputA, inputB)
