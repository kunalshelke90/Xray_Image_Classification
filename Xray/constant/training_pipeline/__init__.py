from datetime import datetime
from typing import List
import torch

TIMESTAMP:datetime=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

#data ingestion constants

ARTIFACT_DIR:str="artifacts"
BUCKET_NAME:str="xraybucket"
S3_DATA_FOLDER:str= "data"