import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class yycQuery(object):
    def __init__(self):
        self.base_url = 'http://192.168.0.70/chat';
        self.url = '';

    def query_receipt(self, post_data={}):
        self.url = self.base_url+'/index'
        return self.query(post_data)


    def query_drugstore(self,post_data={}):
        self.url = self.base_url+'/drugstore'
        return self.query(post_data)


    def query(self,post_data={}):
        r = requests.post(self.url,data=post_data)
        result = json.loads(str(r.content,'UTF-8'))
        logger.info(result)
        return result