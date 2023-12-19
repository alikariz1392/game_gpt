# imports
import pygame as py
import openai as ai
import time as  tm
# setup
ai.api_key = "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"
breakwhile = True
while breakwhile:
    player = input(">>> ")
    response = ai.ChatCompletion.create(model = "gpt-3.5-turbo" , messages=[{"role":"user" , "content":player }])
    print(response.choices[0].message.content)
    if player in ["exit", "goodbye", 'bye']:
        breakwhile = False