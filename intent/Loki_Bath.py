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
userDefinedDICT = {"rent": ["房租", "租金"], "equipment": ["床", "房", "wifi", "WIFI", "Wifi", "internet", "Internet", "早餐", "吧台", "廚房", "健身房"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Bath:
        print("[Bath] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "乾濕分離":
        # write your code here
        pass

    if utterance == "公共[浴室]":
        # write your code here
        pass

    if utterance == "獨立[衛浴]":
        # write your code here
        pass

    return resultDICT