import pytest
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

class UspsGeneric:
    message=""
    def __init__(self):
        pass

    def generateLabel(self,labelRequest):
        url = "http://xpit.4log.com/Magicxpi4.7/MgWebRequester.dll?appname=IFSUSPS_Generic&prgname=HTTP&arguments=-AUSPS_Service%23Trigger1&testMode=1"
        headers = {}
        service_response = requests.request("POST", url, headers=headers, data = labelRequest)
        if (service_response.status_code!=200):
            self.message="No response from service"
            return 0
        print("response time:"+str(service_response.elapsed.total_seconds()))
        self.message=service_response.text
        return 1

