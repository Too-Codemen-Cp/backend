import asyncio
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from aiobotocore.session import get_session

load_dotenv()

class S3Client:
    def __init__(self,
                 access_key: str,
                 secret_key: str,
                 endpoint_url: str,
                 bucket_name: str,):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key":secret_key,
            "endpoint_url": endpoint_url,
            "verify": False,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(self,file_path: str,object_name:str,):
        async with self.get_client() as client:
            with open(file_path, "rb") as file:
                await client.put_object(
                    Bucket=self.bucket_name,
                    Key=object_name,
                    Body=file
                )

# async def main():
#     s3_client = S3Client(
#         access_key=os.getenv("access_key"),
#         secret_key=os.getenv("secret_key"),
#         endpoint_url=os.getenv("endpoint_url"),
#         bucket_name="slava1"
#     )
#
#     await s3_client.upload_file("vilka.jpeg", "vilka.jpeg")
#
# if __name__ == "__main__":
#     asyncio.run(main())