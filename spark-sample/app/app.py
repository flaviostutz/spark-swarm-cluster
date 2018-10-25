print('My Spark application')

import sys
from random import random
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    print('>>>> Starting Spark Session')
    spark = SparkSession\
        .builder\
        .appName("MyFirstPiApp")\
        .getOrCreate()

    partitions = 16
    n = 100000 * partitions
    print('>>>> Will use ' + str(partitions) + ' partitions')

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        print('>>> sleeping for 5s...')
        time.sleep(5)
        print('>>> woke up!')
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    print('>>>> Calculating PI')

    try:
        count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
        print("Pi is roughly %f" % (4.0 * count / n))

    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        print('exception ' + str(e))

    print('>>>> DONE!')

    spark.stop()
