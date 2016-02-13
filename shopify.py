# -*- coding: utf-8 -*-
import mechanize
import urllib
import cookielib
import BeautifulSoup
import html2text
import re
import sys
import StringIO
from urllib2 import HTTPError
import os
import time
import webbrowser

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)


br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]
loop = 1

#url = "http://shop.yeezysupply.com/cart/13696467011:1"
#url = "http://justdon.com/cart/1061774561:1"
url = "http://kithnyc.com/cart/14036578247:1"
#url = "http://shop.cncpts.com/cart/1145615992:1"





print'............................................................'
print'......77777......................................77777......'
print'.....777777...............:?+++??...............777777......'
print'...7 777777...........??+++++++++++++...........,7777777,...'
print'..777777777.........+++++++++++++++++++~........,77777777 ..'
print'..7777777777?.....?++.+?++++++++++++++.++......7777777777 ..'
print'...777.: 77777...++:.+.??.++++++++++.++.++...7777777.7777...'
print'.........777777.++++++++++++++++++++:++?~++..77777..........'
print'...........777.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~. 77~...........'
print'............,7.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.7.............'
print'..............:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~...............'
print'.......?+????+++??++++++++++++++++++??+++++++?++??+??.......'
print'.......??????????????????????????????????????????????.......'
print'..............:7777777 7777777777777777777777...............'
print'...............7777 +......777777......777777...............'
print'...............77777........777 ........7777................'
print'................777,........777 ........777.................'
print'.................777.......77777........77..................'
print'..................777.....7777777?....I 7...................'
print'....................7777 777...7777 777.....................'
print'......................=777777 7777777.......................'
print'.....................777...........=77.~....................'
print'..................77.777I7 77.77 I7777+77...................'
print'................777.77...7777.7777.:.,7.777.................'
print'...............7777.7 77.77~...:77.777 .77777...............'
print'........777..777777.7..7.7777.7777.77...777777..77 .........'
print'.......7777777777 ..7777....+.I:...?777..77777777777~.......'
print'......,777777777....:777777777777777777....7777777777.......'
print'.......+7777777~.....7777777777777777 ......77777777........'
print'..........777777......777777777777777......777777...........'
print'..........:77777........77777777777........777777...........'
print'............,~...............................++.............\n'





print "Running..."
print "Target: " + str(url.split('//')[1].split('.com')[0].upper())
print "Using variant: " + str(url[:-2].split("/")[len(url[:-2].split("/"))-1])+ "\n"
while (1==1):
    try:
        

        
        br.open(str(url))

        '''
        for f in br.forms():
            print f

        '''
        if str(url) in str(br.geturl()):
            print "Try: " + str(loop) + " - MOST LIKELY OOS =( ..."
            print "--> " + str(br.geturl()) +"\n"
                
        
        #br.select_form(nr=1)
        redirect=str(br.geturl())

	
        if "stock_problems" in str(br.geturl()):
            print "Try: " + str(loop) + " - ATC NOT LIVE YET..."
            print "--> " + str(br.geturl()) +"\n"
            loop+=1
        else:
	    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 1, 250))
            print "Try: " + str(loop) + " - Success!!! LEMME GET THAT CART FOR YOU"
            webbrowser.open(str(redirect))
            print "--> " + str(br.geturl()) +"\n"
            #Maybe implement a -4 to variant to atc next size down or up next time
            #redeclare url here.
            time.sleep(10)
            url = "http://kithnyc.com/cart/14036578247:1"
            loop+=1
    
    except:
        if str(url) in str(br.geturl()):
            print "Try: " + str(loop) + " - MOST LIKELY OOS =( ..."
            print "--> " + str(br.geturl()) +"\n"
        else:
            print "Try: " + str(loop) + " - IDK BRUH"
            print "--> " + str(br.geturl())+"\n"
        #time.sleep(1)
        loop+=1
        continue
    
#os.system("pause")



