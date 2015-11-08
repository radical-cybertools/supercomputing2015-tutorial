import os, sys, time

if not os.environ.has_key("SPARK_HOME"):
    SPARK_HOME="/usr/hdp/2.3.2.0-2950/spark-1.5.1-bin-hadoop2.6/"    
    os.environ["SPARK_HOME"]=SPARK_HOME
else:
    SPARK_HOME=os.environ["SPARK_HOME"]
    

#print "Init Spark: " + SPARK_HOME

os.environ["PYSPARK_PYTHON"]="/opt/anaconda/bin/python"
os.environ["PYSPARK_DRIVER_PYTHON"]="ipython"
os.environ["PYSPARK_DRIVER_PYTHON_OPTS"]="notebook"
os.environ["PYTHONPATH"]= os.path.join(SPARK_HOME, "python")+":" + os.path.join(SPARK_HOME, "python/lib/py4j-0.8.2.1-src.zip")
    
sys.path.insert(0, os.path.join(SPARK_HOME, "python"))
sys.path.insert(0, os.path.join(SPARK_HOME, 'python/lib/py4j-0.8.2.1-src.zip')) 
sys.path.insert(0, os.path.join(SPARK_HOME, 'bin') )

# import Spark Libraries
from pyspark import SparkContext, SparkConf, Accumulator, AccumulatorParam
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.mllib.linalg import Vector