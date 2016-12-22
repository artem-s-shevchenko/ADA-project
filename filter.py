import json
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

def names_prepare(s):
    return s.lower()

metadata_path = "hdfs:///datasets/amazon-reviews/metadata.json"
review_path = "hdfs:///datasets/amazon-reviews/complete.json"
brands_path = "amazon/brands.json"
result_path = "amazon/result.json"

conf = SparkConf().setAppName("ADA-Swiss-Amazon")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

with open(brands_path) as data_file:
    brands = json.load(data_file)

metadata_df = sqlContext.read.json(metadata_path)
review_df = sqlContext.read.json(review_path)

filtered_df = metadata_df.where(metadata_df.brand.isin(brands))

joined_df = filtered_df.join(review_df, filtered_df.asin == review_df.asin, "left_outer")

joined_df.write.save(result_path, format="json")

#*****To do*****
#writing
#join (Too many open files) Bypass?
#check non-ascii symbols
#think about advanced filtering