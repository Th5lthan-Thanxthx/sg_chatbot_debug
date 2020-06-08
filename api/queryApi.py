import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class yycQuery(object):
    def __init__(self):
        self.base_url = 'http://192.168.0.250:8080/css/0.1/ext-api';
        self.url = '';

    # 1.1 查询领药日期
    def query_patientreceivetime(self,post_data={}):
        self.url = self.base_url+'/getPatientReceiveTime?app_key=16a5918f502K1tE'
        #post_data = {"idsn":"330204194912300016", "drugName":"瑞复美"}
        return self.query(post_data)

    # 1.2 查询城市药房列表
    def query_citydrugstore(self,post_data={}):
        self.url = self.base_url+'/getCityDrugSore?app_key=16a5918f502K1tE'
        #post_data = {"city":"北京", "drugName":"瑞复美"}
        return self.query(post_data)

    # 1.3 查询热线号码
    def query_hotlinenumber(self,post_data={}):
        self.url = self.base_url+'/queryHotlineNumber?app_key=16a5918f502K1tE'
        #post_data = {}
        return self.query(post_data)

    # 1.4 查询邮寄地址
    def query_emailaddr(self, post_data={}):
        self.url = self.base_url+'/getEmailAddr?app_key=16a5918f502K1tE'
        #post_data = {"drugName":"瑞复美"}
        return self.query(post_data)

    # 1.5 查询药房电话(冗余)
    def query_drugstorephone(self,post_data={}):
        self.url = self.base_url+'/getDrugStorePhone?app_key=16a5918f502K1tE'
        #post_data = {"name":"北京众协阳光大药房有限公司"}
        return self.query(post_data)

    # 1.6 查询药房地址
    def query_drugstoreaddr(self,post_data={}):
        self.url = self.base_url+'/getCityDrugSoreAddr?app_key=16a5918f502K1tE'
        #post_data = {"drugStore":"北京众协阳光大药房有限公司", "city":"北京"}
        return self.query(post_data)

    # 1.7 查询患者进度
    def query_patientprocess(self,post_data={}):
        self.url = self.base_url+'/getPatientProcess?app_key=16a5918f502K1tE'
        #post_data = {"name":"郑孝甫", "mobile":"13917003811", "drugName":"瑞复美"}
        return self.query(post_data)

    # 1.8 查询患者领药药房(冗余)
    def query_patientreceivedrugstore(self,post_data={}):
        self.url = self.base_url+'/getPatientReceiveDrugSore?app_key=16a5918f502K1tE'
        #post_data = {"name":"郑孝甫", "mobile":"13917003811", "drugName":"瑞复美"}
        return self.query(post_data)

    # 2.1 发票丢失
    def query_invoicemissing(self,post_data={}):
        self.url = self.base_url+'/invoiceMissing?app_key=16a5918f502K1tE'
        #post_data = {"drugName":"福可维"}
        return self.query(post_data)

    # 2.2 发票不全
    def query_invoiceincomplete(self,post_data={}):
        self.url = self.base_url+'/invoiceIncomplete?app_key=16a5918f502K1tE'
        #post_data = {"drugName":"福可维"}
        return self.query(post_data)

    # 2.3 发票复印件/发票替代品
    def query_invoicephotocopy(self,post_data={}):
        self.url = self.base_url+'/invoicePhotocopy?app_key=16a5918f502K1tE'
        #post_data = {"drugName":"福可维"}
        return self.query(post_data)

    # 2.4 发票报销
    def query_invoicereimbursement(self,post_data={}):
        self.url = self.base_url+'/invoiceReimbursement?app_key=16a5918f502K1tE'
        #post_data = {"drugName":"福可维", "reimbursement":0}
        return self.query(post_data)

    # 2.5 发票回寄
    def query_invoicepostback(self,post_data={}):
        self.url = self.base_url+'/invoicePostBack?app_key=16a5918f502K1tE'
        #post_data = {"drugName":"福可维"}
        return self.query(post_data)

    def query(self,post_data={}):
        # headers =  { "content-type": "application/json" }
        headers =  { "Content-type": "application/json; charset=UTF-8" }
        r = requests.post(self.url,json=post_data, headers=headers)
        result = json.loads(str(r.content,'UTF-8'))
        logger.info(result)
        return result

