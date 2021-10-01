#!/usr/bin/env python
# -*- coding:utf-8 -*-

import discord
import json
from Apt_Bot import botRunLoki
import datetime

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())


templateDICT = {
    "Bed":None,
    "Bath":None,
    "Price":None,
    "Amenities":[],
    #"updatetime":None
}

mscDICT = {
    #"id":templateDICT
}



class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author.name == self.user:
            return None

        print("到到來自 {} 的訊息".format(message.author.name))
        print("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            print("本 bot 被叫到了！")
            msg = message.content.replace("<@!{}> ".format(self.user.id), "")
            #resultDICT = botRunLoki(msg, [])

            if msg.lower() in ("hi", "", "hey", "hello"):
                await message.reply("hey there!")

                #@TODO does not recognize returning users, remove for now
                if message.author.name in mscDICT.keys():
                    #await message.reply("hey there!")
                    #nowDATETIME = datetime.datetime.now()
                    #timeDIFF = nowDATETIME - mscDICT[message.author.name]["updatetime"]
                    #if timeDIFF.total_seconds() >= 300: #longer than 5 min from last conversation.
                    #    mscDICT[message.author.name] = templateDICT
                    #    await message.reply("您好！為了這次的住宿，想要找什麼樣的房型條件呢？")
                    #else:
                    #    await message.reply("我還在等您的決定。")
                    print("user exists")
                else:
                    mscDICT[message.author.name] = templateDICT

            else:
                resultDICT = botRunLoki(msg, [])
                #Fulfill the four items listed in templateDICT
                for k in resultDICT.keys():
                    mscDICT[message.author.name][k] = resultDICT[k]

                for k in mscDICT[message.author.name].keys():
                    print(mscDICT.items())
                    if mscDICT[message.author.name][k] == None or mscDICT[message.author.name][k] == []:
                        if k == "Bed":
                            replySTR = "需要幾張床呢？"
                            break
                        elif k == "Bath":
                            replySTR = "想要什麼樣的衛浴呢？"
                            break
                        elif k == "Price":
                            replySTR = "價位有什麼考量嗎？"
                            break
                        elif k == "Amenities":
                            replySTR = "特別需要哪些設備嗎？"
                            break
                        #elif k == "updatetime":
                        #    break
                    else:
                        replySTR = message.author.name + " 要找的房間是："
                        for item in mscDICT.values():
                            replySTR += "{}".format(item)

                        #@TODO replace brackets with empty space
                        #current replySTR result:
                        #SafeHaven 要找的房間是：{'Bed': [[3]], 'Bath': ['乾濕分離'], 'Price': ['>5000'], 'Amenities': ['水電費']}
                        replySTR.replace("{","").replace("}","").replace("[","").replace("]","") #this doesnt work
                await message.reply(replySTR)






if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])