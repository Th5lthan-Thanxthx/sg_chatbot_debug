import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class yycQuery(object):
    def __init__(self):
        self.base_url = 'http://192.168.0.250:8080/css/0.1/ext-api';
        self.url = '';

    # 查询发票邮寄地址
    def query_emailaddr(self, post_data={}):
        self.url = self.base_url+'/getEmailAddr?app_key=16a5918f502K1tE'
        #post_data = {"name":"郑孝甫", "mobile":"13917003811", "papProjectName":"瑞复美"}
        return self.query(post_data)

    # 查询患者领药药房
    def query_receivedrugstore(self,post_data={}):
        self.url = self.base_url+'/getPatientReceiveDrugSore?app_key=16a5918f502K1tE'
        #post_data = {"name":"郑孝甫", "mobile":"13917003811", "papProjectName":"瑞复美"}
        return self.query(post_data)

    # 查询领药药房地址
    def query_drugstoreAddress(self,post_data={}):
        self.url = self.base_url+'/getDrugSoreAddress?app_key=16a5918f502K1tE'
        #post_data = {"name":"北京众协阳光大药房有限公司"}
        return self.query(post_data)

    # 查询药房电话
    def query_drugstorephone(self,post_data={}):
        self.url = self.base_url+'/getDrugStorePhone?app_key=16a5918f502K1tE'
        #post_data = {"name":"北京众协阳光大药房有限公司"}
        return self.query(post_data)

    # 查询城市药房
    def query_citydrugstore(self,post_data={}):
        self.url = self.base_url+'/getCityDrugSore?app_key=16a5918f502K1tE'
        #post_data = {"city":"北京"}
        return self.query(post_data)

    # 查询申请进度
    def query_patientprocess(self,post_data={}):
        self.url = self.base_url+'/getPatientProcess?app_key=16a5918f502K1tE'
        #post_data = {"name":"郑孝甫", "mobile":"13917003811", "papProjectName":"瑞复美"}
        return self.query(post_data)

    # 查询领药日期
    def query_patientreceivetime(self,post_data={}):
        self.url = self.base_url+'/getPatientReceiveTime?app_key=16a5918f502K1tE'
        #post_data = {"name":"郑孝甫", "mobile":"13917003811", "papProjectName":"瑞复美"}
        return self.query(post_data)

    def query(self,post_data={}):
        # headers =  { "content-type": "application/json" }
        headers =  { "Content-type": "application/json; charset=UTF-8" }
        r = requests.post(self.url,json=post_data, headers=headers)
        result = json.loads(str(r.content,'UTF-8'))
        logger.info(result)
        return result

