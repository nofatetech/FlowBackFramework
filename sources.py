
# region INIT



import requests, os


# !!!!!!!
from data import Post



# endregion


# region BASE SOURCES



class BaseSourceSpotify:
    name = "Spotify Source"
    api_url = "https://api.spotify.com/api/v1"
    auth_token = ("TOKWNSLSJDL") # TODO: security

    def __init__():
        pass

    def get_playlists():
        return []

class BaseSourceWordpress:
    name = ""
    api_url = ""
    auth_token = ""

    def __init__(self):
        pass

    def get_posts(self, filters: dict):
        # TODO: http requst to API URL

        url = self.api_url + "/posts"
        response = requests.get(url)

        # TODO: Adapters
        # latest_posts2 = []
        # for item in latest_posts:
        #     item2 = Post(id = item.id, title = item.title.rendered)
        #     # item2.id = 
        #     latest_posts2.append(item2)

        return []
        # return latest_posts2



# endregion


# TODO: implement adapters?


# region SOURCES



class Sources:

    # !!!!!!!

    class MyyyBloggg(BaseSourceWordpress):
        name = "My Personal Blog!!!"
        api_url = "https://johnsblog1234.wordpress.com/api/v1"
        auth_token = os.environ.get("MYYYBLOGGG_AUTH_TOKEN")
        
    class MyyyPlaylistsss(BaseSourceSpotify):
        name = "My Playlists!!!"
        auth_token = os.environ.get("MYYYPLAYLISTSSS_AUTH_TOKEN")
    
    # some random custom data i want
    class MyyyJokes:
        def __init__(self) -> None:
            pass
        
        def get_joke(self):
            return "this is a joke"

    # connect to other stuff
    class MyHouseIOT:
        def turn_on_garden_lights_and_set_relax_mood():
            # ..send http calls to my house IOT system..
            return {"status": "Mood set, sir!"}
        

        
# endregion    


