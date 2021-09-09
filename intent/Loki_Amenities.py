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
userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Amenities:
        print("[Amenities] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[可以]養動物":
        # write your code here
        pass

    if utterance == "[附近]有捷運站":
        # write your code here
        pass

    if utterance == "[附近]有游泳池":
        # write your code here
        pass

    if utterance == "不[能]抽煙":
        # write your code here
        pass

    if utterance == "包含水電費":
        # write your code here
        pass

    if utterance == "家具[都]包含":
        # write your code here
        pass

    if utterance == "有健身房":
        # write your code here
        pass

    if utterance == "有廚房":
        # write your code here
        pass

    if utterance == "有餐廳和客廳":
        # write your code here
        pass

    if utterance == "洗衣機和烘乾機[都]需要":
        # write your code here
        pass

    return resultDICT