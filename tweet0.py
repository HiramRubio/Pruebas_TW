#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:47:01 2019

@author: Steven
"""
import pandas
import tweepy


#Leemos un CSV con las Keys para evitar tenerlas en el codigo
df = pandas.read_csv('Keys2.csv')
CK = df['Key'][0]
AT = df['Key'][1]
CS = df['Secret'][0]
ATS = df['Secret'][1]

# Autenticacion con Twitter
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)

# Create API object
api = tweepy.API(auth)

#Verificamos que nos pudimos autenticar
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
 
#Resumen de la informacion de la cuenta
user = api.me()
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))

#"""
# Creando un tweet
#api.update_status("Hola Tweepy")
    
# Create un tweet con media
#path = '/Users/rt/Desktop/Sty/Modificaciones/'
#img = "Img0.jpg"
#message = "Ahora  puedo subir media! #TwitterAPI"
#api.update_with_media(img, status=message)