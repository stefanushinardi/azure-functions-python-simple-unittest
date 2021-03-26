import logging

import azure.functions as func
import pyodbc

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    if name:
        return func.HttpResponse(name, status_code=200)
    else:
        return func.HttpResponse(
             "No name",
             status_code=200
        )
