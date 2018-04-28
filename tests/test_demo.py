# -*- coding:utf-8 -*-
import requests
req = 	{"url": "http://127.0.0.1:2333/login", "json": {"username": "admin","password":"123456"}, "method": "POST", "headers": {"Content-Type": "application/json"}, "timeout": 10}
r = requests.request(**req)
print(r.text)
print(r.json())