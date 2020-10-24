from apicalls import riotapi
from flask import Blueprint
from flask import current_app as app
from flask_cors import cross_origin

import os

api = Blueprint('api', __name__, template_folder='templates')

@cross_origin()
@api.route('/profile')
def GetProfile():
    SummonerDetails = riotapi.GetSummonerDetails('scarra','na1')
    RankData = riotapi.GetRankDetails(os.environ['ID'],'na1')
    ProfileDict = {}
    ProfileDict['SummonerName'] = os.environ['NAME']
    if not RankData:
        ProfileDict['Rank'] = ''
        ProfileDict['Tier'] = 'Unranked'
        ProfileDict['Lp'] = ''
    else:
        try:
            ProfileDict['Rank'] = RankData[0]['rank']
            ProfileDict['Tier'] = RankData[0]['tier']
            ProfileDict['Lp'] = RankData[0]['leaguePoints']
            ProfileDict['ProfileIconId'] = SummonerDetails['profileIconId']
        except Exception as e:
            app.logger.exception('Exception Occured %s' %repr(e))
            ProfileDict['SummonerName'] = 'No Data'
            ProfileDict['Rank'] = 'No Data'
            ProfileDict['Tier'] = 'No Data'
            ProfileDict['Lp'] = 'No Data'
            ProfileDict['ProfileIconId'] = 'No Data'
        
    app.logger.debug('ProfileDict = ' + str(ProfileDict))
    return ProfileDict

@cross_origin()
@api.route('/match')
def GetMatch():
    MatchDetails = riotapi.GetMatchDetails('NA1_3587548931','americas')
    MatchDict = {}
    for player in MatchDetails['info']['participants']:
        if player['puuid'] == 'tisAYz-mOD-fKFvQ8deXGbUmG2e3iD5Baa9N4GLuUbfqEanQ52rCDW7YXyjHKtaBZEoGhNwVCpMYcg':
            MatchDict['Placement'] = player['placement']
            MatchDict['Traits'] = player['traits']
            MatchDict['Units'] = player['units']
    app.logger.debug(MatchDict)
    return MatchDict

    
