from setuptools import setup
from typing import List



#Declaring variavles for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Saheed"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list():
    """
    Description: This function is going to return list of requirement
    mentioned in requirements.txt file
 
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description= "This is the housing predictor project",
    packages = ["housing"],
    install_requires = get_requirements_list()
)

