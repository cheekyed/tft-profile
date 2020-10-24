import os
import requests
import logging

from flask import current_app as app

#Env Variables
riot_key = os.environ['RIOT_API_KEY']

def GetSummonerDetails(SummonerName, Region):
    try:
        response = requests.get(f"https://{Region}.api.riotgames.com/tft/summoner/v1/summoners/by-name/{SummonerName}?api_key={riot_key}")
        app.logger.debug(response.content)
        os.environ['PUUID'] = response.json()['puuid']
        os.environ['ID'] = response.json()['id']
        os.environ['NAME'] = response.json()['name']
        app.logger.debug(response.json()['id'])
        app.logger.debug(response.json()['puuid'])
    except Exception as e:
        app.logger.exception('Exception Occured %s' %repr(e))
        os.environ['PUUID'] = ''
        os.environ['ID'] = ''
        os.environ['NAME'] = ''
    return response.json()

def GetRankDetails(EncryptedId,Region):
    try:
        response = requests.get(f"https://{Region}.api.riotgames.com/tft/league/v1/entries/by-summoner/{EncryptedId}?api_key={riot_key}")
        app.logger.debug(response.json())
    except Exception as e:
        app.logger.exception('Exception Occured %s' %repr(e))
    return response.json()

def GetMatchList(Puuid,Region):
    try:
        response = requests.get(f"https://{Region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{Puuid}/ids?count=10&api_key={riot_key}")
        app.logger.debug(response.json())
    except Exception as e:
        app.logger.exception('Exception Occured %s' %repr(e))

def GetMatchDetails(MatchId,Region):
    try:
        response = requests.get(f"https://{Region}.api.riotgames.com/tft/match/v1/matches/NA1_3587548931?api_key={riot_key}")
        app.logger.debug(response.json())
    except Exception as e:
        app.logger.exception('Exception Occured %s' %repr(e))
    return response.json()

