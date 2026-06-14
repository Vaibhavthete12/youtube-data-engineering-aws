from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("youtube-statistics").getOrCreate()

# Read Bronze JSON
df = spark.read.json(
    "s3://youtube-data-engineering-vaibhav-2026/bronze/raw_statistics/"
)

# Extract items array
items = df.selectExpr("explode(items) as item")

# Select required columns
clean_df = items.select(
    col("item.id").alias("video_id"),
    col("item.snippet.title").alias("title"),
    col("item.snippet.channelTitle").alias("channel_title"),
    col("item.statistics.viewCount").alias("views"),
    col("item.statistics.likeCount").alias("likes"),
    col("item.statistics.commentCount").alias("comments"),
    col("item.snippet.categoryId").alias("category_id")
)

# Write Silver Layer
clean_df.write.mode("append").parquet(
    "s3://youtube-data-engineering-vaibhav-2026/silver/clean_statistics/"
)

print("Statistics Data Processed Successfully")