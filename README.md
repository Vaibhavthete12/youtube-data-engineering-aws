# YouTube Data Engineering Pipeline Using AWS

## Overview
This project builds an end-to-end AWS Data Engineering pipeline using YouTube API.

## AWS Services Used
- AWS Lambda
- Amazon S3
- AWS Glue
- AWS Step Functions
- Amazon SNS
- AWS Athena

## Architecture
YouTube API → Lambda → S3 Bronze → Glue Silver → Glue Gold → Athena → SNS

## Data Layers
Bronze → Raw JSON Data  
Silver → Cleaned Parquet Data  
Gold → Analytics Ready Data

## Features
- Automated YouTube API Data Ingestion
- ETL Pipeline using AWS Glue
- Medallion Architecture
- Cloud Native Data Engineering Pipeline