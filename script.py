import requests
import os
import time
from charbychar import processa
import scanner
from recorder import processa_som
import unidecode

while True:
    if os.path.exists('imagem.jpg'):
        print("Processing captured image...")
        text = scanner.processa('imagem.jpg')
        os.system('rm -rf imagem.jpg')
    else:
        try:
            a = requests.get('https://brailleprinter.herokuapp.com/webapp/downloadfile', allow_redirects=True)
        except requests.exceptions.ConnectionError:
            print('Trying to reconnect...')
            time.sleep(10)
            continue
        text = None
        if a.status_code == 404:
            print('Waiting for new request... (Sleeping for 10 seconds)')
        else:
            start_time = time.time()
            try:

                if str(a.headers['content-disposition']).split('.')[1] in ['wav', 'm4a', 'ogg', 'mp3']:
                    print('Audio saved!')
                    ext = str(a.headers['content-disposition']).split('.')[1]
                    open('tmp.{}'.format(ext), 'wb').write(a.content)
                    print('Processing audio...')
                    text = processa_som('tmp.{}'.format(ext))
                elif '.pdf' in str(a.headers['content-disposition']):
                    print('PDF Saved!')
                    open('tmp.pdf', 'wb').write(a.content)
                elif '.txt' in str(a.headers['content-disposition']):
                    open('tmp.txt', 'wb').write(a.content)
                    text = open('tmp.txt', 'rb').read().decode()
                elif str(a.headers['content-disposition']).split('.')[1] in ['png', 'jpg', 'jpeg']:
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
                else:
                    print("File not supported. Try again.")
                    text = None
            except:
                pass
    
    
    if text != None:
        text = unidecode.unidecode(text)
        file = open('text.txt', 'w')
        file.write(text)
        file.close()
        os.system('python2 translator.py text.txt')
        print("Elapsed time: {}".format(time.time() - start_time))

    os.system('rm -rf imagem.* tmp.* arquivo.* audio_file.*')
    time.sleep(10)
