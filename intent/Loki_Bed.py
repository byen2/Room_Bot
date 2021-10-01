#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Bed

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from ArticutAPI import Articut
import json

with open("account.info", encoding="utf-8") as f:
    userinfoDICT = json.loads(f.read())

articut = Articut(username=userinfoDICT["username"], apikey=userinfoDICT["apikey"], level = "lv3")

DEBUG_Bed = True
userDefinedDICT = {"rent": ["房租", "租金"], "animal": ["動物", "狗", "貓"], "service": ["wifi", "WIFI", "Wifi", "internet", "Internet", "早餐", "吧台", "廚房", "健身房"], "bathroom": ["衛浴", "浴室"], "quantity": ["一", "兩", "三", "四"], "money_type": ["美金", "台幣"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Bed:
        print("[Bed] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    resultDICT["Bed"] = []

    if utterance == "[一]張床":
        # write your code here
        res = articut.parse(args[0])
        bed_num = list(res['number'].values())
        resultDICT["Bed"].append(bed_num)
        #pass

    if utterance == "[兩]房[三]床":
        # write your code here
        res = articut.parse(args[1])
        bed_num = list(res['number'].values())
        resultDICT["Bed"].append(bed_num)
        #pass

    return resultDICT