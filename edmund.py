##################################################################################
##										     			      ##
##  Praveen Kumar Kotekal									  ##
##  Paper - Edmunds API Customer review and ratings Data Pull ##
##             												  ##
##														      ##
##################################################################################


# import necessary python libraries
from urllib2 import Request, build_opener
import simplejson
#import json
import pandas as pd
# edmunds.com API Key

key = 'your key'
fmt_api_key = 'fmt=json&api_key=' + key


#used to make omdbapi.com think we are getting this data from a browser
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

#scope of the api calls

# makes = ['honda', 'toyota', 'chevrolet', 'subaru']
makes = ['honda']
years = ['2011']

# base url for Edmunds Vehicle API
base_api_url = 'https://api.edmunds.com/api/vehicle/v2/'


# https://api.edmunds.com/api/vehicle/v2/{make}/models?fmt=json&api_key={api key}
# make = 'chevrolet'
# url = base_api_url + make + '/models?' + fmt_api_key
# req = Request(url, None, headers) #api request
# opener = build_opener() #submit the api request
# the_page = opener.open(req) #read the json from the api query
# json = simplejson.load(the_page) #
# print json


list_json = []

for make in makes:
    for year in years:
        try:
            url = base_api_url + make + '/models?year=' + year + '&' + fmt_api_key
            req = Request(url, None, headers) #api request
            opener = build_opener() #submit the api request
            the_page = opener.open(req) #read the json from the api query
            json = simplejson.load(the_page) #convert the json to a dict
            json['make'] = make
            list_json.append(json)
        except:
            continue

# store models json into a new dictionary object
data = {'items':list_json}
print list_json
# initiate a new list to store the model year IDs
model_list = []

# loop through each object in the data dictionary to store the make, model, year ID, and year
for item in data['items']:
    for model in item['models']:
        for year in model['years']:
            item_data = [item['make'], model['niceName'], str(year['id']), year['year']]
            model_list.append(item_data)

print "model_list", model_list
# store the model list into a dataframe
model_years_df = pd.DataFrame(model_list, columns=['make', 'model', 'year_id', 'year'])
model_years_df.to_excel('edmunds.xlsx')



