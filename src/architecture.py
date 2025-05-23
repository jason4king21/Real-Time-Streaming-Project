from diagrams import Diagram
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import KinesisDataFirehose
from diagrams.aws.storage import S3
from diagrams.generic.database import SQL  # Placeholder for Snowflake

with Diagram("Real-Time Streaming Pipeline", show=False, filename="diagrams/architecture2", outformat="png"):
    api = APIGateway("API Gateway")
    lam = Lambda("Lambda Processor")
    firehose = KinesisDataFirehose("Firehose")
    s3 = S3("S3 Bucket")
    snowflake = SQL("Snowflake")

    api >> lam >> firehose >> s3 >> snowflake
