from google_images_search import GoogleImagesSearch
import os
import sys
from dotenv import load_dotenv
load_dotenv()


KEY = os.getenv('GOOGLE_API_KEY')
CX = os.getenv('GOOGLE_CX')


def parsequery(text):
    for i in text:
        if i.isalpha():
            pass
        elif(i == ' '):
            text = text.replace(i, ' ')
        else:
            text = text.replace(i, '')
    return text


def getGoogleImage(query, filename):
    gis = GoogleImagesSearch(
        KEY, CX)

    # query should only consist of only alphabetical characters

    print(query)
    _search_params = {
        'q': f'{query}',
        'num': 5,
        'fileType': 'jpg|png|jpeg',
        'safe': 'off',
    }

    gis.search(search_params=_search_params)
    
    if(len(gis.results()) == 0):
        # search again with just the first word
        query = query.split(' ')[0]
        _search_params = {
            query: f'{query}',
            'num': 5,
            'fileType': 'jpg|png|jpeg',
            'safe': 'medium',
        }
        
        gis.search(search_params=_search_params)
    
        if(len(gis.results) == 0):  
            print("No results found")
            return ; 
    
    img = gis.results()[0]

    for i in gis.results():
        if i.url.split('.')[-1] == 'jpg' or i.url.split('.')[-1] == 'jpeg' or i.url.split('.')[-1] == 'png':
            img = i
            break
    
    img.download('./images/')
    # resize the image to 512 but keep the aspect ratio

    # rename the saved image file to query
    
    os.rename(img.path, f"./images/{filename}.jpg")
 
    print("saved Image to ", img.path)

if __name__ == "__main__":
    getGoogleImage("google.com",23)
    # print("key: ", KEY, " CX : ", CX); 
