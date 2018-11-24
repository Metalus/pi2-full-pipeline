#!/bin/python
import locale

locale.setlocale(locale.LC_ALL, 'C')
from tesserocr import PyTessBaseAPI, RIL, iterate_level
import sys
import cv2
import numpy as np
from PIL import Image
from crop import cropa
import unidecode
import os
import time
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def processa(path='imagem.jpg'):

    locale.setlocale(locale.LC_ALL, 'C')
    with PyTessBaseAPI(lang='por') as api:
        start_time = time.time()
        print('pre')
        c = cropa(path)
        print('pro')
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
        api.Recognize()
        ri = api.GetIterator()
        level = RIL.TEXTLINE
        lines = []
        #print(' '.join(word for word in api.AllWords()))
        for r in iterate_level(ri, level):
            symbol = r.GetUTF8Text(level)  # r == ri
            conf = r.Confidence(level)
            #print(symbol, end='')
            if symbol.strip():
                lines.append(symbol.strip())
        #print(api.GetUTF8Text())
        #print(lines)
        text = '\n'.join(lines)
        print(text)
        #text = api.GetUTF8Text()
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        if text != None:
            #text = unidecode.unidecode(text)
            file = open('textscanner.txt', 'w')
            file.write(text)
            file.close()
            os.system('python2 translator.py textscanner.txt')
            print("Elapsed time: {}".format(time.time() - start_time))

if __name__ == '__main__':
    processa()
