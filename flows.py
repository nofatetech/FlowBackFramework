
# region INIT APP

import time
from flask import Flask, request, g, jsonify
from sources import Sources
from dotenv import load_dotenv
import os
from flask_migrate import Migrate
# !!!!!!!
from data import db, Player, Post


# TODO: to use a config class or not, that is a question
# class Config:
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@db.host:5432/database_name'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL2')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

migrate = Migrate(app, db)  # Initialize Flask-Migrate with Flask app and SQLAlchemy instance



# time the request
@app.before_request
def start_timer():
    g.start_time = time.time()

@app.after_request
def end_timer(response):
    if hasattr(g, 'start_time'):
        elapsed_time = time.time() - g.start_time
        if response.is_json:
            data = response.get_json()
            data['x-x-x-elapsed-time-x-x-x'] = elapsed_time
            response.set_data(jsonify(data).get_data())
    return response


# endregion




# FLOWS

# region flows

class Flows:
    # !!!!!!!
    # get basic data for app homepage
    class GetHomeData:
        def run(self, params: dict):
            MyyyBloggg = Sources.MyyyBloggg()
            MyyyJokes = Sources.MyyyJokes()

            rett = {
                "token" : "123123",
                "latest_posts" : MyyyBloggg.get_posts({"categories":["blog"]}),
                "news" : MyyyBloggg.get_posts({"categories":["news"]}),
                "joke" : MyyyJokes.get_joke()
            }
            return rett
            pass
        
        def __init__(self, *args, **kwargs):
            pass

    class GetGodotTypes:
        def run(self, params: dict):
            tPlayer = Player()
            ttPlayer = tPlayer.generate_gdscript()
   
            rett = {
                "Player" : ttPlayer
            }
            return rett


# endregion




# region FLOWS LIST

# !!!!!!!
FLOWS = {
    "GetHomeData": Flows.GetHomeData,
    "Get home data now!!": Flows.GetHomeData,
}

# endregion






# ROUTES

# region ROUTES

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/flow', methods=['POST'])
def post_flow():
    rjson = request.get_json(silent=False)
    if rjson:
        flowname = rjson["flow"] or ""
        params = rjson["params"] or ""
    
    if flowname in FLOWS:
        flow = FLOWS[flowname]()
        flow_result = flow.run(params)
        rett = {
            "status": "ok",
            "flow_result": flow_result,
            "error": "",
        }
    else:
        rett = {
            "status": "error",
            "flow_result": None,
            "error": f"Flow Not Found - %s" % str(flowname),
        }
        # raise ValueError(f"Workflow '{flowname}' not found.")
    return jsonify(rett)


# endregion
