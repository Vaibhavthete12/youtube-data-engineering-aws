from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("youtube-category").getOrCreate()

# Read Bronze JSON
df = spark.read.json(
    "s3://youtube-data-engineering-vaibhav-2026/bronze/raw_statistics_reference_data/"
)

# Extract items array
items = df.selectExpr("explode(items) as item")

# Select required fields
clean_df = items.select(
    col("item.id").alias("category_id"),
    col("item.snippet.title").alias("category_name")
)

# Write Silver Layer
clean_df.write.mode("append").parquet(
    "s3://youtube-data-engineering-vaibhav-2026/silver/clean_reference_data/"
)

print("Category Data Processed Successfully")