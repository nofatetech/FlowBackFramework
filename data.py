
# region INIT



import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Initialize the database instance
db = SQLAlchemy()



# endregion



# MIXINS, COMPOSITION

# region MIXINS



class BaseModel:
    def save(self):
        # Common save logic
        pass

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


# MODELS

# region MODELS



class Player(db.Model, BaseModel, GamificationMixin, PlayerActionsMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f"<Player {self.username}>"

class Challenge(db.Model, BaseModel, GamificationMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Challenge {self.title}>"

class Post(db.Model, BaseModel, GamificationMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

    def __repr__(self):
        return f"<Post {self.title}>"



# endregion
