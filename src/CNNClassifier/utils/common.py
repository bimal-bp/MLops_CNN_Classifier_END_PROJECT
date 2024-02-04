import os
from box.exceptions import BoxValueError
import yaml
from CNNClassifier import logger 
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} load successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"create directory at :{path}")

@ensure_annotations
def save_json(path: path,data: dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f" json file saved at :{path}")


@ensure_annotations
def load_json(path:path) -> ConfigBox:
    with open(path) as f:
        content =json.load(f)
    logger.info(f"json file loaded succesfully from:{path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any,path:path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved")


@ensure_annotations
def load_bin(path:path) -> Any:
    data=joblib.load(path)
    logger.info(f"binary file loaded from:{path}")
    return data

@ensure_annotations
def get_size(path :path) -> str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"-{size_in_kb} KB"

def decode_images(imgstring,fileName):
    imgdata=base64.b64decode(imgstring)
    with open(fileName,'wb')as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb')as f:
        return base64.b64encode(f.read())