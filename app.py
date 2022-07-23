import sys
from flask import Flask
from housing.logging import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)

@app.route('/' ,methods = ['Get' ,'Post'])
def index():
    try:
        raise Exception("we are testing Exception module")
    
    except Exception as e :
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info('we are testing logging module')
    return "Starting Machine learning project"

if __name__ == "__main__":
    app.run(debug = True)
