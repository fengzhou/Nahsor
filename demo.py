import random


def sschszxds():
    hcode = ""
    hnum = random.randint(1, 10)
    # print(betNum)
    for x in range(hnum):
        qylot = list(range(0, 10))
        hlist = random.sample(qylot, 2)
        code = ""
        for i in hlist:
            code += "%s," % i
        if code[:-1] in hcode:
            print(code)
            print(hcode)
            continue
        hcode += code[:-1]+"|"
    hcode = hcode[:-1]
    betNum = len(hcode.split("|"))
    print("code:'", hcode)
    print("bet_num:'%s'" % betNum)
    return hcode, betNum


# a = "f"
# if a in "sdf":
#     print("OK")
# print("good")



sschszxds()
