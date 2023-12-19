# imports
import pygame as py
import openai as ai
import time as  tm
# setup
ai.api_key = "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"
player = input(">>> ")
response = ai.ChatCompletion.create(model = "gpt-3.5-turbo" , massages=[{"role":"user" , "content":player }])
print(response.choices[0].massages.content)