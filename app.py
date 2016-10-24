#!/usr/bin/env python
import ntpath
import os
import logging

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/var/www/stream/uploads/myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

logger.info("starting..")
targetdir = "/var/www/stream/uploads/"


def application(env, start_response):
    '''
    this is to rename the file that got written by nginx to the original name
    '''
    try:
        sourcepath = env["HTTP_X_FILE"]
        filename = ntpath.basename(env["REQUEST_URI"])
        targetpath = targetdir + filename
    except:
        errhandler('unable to get request-uri/cache name', start_response)

    try:
        o=open(targetpath, "w")
    except:
        errhandler('unable to open targetpath', start_response)
    try:
        f=open(sourcepath)
    except:
        errhandler('unable to open sourcepath', start_response)
    ## this is kinda hacky, do remove the webkit boundy foo
    numline=4 #4 lines to skip for header thingy
    p=""
    for i in range(numline):
        f.next()
    for line in f:
        if p:
            o.write(p)
        p=line
    f.close()
    o.close()
    start_response('200 OK', [('Content-Type','text/html')])
    html = "<h1>Sucessfully uploaded " + filename + "</h1>\n"
    return html

def errhandler(errmsg, start_response):
    logger.error(errmsg)
    start_response('500 INTERNAL SERVER ERROR', [('Content-Type','text/html')])
    html = errmsg
    return html

