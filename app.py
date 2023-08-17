import http.client
import json
import requests
import csv
import pandas as pd
from config import *
from classes import *


#first, define an isntance of the class
ravelryutils_api = RavelryUtils(authUsername, authPassword)



# QUEUED PATTERNS
#get the data
queue = ravelryutils_api.get_queue(rav_username = 'amcsw', page_size = 100)
#print(queue)


# Favorites

projects = ravelryutils_api.get_projects(rav_username = 'amcsw')
#print(favorite_patterns)

# Favorites

favorite_patterns = ravelryutils_api.get_favorites(rav_username = 'amcsw')


print(favorite_patterns)


# # Stash

# stash = raveleryutils_api.get_stash(rav_username = 'amcsw')
# print(stash)


with open("favorites.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(projects.members[0].__dict__.keys())
    writer.writerows(projects.members)