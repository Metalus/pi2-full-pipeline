#!/bin/python
from tesserocr import PyTessBaseAPI, RIL, iterate_level
import sys
import cv2
import numpy as np
from PIL import Image
from crop import cropa


def processa(path):
    with PyTessBaseAPI(lang='por') as api:
        c = cropa(path)
        if '.png' in path:
            api.SetImageFile('tmp.png')
        elif '.jpeg' in path:
            api.SetImageFile('tmp.jpeg')
        else:
            api.SetImageFile('tmp.jpg')

        api.SetVariable("save_blob_choices", "T")
        
        """"
        #ima = cv2.imread(path)
        #ima = cv2.resize(ima, (1000,900))
        #api.SetImage(Image.fromarray(ima))
        lines = api.GetTextlines()
        print(list(lines))
        for im in lines:
            #ia= cv2.rectangle(ima,(im[1]['x'], im[1]['y']),(im[1]['x'] + im[1]['w'],im[1]['y'] + im[1]['h']),(0,255,0),3)
            #cv2.imshow("kk", ia)
            #cv2.waitKey(0)
            api.SetRectangle(im[1]['x'], im[1]['y'], im[1]['w'], im[1]['h'])
            api.Recognize()
            print(api.GetUTF8Text())
        """
        print(' '.join(word for word in api.AllWords()))
        api.Recognize()
        ri = api.GetIterator()
        level = RIL.TEXTLINE
        for r in iterate_level(ri, level):
            symbol = r.GetUTF8Text(level)  # r == ri
            conf = r.Confidence(level)
            print(symbol, end='')
        #print(api.GetUTF8Text())
        return api.GetUTF8Text()
