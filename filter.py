import json
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
import os
import shutil

metadata_path = "hdfs:///datasets/amazon-reviews/metadata.json"
review_path = "hdfs:///datasets/amazon-reviews/complete.json"
brands_path = "./amazon/brands.json"
result_path = "amazon/results/"
final_result_path = "amazon/res.json"

conf = SparkConf().setAppName("ADA-Swiss-Amazon")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

with open(brands_path) as data_file:
    brands = json.load(data_file)

metadata_df = sqlContext.read.json(metadata_path)
review_df = sqlContext.read.json(review_path).withColumnRenamed("asin", "asin2")

#In the data we are interested in fields asin (we use it to merge tables) and
# brand (we use it for filtering). Therefore, we drop null values.
#Experiments which were done during preparation:

#metadata.json
#9430088 full
#1808958 cleaned brand
#9429757 cleaned asin

#complete.json
#142831980 cleaned full
#142831980 cleaned asin
metadata_df = metadata_df.dropna(subset=["asin", "brand"])

#Important information: ALL brands are in ascii, even those, which has non-ascii
#symbols in the original name (e.g. Neslté in life and Nestle in data).
filtered_df = metadata_df.where(metadata_df.brand.isin(brands))

joined_df = filtered_df.join(review_df, filtered_df.asin == review_df.asin2, "left_outer").drop("asin2")

print("*****", joined_df.count(), "*****")

if os.path.exists(result_path):
    shutil.rmtree(result_path)
joined_df.write.save("file:///home/shevchen/" + result_path, format="json")

#Creating one json file from multiple ones
paths = [result_path + f for f in os.listdir(result_path) if f[0] != "." and f[0] != "_"]

with open(final_result_path, "w") as big_file:
    big_file.write("[\n")
    for path in paths:
        with open(path) as file:
            lines = file.readlines()
            i = 0
            for line in lines:
                i += 1
                if path == paths[-1] and i == len(lines):
                    big_file.write(line)
                else:
                    big_file.write(line[:-1] + ",\n")
    big_file.write("]\n")
