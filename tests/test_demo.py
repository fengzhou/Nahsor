# -*- coding:utf-8 -*-
def exex_global_values(request):
    '''
    {
        "url": "http://127.0.0.1:2333/test",
        "json": {'token': '$extracts["token"]'},
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "timeout": 10
    }
    '''
    execlist = []
    for key in request:
        if type(request[key]) == dict:
            for key1 in request[key]:
                # print(key)
                if '$' == request[key][key1][:1]:
                    # print(key1)
                    execkey = "request[%s][%s] = %s" % (key, key1, request[key][key1][1:])
                    execlist.append(execkey)
                    # print(execkey)
    return execlist



request =  {
        "url": "http://127.0.0.1:2333/test",
        "json": {
            'token': 'extracts["token"]'
        },
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "timeout": 10
    }
r = exex_global_values(request)
print(r)