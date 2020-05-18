from urllib import parse,request
import json
import requests

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.update(iterable)
       

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


    def say(self):
        print(self.__update)

if(__name__ == '__main__'):
    url = "http://192.168.0.70/wechat/run"
    url = "http://www.baidu.com"
    textmod = {"username": "admin", "password": "admin", "rememberMe": True}
    textmod = json.dumps(textmod).encode(encoding='utf-8')
    header_dict = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    req = request.Request(url=url, data=textmod, headers=header_dict)
    res = request.urlopen(url)
    # # print(res)
    res = res.read()
    res = res.decode(encoding="utf-8")
    # with request.urlopen('http://www.python.org/') as f:
    #     print(f.read(300).decode('utf-8'))
    # cookies = dict(cookiename='working')
    # r = requests.get(url,cookies=cookies)
    # print(r.raw.read(10))
    # print(r.json())
    print(r.content)
    print(r.text)