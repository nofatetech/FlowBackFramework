
# region INIT



import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from dataclasses import dataclass, field
from sqlalchemy import Column, Integer, DateTime, func


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
class BaseDataModel(Base):
    __abstract__ = True  # This ensures the MyyyMyyyBaseModel class is not created as a table itself
    id: int = field(init=False, default=None)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime = field(default=None)

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    def save(self, session):
        rett = {"result":"", "error": ""}
        try:
            self.updated_at = datetime.now(timezone.utc)
            session.add(self)
            session.commit()
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

    def soft_delete(self, session):
        rett = {"result":"", "error": ""}
        try:
            self.deleted_at = datetime.now(timezone.utc)
            session.add(self)
            session.commit()
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


# Some functionality I want for many of my data types (models)
class SimpleBaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # crate object with any dict
    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        if data:
            for key, value in data.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, default=None)

    def save(self, session):
        rett = {"result":"", "error": ""}
        try:
            self.updated_at = datetime.now(timezone.utc)
            session.add(self)
            session.commit()
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

    def soft_delete(self, session):
        rett = {"result":"", "error": ""}
        try:
            self.deleted_at = datetime.now(timezone.utc)
            session.add(self)
            session.commit()
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


# Some functionality I want for many of my data types (models)
class MyyyBaseModel:
    pass


class PlayerAuthMixin:
    auth_token = db.Column(db.Text, unique=True, nullable=True)
    

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



class Player(db.Model, SimpleBaseModel, PlayerAuthMixin, GamificationMixin, PlayerActionsMixin):
    name = db.Column(db.Text, unique=True, nullable=False)
    username = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def __repr__(self):
        return f"<Player {self.title}>"


class Challenge(db.Model, BaseDataModel, MyyyBaseModel, GamificationMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Challenge {self.title}>"

class Post(db.Model, BaseDataModel, MyyyBaseModel, GamificationMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

    def __repr__(self):
        return f"<Post {self.title}>"



# endregion
