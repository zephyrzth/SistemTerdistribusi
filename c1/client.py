import Pyro4
import base64
import json
import sys

namainstance = sys.argv[1] or "fileserver"

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    return fserver

if __name__=='__main__':
    f = get_fileserver_object()
    #f.create('coba.txt')
    f.update('coba.txt', content = open('coba.txt','rb+').read() )
    f.create('coba2.txt')

    #f.create('slide2.pptx')
    #f.update('slide2.pptx', content = open('slide2.pptx','rb+').read())

    print(f.list())
    d = f.read('coba.txt')
    #kembalikan ke bentuk semula ke dalam file name slide1-kembali.pdf
    open('coba-kembali.txt','w+b').write(base64.b64decode(d['data']))

    #k = f.read('slide2.pptx')
    #kembalikan ke bentuk semula ke dalam file name slide2-kembali.pptx
    #open('slide2-kembali.pptx','w+b').write(base64.b64decode(k['data']))


