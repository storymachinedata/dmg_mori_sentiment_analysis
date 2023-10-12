import boto3
import pandas as pd
from src.utils.helpers import read_json


class DataManagment:
    """This class maintains a connection with the AWS S3 to read and write
    data from a given a bucket.
    """

    def __init__(self):
        self.secret = read_json(path_to_file="../secret.json")
        self.access_key: str = self.secret["access_key"]
        self.secret_key: str = self.secret["secret_key"]
        self.bucket_name: str = self.secret["bucket_name"]
        self.region: str = self.secret["region"]
        self.s3: boto3.resource = self.connect_to_s3()

    def connect_to_s3(self):
        """This function establishes a connection provides an S3 resource
        object to perform transactions.

        Returns:
            boto3.resource: Returns the Boto3 instance object.
        """
        print("Created a connection to S3")
        return boto3.resource(
            service_name="s3",
            region_name=self.region,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
        )

    def read_dataframe_from_s3(self, folder_name: str, file_name: str):
        object_name = f"{folder_name}/{file_name}"
        try:
            s3_object_response = (
                self.s3.Bucket(self.bucket_name).Object(object_name).get()
            )
            print(f"Succesfully read {file_name} from S3")
            return pd.read_csv(s3_object_response["Body"], index_col=0)
        except:
            print("Error: check connection or file name")

    def upload_dataframe_to_s3(
        self, df: pd.DataFrame, folder_name: str, file_name: str
    ):
        df.to_csv(file_name)
        try:
            self.s3.Bucket(self.bucket_name).upload_file(
                Filename=file_name, Key=(folder_name + file_name)
            )
            print("Successfully uploaded!!")
        except:
            print("Failed to upload file!!")
