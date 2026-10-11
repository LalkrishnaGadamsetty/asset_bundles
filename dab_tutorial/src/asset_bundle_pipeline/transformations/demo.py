import dlt
from pyspark.sql.functions import *


@dlt.table
def demo_table():
    return spark.range(100)