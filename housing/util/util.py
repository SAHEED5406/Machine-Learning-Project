import yaml
from housing.exception import HousingException
from housing.logging import logging
import os ,sys

def read_yaml_file(file_path:str)->dict:
    """
    Reads the YAML file and returns the conntents as a dictionary 
    file path : str
    """

    try :
        with open(file_path ,"rb") as yaml_file :
            return yaml.safe_load(yaml_file)
    
    except Exception as e :
        raise HousingException(e,sys) from e
