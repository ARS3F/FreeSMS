#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s



banner = """
                                  
                                  
    _    ____  ____ _____ _____ 
   / \  |  _ \/ ___|___ /|  ___|
  / _ \ | |_) \___ \ |_ \| |_   
 / ___ \|  _ < ___) |__) |  _|  
/_/   \_\_| \_\____/____/|_|    
                                
                                                                                           
                                                                                                                                
| İstediginiz telefon adresine hergun 1 defa mesaj atma hakkınız vardır. 
| Mesajınız karakter sayısı sınırlı bunu mesajınızı yazdıktan sonra görüceksiniz.
| Tel adresinizi doğru girmezseniz hata alabilrsiniz.
| Bu araç THT üyelerine özel ARS3F tarafından hazırlanmıştır.

"""

print(banner)

sor = input("Tel adresi Örn:+905555555555 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek kısmı aşagıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajınız Gönderilsinmi?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hata yaptınız.")

