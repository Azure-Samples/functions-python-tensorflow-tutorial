import logging

import azure.functions as func

import json

# Import helper script
from . import predict

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    image_url = req.params.get('img')
    # Scoring step
    results = predict.predict_image_from_url(image_url)

    headers = {
        "Content-type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }

    return func.HttpResponse(json.dumps(results), headers = headers)
