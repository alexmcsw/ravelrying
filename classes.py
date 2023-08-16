###### Packages

import http.client
import json
import requests
import pandas as pd
from config import *

class raveleryutils:

    # first, set up everything that you will need to connect to the API.
    def __init__(self, authUsername:str, authPassword:str):
        self.authUsername = authUsername
        self.authPassword = authPassword
        
    
    #next, define any functions you will need.  This way, we define it once but can use it as many times as we would like
    
    # this returns all valid color families
    def get_color_families(self) -> pd.core.frame.DataFrame:
        #define URL
        url = 'https://api.ravelry.com/color_families.json'      
        #make the request
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        #close the connection
        r1.close()
        
        return pd.DataFrame.from_records(json.loads(r1.text)['color_families'])
    
    # This returns the pattens from search.  Parameters include query (like "hats"), page number, page size, and craft
    def get_patterns(self, query = '', page = 1, page_size = 100, craft = 'knitting') -> pd.core.frame.DataFrame:
        #define URL
        url = 'https://api.ravelry.com/patterns/search.json?query={}&page={}&page_size={}&craft={}'.format(query, page, page_size, craft)  
        #make the request
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        #close the connection
        r1.close()
        
        return pd.DataFrame.from_records(json.loads(r1.text)['patterns'])
    
    # This returns all the patterns from a given person's rav_username
    def get_queue(self, rav_username = 'rieslingm', query = '', page = 1, page_size = 100) -> pd.core.frame.DataFrame:
        #define URL
        url = 'https://api.ravelry.com/people/{}/queue/list.json?query={}&page={}&page_size={}'.format(rav_username, query, page, page_size) 
        #make the request
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        #close the connection
        r1.close()
        
        return pd.DataFrame.from_records(json.loads(r1.text)['queued_projects'])
    
    
    # This returns all the favorites from a given person's rav_username
    def get_favorites(self, rav_username = username, types = 'pattern', query = '', deep_search = '', page = 1, page_size = 100) -> list:
        #define URL
        url = 'https://api.ravelry.com/people/{}/favorites/list.json?types={}&query={}&deep_search={}&page={}&page_size={}'.format(rav_username, types, query, deep_search, page, page_size) 
        #make the request
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        #close the connection
        r1.close()
        
        return pd.DataFrame.from_records(json.loads(r1.text)["favorites"]).favorited.apply(pd.Series)
    

    # This returns a given person's stash
    def get_stash(self, rav_username = username, page = 1, page_size = 100) -> list:
        #define URL
        url = 'https://api.ravelry.com/people/{}/stash/list.json?page={}&page_size={}'.format(rav_username, page, page_size) 
        #make the request
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        #close the connection
        r1.close()
        
        return pd.DataFrame.from_records(json.loads(r1.text)["stash"])
