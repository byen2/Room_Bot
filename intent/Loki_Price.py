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
userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Price:
        print("[Price] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "2500到5000[中間]":
        # write your code here
        pass

    if utterance == "[每一個月]不[能]超過5000美金":
        # write your code here
        pass

    if utterance == "價錢2500美金到5000美金":
        # write your code here
        pass

    if utterance == "少於5000美金":
        # write your code here
        pass

    if utterance == "少於5000美金，超過[一點][也][行]":
        # write your code here
        pass

    return resultDICT