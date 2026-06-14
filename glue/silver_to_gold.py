from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("gold-layer").getOrCreate()

# Read Silver statistics
stats_df = spark.read.parquet(
    "s3://youtube-data-engineering-vaibhav-2026/silver/clean_statistics/"
)

# Read Silver category data
ref_df = spark.read.parquet(
    "s3://youtube-data-engineering-vaibhav-2026/silver/clean_reference_data/"
)

# Convert datatype for join
stats_df = stats_df.withColumn(
    "category_id",
    col("category_id").cast("string")
)

ref_df = ref_df.withColumn(
    "category_id",
    col("category_id").cast("string")
)

# Join
joined_df = stats_df.join(
    ref_df,
    "category_id",
    "inner"
)

# Final Gold dataset
gold_df = joined_df.select(
    "video_id",
    "title",
    "channel_title",
    "views",
    "likes",
    "comments",
    "category_name"
)

# Write Gold layer
gold_df.write.mode("append").parquet(
    "s3://youtube-data-engineering-vaibhav-2026/gold/trending_analytics/"
)

print("Gold Layer Created Successfully")