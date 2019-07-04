import logging

import azure.functions as func

import json
import os
import io

# Import helper script
from . import predict

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Initialize model
    predict.initialize()

    image_url = req.params.get('img')
    # Scoring step
    results = predict.predict_url(image_url)

    return json.dumps(results)
