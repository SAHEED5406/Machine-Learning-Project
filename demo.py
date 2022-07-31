from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logging import logging
from housing.config.configuration import Configuration

def main():
    try :
        #pipeline = Pipeline()
        #pipeline.run_pipeline()
        Configuration().get_data_validation_config()
    except Exception as e:
        logging.error(e)

if __name__ == "__main__" :
    main()
