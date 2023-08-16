###### Packages

import http.client
import json
import requests
import pandas as pd
from config import *

class RavelryUtils:
    '''Initialize connection to Ravelry API'''

    def __init__(self, authUsername:str, authPassword:str):
        self.authUsername = authUsername
        self.authPassword = authPassword
        


    ### Methods

    def get_color_families(self) -> pd.core.frame.DataFrame:
        '''this returns all valid color families'''
        url = 'https://api.ravelry.com/color_families.json'      
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        r1.close()
        
        return pd.DataFrame.from_records(json.loads(r1.text)['color_families'])
    

    
    def get_patterns(self, query = '', page = 1, page_size = 100, craft = 'knitting') -> pd.core.frame.DataFrame:
        '''This returns the pattens from search.  Parameters include query (like 'hats'), page number, page size, and craft'''

        url = 'https://api.ravelry.com/patterns/search.json?query={}&page={}&page_size={}&craft={}'.format(query, page, page_size, craft)  
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        r1.close()
        
        return pd.DataFrame.from_records(json.loads(r1.text)['patterns'])
    

    def get_queue(self, rav_username = 'rieslingm', query = '', page = 1, page_size = 100) -> pd.core.frame.DataFrame:
        '''This returns all the patterns in queue from a given person's rav_username'''
        url = 'https://api.ravelry.com/people/{}/queue/list.json?query={}&page={}&page_size={}'.format(rav_username, query, page, page_size) 
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        r1.close()
        
        return pd.DataFrame.from_records(json.loads(r1.text)['queued_projects'])
    
    
    
    def get_favorites(self, rav_username = username, types = 'pattern', query = '', deep_search = '', page = 1, page_size = 100):
        '''This returns all the favorites from a given person's rav_username'''
        url = 'https://api.ravelry.com/people/{}/favorites/list.json?types={}&query={}&deep_search={}&page={}&page_size={}'.format(rav_username, types, query, deep_search, page, page_size) 
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        r1.close()
        
        return pd.DataFrame.from_records(json.loads(r1.text)['favorites']).favorited.apply(pd.Series)
    
    def get_projects(self, rav_username = username, types = 'pattern', query = '', deep_search = '', page = 1, page_size = 5):
        '''This returns all the projects from a given person's rav_username'''
        url = 'https://api.ravelry.com/people/{}/projects/list.json?types={}&query={}&deep_search={}&page={}&page_size={}'.format(rav_username, types, query, deep_search, page, page_size) 
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        r1.close()
        return Projects([self.get_project_full(id = id) for id in pd.DataFrame.from_records(json.loads(r1.text)['projects'])['id']])
    
    def get_project_full(self, rav_username = username, id = 0):
        '''This returns a full project given an ID from a given person's rav_username'''
        url = 'https://api.ravelry.com/projects/{}/{}.json?'.format(rav_username, id)
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        r1.close()
        return Project(json.loads(r1.text)['project'])

    def get_stash(self, rav_username = username, page = 1, page_size = 100):
        '''This returns a given person's stash'''
        url = 'https://api.ravelry.com/people/{}/stash/list.json?page={}&page_size={}'.format(rav_username, page, page_size) 
        r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(self.authUsername, self.authPassword))
        r1.close()
        
        return pd.DataFrame.from_records(json.loads(r1.text)['stash'])


class Projects:
    ''' Contains list of project IDs'''
    def __init__(self,projects_list):
        self.members = projects_list


class Project:
    ''' Contains details about a given project'''
    def __init__(self, project_dict):
        for k,v in project_dict.items():
            if k != "packs":
                self.__setattr__(k,v)
            else:
                self.__setattr__(k,Packs(v[0]))
                print(v[0])

class Packs:
    ''' Contains details about a given pack'''
    def __init__(self, project_dict):
         for k,v in project_dict.items():
            self.__setattr__(k,v)


# TODO: Class for each ravelry object, favourite, queue, project. can modify above methods to create instances of each class

