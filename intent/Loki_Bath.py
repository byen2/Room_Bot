#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Bath

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Bath = True
userDefinedDICT = {"rent": ["房租", "租金"], "animal": ["動物", "狗", "貓"], "service": ["wifi", "WIFI", "Wifi", "internet", "Internet", "早餐", "吧台", "廚房", "健身房"], "bathroom": ["衛浴", "浴室"], "quantity": ["一", "兩", "三", "四"], "money_type": ["美金", "台幣"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Bath:
        print("[Bath] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    resultDICT["Bath"] = []

    if utterance == "乾濕分離":
        #separate bathroom into dry and wet sections?
        # write your code here
        resultDICT["Bath"].append("乾濕分離")
        #pass

    if utterance == "公共[浴室]":
        # shared bathroom?
        # write your code here
        resultDICT["Bath"].append("shared")
        #pass

    if utterance == "獨立[衛浴]":
        # own bathroom?
        # write your code here
        resultDICT["Bath"].append("individual")
        #pass

    return resultDICT