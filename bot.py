from secrets import *
import tweepy

import wikipedia
import random
from datetime import date

wikipedia.set_lang("es")

today = date.today()

months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

fecha = today.strftime("%d") + " de " + months[today.month-1]
pag = wikipedia.page(fecha)
content = pag.content

table = content.split("\n")

nAcont = 0
fAcont = 0
for i, a in enumerate(table):
	if a == "== Acontecimientos ==":
		nAcont = i

	if nAcont != 0 and a == "":
		fAcont = i
		break


rAcont = table[random.randint(nAcont + 1, fAcont)].split(":")
txt = "Un día como hoy en " + rAcont[0] + rAcont[1]

# Bot
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

api.update_status(txt)