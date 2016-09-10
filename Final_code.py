
from urllib2 import Request, build_opener
import simplejson
import pandas as pd
#import json
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

# edmunds.com API Key
key = 'sc3svg35bkwdr2nr8qg46prf'
fmt_api_key = 'fmt=json&api_key=' + key
#  API call for recalls using model year IDs
# for index, row in model_years_df.iterrows():
years = ['2012','2013', '2015', '2016', '2017']
models = ['brz',
'crosstrek',
'forester',
'impreza',
'impreza-wrx',
'legacy',
'outback',
'tribeca',
'wrx',
'xv-crosstrek']
# url1 = 'https://api.edmunds.com/v1/api/maintenance/recallrepository/findbymodelyearid?modelyearid=' + year_id + '&' + fmt_api_key
records = []
for model in models:
    for year in years:

        try:
        # url = 'https://api.edmunds.com/api/vehiclereviews/v2/honda/accord/2015?' + fmt_api_key
            u = 'https://api.edmunds.com/api/vehiclereviews/v2/subaru/' + model + '/' + year + '?' + fmt_api_key
            print u
            req = Request(u, None, headers) #api request
            opener = build_opener() #submit the api request
            the_page = opener.open(req) #read the json from the api query
            json = simplejson.load(the_page) #convert the json to a dict
            for review in json['reviews']:

                try:
                    text_review = review['text']
                except:
                    text_review = ''

                try:
                    userRating = review['userRating']
                except:
                    userRating = ''

                try:
                    styleId = review['styleId']
                except:
                    styleId = ''

                try:
                    id = review['id']
                except:
                    id = ''

                try:
                    purchaseDate = review['carDetailsDto']['purchaseDate']
                except:
                    purchaseDate = ''

                try:
                    pricePaid = review['carDetailsDto']['pricePaid']
                except:
                    pricePaid = ''

                try:
                    odometerMiles = review['carDetailsDto']['odometerMiles']
                except:
                    odometerMiles = ''

                try:
                    title = review['title']
                except:
                    title = ''

                try:
                    commentsCount = review['commentsCount']
                except:
                    commentsCount = ''

                try:
                    averageRating = review['averageRating']
                except:
                    averageRating = ''

                try:
                    rearSeats = review['comfortRatingDto']['rearSeats']
                except:
                    rearSeats = ''

                try:
                    frontSeats = review['comfortRatingDto']['frontSeats']
                except:
                    frontSeats = ''


                try:
                    comfortRating = review['comfortRatingDto']['comfortRating']
                except:
                    comfortRating = ''


                try:
                    gettingInOut = review['comfortRatingDto']['gettingInOut']
                except:
                    gettingInOut = ''

                try:
                    rideComfort = review['comfortRatingDto']['rideComfort']
                except:
                    rideComfort = ''


                try:
                    noiseAndVibration = review['comfortRatingDto']['noiseAndVibration']
                except:
                    noiseAndVibration = ''

                try:
                    authorName = review['author']['authorName']
                except:
                    authorName = ''

                try:
                    entertainment = review['technologyRatingDto']['entertainment']
                except:
                    entertainment = ''

                try:
                    climateControl = review['technologyRatingDto']['climateControl']
                except:
                    climateControl = ''

                try:
                    bluetooth = review['technologyRatingDto']['bluetooth']
                except:
                    bluetooth = ''

                try:
                    usbPorts = review['technologyRatingDto']['usbPorts']
                except:
                    usbPorts = ''

                try:
                    technologyRating = review['technologyRatingDto']['technologyRating']
                except:
                    technologyRating = ''

                try:
                    navigation = review['technologyRatingDto']['navigation']
                except:
                    navigation = ''

                try:
                    parkingAids = review['safetyRatingDto']['parkingAids']
                except:
                    parkingAids = ''


                try:
                    outwardVisibility = review['safetyRatingDto']['outwardVisibility']
                except:
                    outwardVisibility = ''


                try:
                    rainSnowTraction = review['safetyRatingDto']['rainSnowTraction']
                except:
                    rainSnowTraction = ''


                try:
                    safetyRating = review['safetyRatingDto']['safetyRating']
                except:
                    safetyRating = ''

                try:
                    activeSafety = review['safetyRatingDto']['activeSafety']
                except:
                    activeSafety = ''


                try:
                    headlights = review['safetyRatingDto']['headlights']
                except:
                    headlights = ''


                try:
                    safetyRating = review['safetyRatingDto']['safetyRating']
                except:
                    safetyRating = ''

                try:
                    instrumentation = review['interiorRatingDto']['instrumentation']
                except:
                    instrumentation = ''


                try:
                    interiorDesign = review['interiorRatingDto']['interiorDesign']
                except:
                    interiorDesign = ''

                try:
                    qualityOfMaterials = review['interiorRatingDto']['qualityOfMaterials']
                except:
                    qualityOfMaterials = ''

                try:
                    logicOfControls = review['interiorRatingDto']['logicOfControls']
                except:
                    logicOfControls = ''

                try:
                    interiorRating = review['interiorRatingDto']['interiorRating']
                except:
                    interiorRating = ''

                try:
                    cargoStorage = review['interiorRatingDto']['cargoStorage']
                except:
                    cargoStorage = ''

                try:
                    acceleration = review['performanceRatingDto']['acceleration']
                except:
                    acceleration = ''

                try:
                    roadHolding = review['performanceRatingDto']['roadHolding']
                except:
                    roadHolding = ''

                try:
                    braking = review['performanceRatingDto']['braking']
                except:
                    braking = ''

                try:
                    performanceRating = review['performanceRatingDto']['performanceRating']
                except:
                    performanceRating = ''

                try:
                    shifting = review['performanceRatingDto']['shifting']
                except:
                    shifting = ''

                try:
                    steering = review['performanceRatingDto']['steering']
                except:
                    steering = ''


                new_record = [text_review, userRating, styleId, id, purchaseDate, pricePaid, odometerMiles, title, commentsCount, averageRating,  rearSeats, frontSeats, comfortRating, gettingInOut,
                       rideComfort, noiseAndVibration, authorName, climateControl, bluetooth, usbPorts, technologyRating, navigation, parkingAids, outwardVisibility, rainSnowTraction, safetyRating,
                       activeSafety, headlights, safetyRating, instrumentation, interiorDesign, qualityOfMaterials, logicOfControls, interiorRating, cargoStorage, acceleration, roadHolding, braking,
                       performanceRating, shifting, steering]

                records.append(new_record)

        except Exception, e:
            print e




# print json


# loop through articles and add them into a list

# save articles to a dataframe
records_df = pd.DataFrame(records, columns= ['text_review', 'userRating', 'styleId', 'id', 'purchaseDate', 'pricePaid', 'odometerMiles',
                                              'title', 'commentsCount', 'averageRating', ' rearSeats', 'frontSeats',
                                              'comfortRating', 'gettingInOut', 'rideComfort', 'noiseAndVibration',
                                              'authorName', 'climateControl', 'bluetooth', 'usbPorts', 'technologyRating',
                                              'navigation', 'parkingAids', 'outwardVisibility', 'rainSnowTraction', 'safetyRating',
                                              'activeSafety', 'headlights', 'safetyRating', 'instrumentation', 'interiorDesign',
                                              'qualityOfMaterials', 'logicOfControls', 'interiorRating', 'cargoStorage', 'acceleration',
                                              'roadHolding', 'braking', 'performanceRating', 'shifting', 'steering'])

try:
    print "started excel creation"
    records_df.to_excel('edmund_sample_subaru.xlsx')
    print "excel created"
except Exception,e:
    print e