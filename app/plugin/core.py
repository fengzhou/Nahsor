import requests
from asserts import asserts

# req = {
#     "method":"GET",
#     "json":{"aaa":"bbb"},
#     "url":"http://127.0.0.1:2333/test",
#     "headers":{"Content-Type":"application/json"},
#     "timeout":10
# }
# validates = [
#     {"Equal":["r.json()","req[\"json\"]"]},
#     {"Equal":["r.status_code","200"]}
# ]
def httpcass(req,validates):
    '''
    requests接口方法,
    req为requests所需参数的字典,
    validates为校验所用的字典
    '''
    try:
        r = requests.request(**req)
    except requests.exceptions.Timeout as timeout:
        raise timeout
    for validate in validates:
        validate = validate.items()
        # print(validate)
        for key, values in validate:
            assert eval(values[0] + asserts[key] + values[1])
    return r


def analyzejson(spec):
    '''
    解析json,并返回req和validates
    '''
    req = spec.get("req",None)
    # print(req)
    validates = spec.get("validates", None)
    return req, validates