"""This module is used to get the omdb api data for the movie name passed as parameter
along with resizing the image for each title to display as a pop up in the GUI"""

import omdb
import requests
import json
import os
from PIL import Image,ImageFilter
from tkinter import messagebox
import tkinter as tk
import re


from resizeimage import resizeimage


# if creating a new client instance
# client = omdb.OMDBClient(apikey=api_k)
def moviedata(name):
    omdbapi = 'e59e6a35'
    try:
    # if using the module level client
        omdb.set_default('apikey', omdbapi) #setting up the api with api key
        val = omdb.title(name)
        if os.path.exists(os.path.join(os.getcwd(),'movieposter',name+'.jpg')) is True:
            return val
        else:
            img_link = requests.get(val['poster']) #to get the poster link
            print(val['poster'])
            # # img_link = requests.get()
            if img_link.status_code == 200:
                with open(os.path.join(os.getcwd(),'movieposter',name+'.jpg'),'wb') as imgfile:
                    imgfile.write(img_link.content)
                    print('Done')
                image1 = Image.open(os.path.join(os.getcwd(),'movieposter',name+'.jpg'))
                # image1.show()
                cover = resizeimage.resize_cover(image1, [177, 266]) #resizing the cover
                cover.save(os.path.join(os.getcwd(),'movieposter',name+'.jpg'), image1.format)
                return val
            else:
                return val
                # tk.messagebox.showerror('Movie Not Found','The name was too long or unreqnizable or is in foreign language')
    except:
        return False

    # os.system('taskkill /f /im python.exe')


def imagedownload(name):
    omdbapi = 'e59e6a35'
    omdb.set_default('apikey', omdbapi) #setting up the api with api key
    val = omdb.title(name)

    if os.path.exists(os.path.join(os.getcwd(),'movieposter',name+'.jpg')) is True:
        print('Image already exists')
    else:
        img_link = requests.get(val['poster']) #to get the poster link

        # print(obj.sub(r'\1_V1_.jpg', s))
        # # img_link = requests.get()
        if img_link.status_code == 200:
            with open(os.path.join(os.getcwd(),'movieposter',name+'.jpg'),'wb') as imgfile:
                imgfile.write(img_link.content)
                print('Image Downloaded')
            image1 = Image.open(os.path.join(os.getcwd(),'movieposter',name+'.jpg'))
            # image1.show()
            cover = resizeimage.resize_cover(image1, [177, 266]) #resizing the cover
            cover.save(os.path.join(os.getcwd(),'movieposter',name+'.jpg'), image1.format)

    if os.path.exists(os.path.join(os.getcwd(),'movieposter',name +'large'+'.jpg')) is True:
        print('large Image exists')
    else:
        s = val['poster']
        obj=re.compile(r'(.+\.)(_V1_.+)')
        large_img = obj.sub(r'\1_V1_.jpg', s)
        large_img_link = requests.get(large_img)
        if large_img_link.status_code == 200:
            with open(os.path.join(os.getcwd(),'movieposter',name +'large'+'.jpg'),'wb') as large_img:
                large_img.write(large_img_link.content)
                print('large img downloaded')
        else:
            print('Network Error')


# imagedownload('12 angry men')
def blurimg(name):
    if os.path.exists(os.path.join(os.getcwd(),'movieposter',name +'blur'+'.jpg')) is True:
        print('Blur image exists')
    else:
        img = Image.open(os.path.join(os.getcwd(),'movieposter',name +'large'+'.jpg'))
        blurred_img = img.filter(ImageFilter.BoxBlur(5))
        blurred_img.save(os.path.join(os.getcwd(),'movieposter',name +'blur'+'.jpg'))
# blurimg('12 angry men')
# s =
# obj=re.compile(r'(.+\.)(_V1_.+)')
# print(obj.sub(r'\1_V1_.jpg', s))

# img_link = 'https://m.media-amazon.com/images/M/MV5BOWE4ZDdhNmMtNzE5ZC00NzExLTlhNGMtY2ZhYjYzODEzODA1XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg'
# s = requests.get(img_link)
# print(s.status_code)

# with open(os.path.join(os.getcwd(),'movieposter','seven'+'large'+'.jpg'),'wb') as imgfile:
#     imgfile.write(s.content)
#     print('done')
# image1 = Image.open(os.path.join(os.getcwd(),'movieposter','seven'+'large'+'.jpg'))
#         # image1.show()
# cover = resizeimage.resize_cover(image1, [600, 600]) #resizing the cover
# cover.save(os.path.join(os.getcwd(),'movieposter','seven'+'large'+'.jpg'), image1.format)


# img = Image.open(os.path.join(os.getcwd(),'movieposter','seven'+'large'+'.jpg'))
# blurred_img = img.filter(ImageFilter.BoxBlur(3))
# blurred_img.save(os.path.join(os.getcwd(),'movieposter','seven'+'blur2'+'.jpg'))


