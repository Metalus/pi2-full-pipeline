import requests
import os
import time
from charbychar import processa
from recorder import processa_som
import unidecode

while True:
    a = requests.get('https://brailleprinter.herokuapp.com/webapp/downloadfile', allow_redirects=True)

    text = None
    if a.status_code == 404:
        print('Waiting for new request... (Sleeping for 10 seconds)')
    else:
        start_time = time.time()
        if '.wav' in str(a.headers['content-disposition']):
            print('Audio saved!')
            open('tmp.wav', 'wb').write(a.content)
            print('Processing audio...')
            text = processa_som('tmp.wav')
        elif '.pdf' in str(a.headers['content-disposition']):
            print('PDF Saved!')
            open('tmp.pdf', 'wb').write(a.content)
         elif '.txt' in str(a.headers['content-disposition']):
            open('tmp.txt', 'wb').write(a.content)
            text = open('tmp.txt', 'rb').read().decode()
        else:
            # processamento de imagem
            print('Image saved!')
            print('Processing image...')

            if '.png' in str(a.headers['content-disposition']):
                open('arquivo.png', 'wb').write(a.content)
                text = processa('arquivo.png')
            elif '.jpeg' in str(a.headers['content-disposition']):
                open('arquivo.jpeg', 'wb').write(a.content)
                text = processa('arquivo.jpeg')
            else:
                open('arquivo.jpg', 'wb').write(a.content)
                text = processa('arquivo.jpg')

    if text != None:
        text = unidecode.unidecode(text)
        file = open('text.txt', 'w')
        file.write(text)
        file.close()
        os.system('python2 translator.py text.txt')
        print("Elapsed time: {}".format(time.time() - start_time))


    time.sleep(10)
