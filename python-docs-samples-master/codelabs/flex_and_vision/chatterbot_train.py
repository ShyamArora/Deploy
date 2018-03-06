#!/usr/bin/python
# coding: utf-8
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatterbot = ChatBot("Terminal",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
database='./database.json')
chatterbot.set_trainer(ListTrainer)

conversation = [
"Hello",
"Hello there! How may I help you?",
"Hi",
"Hello there! How may I help you?",
"Hello MEON",
"Hello there! How may I help you?",
"Hi MEON",
"Hello there! How may I help you?",
"Hey MEON",
"How are you doing?, How may I help you?",
"How are you doing?",
"I'm doing great. How may I help you?",
"Thank you",
"You're welcome, Always at your service.",
"Bye",
"Okay, see you soon. Have a great day!",
"I am doing good",
"Glad to hear! How may I help you?",
"I am doing great",
"Glad to hear! How may I help you?",
"okay",
"Is there anything else that I can help you with today?",
"ok",
"Is there anything else that I can help you with today?",
"okk",
"Is there anything else that I can help you with today?",
"ok then",
"Is there anything else that I can help you with today?",
"thanks",
"You're welcome, Always at your service.",
"thanks for help",
"You're welcome, Always at your service.",
"thankyou",
"You're welcome, Always at your service.",
"Hallo",
"Hallo! Wie geht es Ihnen?",
"Mir geht es gut",
"Froh zu hören! Wie kann ich dir helfen?",
"Vielen Dank",
"Sie sind herzlich willkommen und bitte sagen Sie mir, wenn Sie jederzeit helfen können. Immer für Sie da",
"こんにちは","こんにちは！ どのように私はあなたを助けることができる？",
"こんにちは"," こんにちは！ どのように私はあなたを助けることができる？",
"お元気ですか？","私は素晴らしいことをしています。どうすればあなたを助けることができますか？",
"ありがとうございました","あなたは歓迎です、いつもあなたのサービスで。",
"さよなら","さて、お会いしましょう。素晴らしい一日を！",
]

chatterbot.train(conversation)


def chat(inpt):
    a =chatterbot.get_response(inpt)
    b = str(a)
    c = b[0:-1]
    print(c)
    return c
#put your any input you want to give to bot in below method to get output
chat("さよなら")
