
# region INIT



import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declared_attr
from dataclasses import dataclass


# Initialize the database instance
db = SQLAlchemy()



# endregion



# MIXINS, COMPOSITION

# region MIXINS


# example:
# newuser = params["newuser"] or None
# if newuser:
#     carl = Player(**newuser)
#     res1 = carl.save(db.session)

@dataclass
class BaseDataModel:
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

# Some functionality I want for many of my data types (models)
class BaseModel:
    # @declared_attr
    # def __tablename__(cls):
    #     return cls.__name__.lower()

    # TODO: easy save methods here?
    def save(self, session):
        rett = {"result":"", "error": ""}
        try:
            session.add(self)
            session.commit()
            rett["status"] = "OK"
            return "OK"
        except exc.SQLAlchemyError as e:
            session.rollback()
            error_message = f"ERROR!! SQLAlchemyError: {str(e)}"
            rett["status"] = "error"
            rett["error"] = error_message
        except Exception as e:
            session.rollback()
            error_message = f"ERROR!! Exception: {str(e)}"
            rett["status"] = "error"
            rett["error"] = error_message
        return rett

    def delete(self):
        # Common delete logic
        pass

class GamificationMixin:
    def player_add_points(self, points: float, challenge: 'Challenge' = None):
        pass

class PlayerActionsMixin:
    def perform_action(self, action: str):
        if action == "login":
            return f"Player {self.username} logged in."
        elif action == "logout":
            return f"Player {self.username} logged out."
        else:
            return "Unknown action."

class PostActionsMixin:
    pass



# endregion


# TYPES / MODELS

# region TYPES / MODELS



class Player(db.Model, BaseDataModel, BaseModel, GamificationMixin, PlayerActionsMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f"<Player {self.title}>"

class Challenge(db.Model, BaseDataModel, BaseModel, GamificationMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Challenge {self.title}>"

class Post(db.Model, BaseDataModel, BaseModel, GamificationMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

    def __repr__(self):
        return f"<Post {self.title}>"



# endregion
