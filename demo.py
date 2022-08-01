from housing.component import data_transformation
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logging import logging
from housing.config.configuration import Configuration
from housing.component.data_validation import DataValidation
from housing.component.data_ingestion import DataIngestion

def main():
    try :
        #pipeline = Pipeline()
        #pipeline.run_pipeline()
        data_ingestion_config = Configuration().get_data_ingestion_config()
        #data_ingestion_artifact = DataIngestion(data_ingestion_config).initiate_data_ingestion()
        data_validation_config = Configuration().get_data_validation_config()
        #DataValidation(data_validation_config=data_validation_config ,data_ingestion_artifact=data_ingestion_artifact).initiate_data_validation()
        data_transformation_config = Configuration().get_data_transformation_config()
    except Exception as e:
        logging.error(e)

if __name__ == "__main__" :
    main()
