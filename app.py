# Module Imports
import os
import logging

from flask import Flask
from flask import render_template
from apicalls import riotapi
from apicalls import api
from flask_cors import CORS

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
app.register_blueprint(api.api,url_prefix = '/api')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#Set logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# @app.route('/view')
# def view():
#     # riotapis.GetSummonerDetails('scarra','na1')
#     # riotapis.GetRankDetails(os.environ['ID'],'na1')
#     # riotapis.GetMatchList("tisAYz-mOD-fKFvQ8deXGbUmG2e3iD5Baa9N4GLuUbfqEanQ52rCDW7YXyjHKtaBZEoGhNwVCpMYcg",'americas')
#     return render_template('index.html')

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template("index.html")