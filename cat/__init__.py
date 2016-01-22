#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2016, René Tanczos <gravmatt@gmail.com> (Twitter @gravmatt)
The MIT License (MIT)

cat is a amazing modul to get cat images. This Project won't be
posible without the great Cat API (http://thecatapi.com).
Big thanks!

Project on github https://github.com/gravmatt/random-cat
"""

import urllib, uuid, os, sys

url = 'http://thecatapi.com/api/images/get'

def getCat(directory=None, filename=None, format='png'):
    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), format)
    savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    downloadlink = url + '?type=%s' % format
    urllib.urlretrieve(downloadlink, savefile)
    return savefile


def main():
    format = 'png'
    filename = None
    directory = None
    if(len(sys.argv) > 1):
        format = sys.argv[1]
        if(not format in ['png', 'jpg', 'gif']):
            sys.stdout.write('Wrong format! Only png, jpg or gif')
            return
    if(len(sys.argv) > 2):
        filename = sys.argv[2]
        directory = os.path.sep.join(filename.split(os.path.sep)[:-1])
        filename = os.path.basename(filename).split('.')[0]
    sys.stdout.write(getCat(directory, filename, format))

if(__name__ == '__main__'):
    main()
