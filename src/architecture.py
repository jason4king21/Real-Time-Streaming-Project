from diagrams import Diagram, Node
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import KinesisDataFirehose
from diagrams.aws.storage import S3

class CustomSnowflake(Node):
    _provider = "custom"
    _icon_dir = "../resources"  # One level up from src/

    # fontcolor = "#ffffff"
    _dot_attrs = {
        "shape": "none",
        "xlabel": "Snowflake"
    }

    def __init__(self, label="snowflake"):
        super().__init__(label)

with Diagram("Real-Time Streaming Pipeline", show=False, filename="../diagrams/architecture", outformat="png"):
    api = APIGateway("API Gateway")
    lam = Lambda("Lambda Processor")
    firehose = KinesisDataFirehose("Firehose")
    s3 = S3("S3 Bucket")
    snowflake = CustomSnowflake("snowflake")

    api >> lam >> firehose >> s3 >> snowflake
