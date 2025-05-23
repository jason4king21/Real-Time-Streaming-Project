# Real-Time Streaming Project

This project demonstrates a real-time streaming data pipeline using AWS S3, API Gateway, Lambda, Kinesis Firehose, and Snowflake's Snowpipe.

## Architecture
![Architecture Diagram](diagrams/architecture.png)

## Components
- **API Gateway** receives incoming JSON data from external sources.
- **Lambda** processes and validates the data.
- **Kinesis Firehose** buffers and delivers the data to an S3 bucket.
- **Snowpipe** auto-ingests the data into Snowflake for querying.

## Tech Stack
- AWS Lambda
- API Gateway
- Kinesis Firehose
- AWS S3
- Snowflake + Snowpipe




