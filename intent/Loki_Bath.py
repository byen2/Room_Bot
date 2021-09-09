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
userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Bath:
        print("[Bath] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[兩張]床":
        # write your code here
        pass

    if utterance == "兩人住，[一張]床就[行]":
        # write your code here
        pass

    return resultDICT