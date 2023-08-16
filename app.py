import http.client
import json
import requests
import pandas as pd
from config import *
from classes import *



# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # trying out the ravelry API for the first time
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # load API token username and password
# # Please input your own credentials which you can make at https://www.ravelry.com/groups/ravelry-api

# #define URL for the API request
# url = 'https://api.ravelry.com/color_families.json'      
# #make the request
# r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(authUsername, authPassword))
# #close the connection
# r1.close()

# print("response code: {}".format(r1)) #tells me the response code
# print("response code Details: {}".format(r1.iter_lines())) #tells me details about the response code
# print("response output:")
# print(r1.text) #tells me the output
# print("response output formatted:")
# print(json.dumps(json.loads(r1.text), indent=4)) #makes the json more readable

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # trying an API request with parameters
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #define URL for the API request
# url = 'https://api.ravelry.com/patterns/search.json'      
# #make the request
# r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(authUsername, authPassword))
# #close the connection
# r1.close()

# print("response code: {}".format(r1)) #tells me the response code
# print("response code Details: {}".format(r1.iter_lines())) #tells me details about the response code
# print("response output:")
# print(r1.text) #tells me the output
# print("response output formatted:")
# print(json.dumps(json.loads(r1.text), indent=4)) #makes the json more readable


# #define parameters
# query = 'flamingo'
# page = 6
# page_size = 2
# craft = 'knitting'

# #define URL for the API request
# url = 'https://api.ravelry.com/patterns/search.json?query={}&page={}&page_size={}&craft={}'.format(query, page, page_size, craft)      
# #make the request
# r1 = requests.get(url, auth=requests.auth.HTTPBasicAuth(authUsername, authPassword))
# #close the connection
# r1.close()

# print("response code: {}".format(r1)) #tells me the response code
# print("response code Details: {}".format(r1.iter_lines())) #tells me details about the response code
# print("response output:")
# print(r1.text) #tells me the output
# print("response output formatted:")
# print(json.dumps(json.loads(r1.text), indent=4)) #makes the json more readable

#first, define an isntance of the class
raveleryutils_api = raveleryutils(authUsername, authPassword)

# # Get yarn weights
# color_families = raveleryutils_api.get_color_families()

# # TOP PATTERNS
# top_hat_patterns = raveleryutils_api.get_patterns(query = 'hat', page = 15, page_size = 2)
# top_patterns = raveleryutils_api.get_patterns()
# print("get_patterns columns: {}".format(top_patterns.columns))
# print("top pattern names:" )

# QUEUED PATTERNS
#get the data
# queue1 = raveleryutils_api.get_queue(rav_username = 'amcsw', page_size = 100)
# queue2 = raveleryutils_api.get_queue(rav_username = 'rieslingm', page_size = 100)
# print("items in queue: {}".format(len(queue1)))


# Favorites
# I know this will not work because my credentials are not good enough
# favorite_patterns = raveleryutils_api.get_favorites(rav_username = 'amcsw')
# print(favorite_patterns)


# Stash

stash = raveleryutils_api.get_stash(rav_username = 'amcsw')
print(stash)