#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Price

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Price = True
userDefinedDICT = {"rent": ["房租", "租金"], "equipment": ["床", "房", "wifi", "WIFI", "Wifi", "internet", "Internet", "早餐", "吧台", "廚房", "健身房"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Price:
        print("[Price] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    resultDICT["Price"] = []

    if utterance == "[2500]到[5000美金]":
        # write your code here
        resultDICT["Price"].append(arg[0])
        resultDICT["Price"].append(arg[1])
        #pass

    if utterance == "少於[5000美金]":
        # write your code here
        #rewrite this stupid phrase
        pass

    if utterance == "房租[2500美金]到[5000美金]":
        # write your code here
        resultDICT["Price"].append(arg[0])
        resultDICT["Price"].append(arg[1])
        #pass

    return resultDICT