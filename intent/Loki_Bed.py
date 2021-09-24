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
        resultDICT["Bed"].append(args[0])
        #pass

    if utterance == "[兩]房[三]床":
        # write your code here
        resultDICT["Bed"].append(args[1])
        #pass

    return resultDICT