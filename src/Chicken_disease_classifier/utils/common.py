import os
from box.exceptions import BoxValueError
import yaml
from Chicken_disease_classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any 
import base64

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    This function reads a yaml file and returns a ConfigBox object
    
    Args:
        path_to_yaml (Path): file Path to yaml
    
    Raises:
        ValueError: If the yaml file is not found
        e: If the yaml file is not valid/empty
    
    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully read the yaml file from {path_to_yaml}")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("The yaml file is empty or not valid")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    This function create a list of directories

    Args:
        path_to_directories (list): list of directories to be created
        verbose (bool): whether to print logs or not, default is True
    """
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok = True)
        if verbose:
            logger.info(f"Directory created at : {directory}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    This function saves data to a json file

    Args:
        path (Path): file Path to save json file
        data (dict): data to be saved in json file
    """

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved to {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    This function loads data from a json file

    Args:
        path (Path): file Path to load json file
    
    Returns:
        ConfigBox: Data as class attributes instead of dict from json file
    """
    with open(path, 'r') as f:
        data = json.load(f)
    
    logger.info(f"json file loaded successfully from : {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    This function saves data to a binary file

    Args:
        data (Any): data to be saved
        path (Path): file Path to save binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved to : {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    This function loads data from a binary file

    Args:
        path (Path): file Path to load binary file
    
    Returns:
        Any: Data loaded from binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from : {path}")
    return data 

@ensure_annotations
def get_size(path: Path) -> str:
    """
    This function returns the size of the file

    Args:
        path (Path): file Path to get size
    
    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" ~ {size_in_kb} KB"

def decodeImage(imgstring, filename):
    """
    This function decodes the image from base64 string

    Args:
        imgstring (str): base64 string of image
        filename (str): name of the file to be saved
    
    """
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
    
def encodeImageIntoBase64(croppedImagePath):
    """
    This function encodes the image into base64 string

    Args:
        croppedImagePath (str): Path to the image
    
    Returns:
        str: base64 string of the image
    """
    with open(croppedImagePath, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
        return my_string