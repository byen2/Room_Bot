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
userDefinedDICT = {"rent": ["房租", "租金"], "equipment": ["床", "房", "wifi", "WIFI", "Wifi", "internet", "Internet", "早餐", "吧台", "廚房", "健身房"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Bed:
        print("[Bed] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一張][床]":
        # write your code here
        pass

    if utterance == "[兩]房[三]床":
        # write your code here
        pass

    return resultDICT