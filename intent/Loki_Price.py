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
userDefinedDICT = {"rent": ["房租", "租金"], "animal": ["動物", "狗", "貓"], "service": ["wifi", "WIFI", "Wifi", "internet", "Internet", "早餐", "吧台", "廚房", "健身房"], "bathroom": ["衛浴", "浴室"], "quantity": ["一", "兩", "三", "四"], "money_type": ["美金", "台幣"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Price:
        print("[Price] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    resultDICT["Price"] = []

    if utterance == "[2500]到[5000][美金]":
        # write your code here
        resultDICT["Price"].append(args[0] + "-" + args[1])
        #pass

    if utterance == "少於[5000][美金]":
        # write your code here
        resultDICT["Price"].append(">" + args[0])
        #pass

    if utterance == "房租[2500][美金]到[5000][美金]":
        # write your code here
        resultDICT["Price"].append(args[0] + "-" + args[1])
        #pass

    return resultDICT