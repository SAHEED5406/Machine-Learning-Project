from flask import Flask
from housing.logging import logging

app = Flask(__name__)

@app.route('/' ,methods = ['Get' ,'Post'])
def index():
    logging.info('we are testing logging module')
    return "Starting Machine learning project"

if __name__ == "__main__":
    app.run(debug = True)
