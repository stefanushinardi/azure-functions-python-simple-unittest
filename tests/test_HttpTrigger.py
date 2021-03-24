import unittest

import azure.functions as func
from HttpTrigger import main

class TestFunctions(unittest.TestCase):
    def test_http_trigger_happy_case(self):
        test_name = "Azure"

        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/HttpTrigger',
            params={'name': test_name})

        resp = main(req)
        
        self.assertEqual(
            resp.get_body().decode(),
            test_name
        )

        
    def test_http_trigger_sad_case(self):
        test_name = "Azure"

        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/HttpTrigger',
            params=None)

        resp = main(req)
        
        self.assertEqual(
            resp.get_body().decode(),
            "No name"
        )