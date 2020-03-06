# This code downloads Astronomy picture of the day from Nasa (current date through June 16, 1995).
# The code, after downloading photos, will categorize them and save it into different folders
# Description for each photos will be also saved as a txt file in the same folder with the pictures

def get_date():
    # This function calculates how many days passed since the day the first Astronomy picture of the day was posted
    # Number of days from June 16, 1995 to current date is returned

    tday = dt.date.today()
    time_NASA = time_NASA = dt.date(1995, 6, 16)
    POFTD_time = tday - time_NASA
    POFTD_time = POFTD_time.days

    return POFTD_time

def date(POFTD_time):
    # This function gets 'date' - one of the query parameters for NASA API
    n = 0
    for i in range(POFTD_time+1):
        tdelta = dt.timedelta(days=n)
        date_i = (dt.date(1995,6, 16) + tdelta)
        n = n + 1
        print(date_i)

def resolution():
    # Hd or Sd resolution

    resolution = ''
    while resolution != '1' and resolution != '2':
        print("Press 1 to download sd resolution images and press 2 to download hd resolution images: ", end='')
        resolution = input()
    return resolution

def create_directories(objects):
    # This function will create folders for images to be downloaded
    for j in objects:
        os.makedirs('/Users/kihyunlee/Desktop/University/POFTD/%s' %j, exist_ok=True) #User should be able to put their name

def specific_image():
    # This function will check whether user wants to search for a particular astronomical object
    mode = ''
    while mode != '1' and mode != '2':
        print('Are you looking for something specific? If you are press 1. If you want to download all the images press 2: ', end = '')
        mode = input()

    if mode == '1':
        print('What are you looking for? Please enter keywords you\'re looking for (You can search for multiple keywords (e.g. Mars Earth) : ', end = '')
        user_response = input().split()
        print(user_response)
        print(type(user_response))
        return user_response

    if mode == '2':
        Astronomical_objects = ['Solar System', 'Oort cloud', 'Meteoroid', 'Micrometeoroid', 'Meteor', 'Moons', 'Moon',
                                'Asteroids',
                                'Synestia', 'Ring', 'Comets', 'Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',
                                'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Black hole',
                                'Neutron star', 'Pulsar', 'Quasi-star', 'Quassar', 'Dark matter']
        print(Astronomical_objects)
        return Astronomical_objects


def downloadURL(nDays, resolution, objects):
    # The function will extract download url from Json data obtained from NASA's API
    # Using title and the explanation written, photos will be categorized and saved into different folders


    n = 0
    downloaded = 0
    missed = 0
    for i in range(nDays - 9000):
        tdelta = dt.timedelta(days=n)
        date_i = (dt.date(1995,6, 16) + tdelta)
        url = 'https://api.nasa.gov/planetary/apod?date=' + str(date_i) + '&api_key=AfAB04wLz3S5Vz9fHo3zl6KCytpJDqIyv3Ra6rjW'
        response = requests.get(url)
        response.raise_for_status()
        jsonData = json.loads(response.text)

    # Extract a download url, title of a photo, and explanation by NASA
        if resolution == '1':
            downloadURL = jsonData["url"]
        else:
            downloadURL = jsonData["hdurl"]
        title = jsonData["title"]
        explanation = jsonData['explanation']

    # Measure how long it took to download all the images
        #start_time = time.time

    # Keyword_list will append a word if the word is inside of user created list or category list
        keyword_list = []
        for j in objects:
            if j in title:
                keyword_list.append(j)
            if j in explanation:
                keyword_list.append(j)
        print(keyword_list)
        print(type(keyword_list))
        print(len(keyword_list))
    # Counting which word appears the most
    # 0th index of this list will be the word that appeared most frequently in the title and the description
    # the 1st index of the list will be number of appearance
        word_count = [0, 0]
        for j in range(len(keyword_list)):
            if word_count[1] < keyword_list.count(keyword_list[j]):
                nth = [keyword_list[j], keyword_list.count(keyword_list[j])]


        if j in keyword_list:
            wget.download(downloadURL, '/Users/kihyunlee/Desktop/University/POFTD/%s' %j)
            downloaded = downloaded + 1

        else:
            wget.download(downloadURL, '/Users/kihyunlee/Desktop/University/POFTD/Extras')
            extras.write("%s\n" %title)
            missed = missed + 1

        print("You downloaded %f files" % downloaded)
        print("You missed %f files" % missed)

        if i < 1:
            n = n + 4
        else:
            n = n + 1

        #if n == ndays:
            #time_took = time.time - start_time
            #print(time_took)
            #break

# Code starts from here

import json, requests, pprint, time, datetime as dt, wget, os


Astronomical_objects = ['Solar System', 'Oort cloud',  'Meteoroid', 'Micrometeoroid', 'Meteor', 'Moons', 'Moon', 'Asteroids',
                        'Synestia', 'Ring','Comets', 'Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Black hole',
                        'Neutron star', 'Pulsar', 'Quasi-star', 'Quassar' , 'Dark matter']


extras = open("/Users/kihyunlee/Desktop/University/POFTD/extras.txt", "w")
os.makedirs("/Users/kihyunlee/Desktop/University/POFTD/Extras", exist_ok=True)




numberDays = get_date()
user_dictionary = specific_image()
resolution = resolution()
create_directories(user_dictionary)
downloadURL(numberDays, resolution, user_dictionary)






