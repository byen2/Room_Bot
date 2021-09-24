#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Amenities

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Amenities = True
userDefinedDICT = {"rent": ["房租", "租金"], "animal": ["動物", "狗", "貓"], "service": ["wifi", "WIFI", "Wifi", "internet", "Internet", "早餐", "吧台", "廚房", "健身房"], "bathroom": ["衛浴", "浴室"], "quantity": ["一", "兩", "三", "四"], "money_type": ["美金", "台幣"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Amenities:
        print("[Amenities] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    resultDICT["Amenities"] = []

    if utterance == "[可以]養[動物]":
        # write your code here
        resultDICT["Amenities"].append(args[1])
        #pass

    if utterance == "[家具][都]包含":
        # write your code here
        resultDICT["Amenities"].append(args[0])
        #pass

    if utterance == "[洗衣機]和[烘乾機][都]包含":
        # write your code here
        resultDICT["Amenities"].append(args[0])
        resultDICT["Amenities"].append(args[1])
        #pass

    if utterance == "[附近]有[捷運站]":
        # write your code here
        resultDICT["Amenities"].append(args[1])
        #pass

    if utterance == "不[能]抽煙":
        # write your code here
        resultDICT["Amenities"].append("smoke-free")
        #pass

    if utterance == "包含[水電費]":
        # write your code here
        resultDICT["Amenities"].append("水電費")
        #pass

    if utterance == "有[廚房]":
        # write your code here
        resultDICT["Amenities"].append(args[0])
        #pass

    if utterance == "有[餐廳]和[客廳]":
        # write your code here
        resultDICT["Amenities"].append(args[0])
        resultDICT["Amenities"].append(args[1])
        #pass

    return resultDICT