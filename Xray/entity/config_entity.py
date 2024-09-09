from Xray.constant.training_pipeline import *
import os
from torch import device
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.s3_data_folder:str=S3_DATA_FOLDER
        self.bucket_name:str=BUCKET_NAME
        self.artifacts_dir:str=os.path.join(ARTIFACT_DIR,TIMESTAMP)
        self.data_path:str=os.path.join(self.artifacts_dir,"data_ingestion",self.s3_data_folder)
        self.train_data_path:str =os.path.join(self.data_path,"train")
        self.test_data_path:str =os.path.join(self.data_path,"test")
        