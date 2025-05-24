# 🚀 Real-Time Streaming Data Pipeline

This project showcases a real-time data ingestion pipeline using **AWS** and **Snowflake**, simulating production-grade streaming from an external API into a cloud data warehouse.

---

## 🔧 Tech Stack

- **API Gateway** – Receives real-time JSON events  
- **AWS Lambda** – Parses, enriches, and routes data  
- **Amazon Kinesis Firehose** – Streams data to S3  
- **Amazon S3** – Acts as the landing zone for Snowflake ingestion  
- **Snowflake + Snowpipe** – Automatically ingests files into Snowflake tables  

---

## 🧩 Architecture Overview
![Real-Time Streaming Pipeline](diagrams/architecture.png)

1. **API Gateway**: Accepts POST requests from external sources
2. **Lambda Function**: Validates and enriches data; routes valid events to Firehose and errors to a separate S3 bucket
3. **Kinesis Firehose**: Buffers and delivers records to S3
4. **S3 Bucket**: Stores JSON files for downstream processing
5. **Snowpipe**: Automatically loads files from S3 into a Snowflake staging table for querying

---

## Tech Stack
- AWS Lambda
- API Gateway
- Kinesis Firehose
- AWS S3
- Snowflake + Snowpipe

## 📂 Repository Structure
```
Real-Time-Streaming-Project/
│
├── README.md                  → Project overview, setup instructions, and architecture details
├── diagrams/
│   └── architecture.png       → Visual diagram of the AWS + Snowflake pipeline
│   └── Diagram Generator/
│       └── architecture.py    → Python code to create the diagram
├── iam/
│   └── lambda_iam_role.json   → IAM role definition for AWS lambda permissions
├── lambda/
│   ├── api_gateway_lambda_handler.py     → Python code for AWS Lambda to process incoming API events
├── snowflake/
│   ├── snowpipe_trigger.sql     → SQL script to configure Snowpipe for auto-ingestion
├── tests/
│   └── sample.json            → Sample JSON file used to test the API and Lambda function
└── .gitignore                 → Specifies untracked files and directories to ignore in Git
```

---

## ✅ Highlights

- Serverless and scalable design
- Near real-time data visibility
- Minimal maintenance using managed services

---

## 🏷️ Tags & Topics
```
Use these hashtags when sharing the project:
#DataEngineering #AWS #Snowflake #RealTimeData #StreamingData #Serverless #ETL #DataPipeline #Kinesis #CloudComputing #Lambda
```
