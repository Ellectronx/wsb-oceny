#!/usr/bin/env python
#
# Author: Tomas (www.lisenet.com)
#
# CHANGELOG
#
# [v0.1] - 2013
# Initial release, script uses one hardcoded URL
#

import os
import time
import signal
import hashlib
import subprocess

from selenium import webdriver
from bs4 import BeautifulSoup

import db
from sendEmail import *

def main():

    killXvfb()
    os.system('/usr/bin/Xvfb :11 -ac -screen 0 1024x768x24 &')
    os.environ['DISPLAY'] = ':11.0'

    #URL 
    url = "https://portal.wsb.pl/group/gdansk/oceny-wstepne"

    profile = webdriver.FirefoxProfile()
    # Set a user agent string to help parse webserver logs easily
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 selenium_xvfb.py")
    browser = webdriver.Firefox(profile)
    browser.get(url)
    time.sleep(1)

    # DEFINE USERNAME & PASSWORD FIELDS
    user = browser.find_element_by_name("username")
    password = browser.find_element_by_name("password")
    # Clear the input fields
    user.clear()
    password.clear()
    user.send_keys("gax30800")
    password.send_keys("Electron26")
    
    #PRESS LOGIN BUTTON
    browser.find_element_by_id("login_button").click()

    time.sleep(5)
    browser.get(url)
    html = browser.page_source

    
    #with open('plik.html', 'r') as myfile:
    #    html = myfile.read()

    soup = BeautifulSoup(html,features="lxml")

    # create a database connection
    conn = db.prepareTablesAndConnection()


    table = soup.find("table", { "class" : "dataTable" })
    for row in table.findAll("tr"):
        t=()
        cells = row.findAll("td")
        for c in cells:
            t=t+(c.find(text=True).strip(),)
        try:
            h = t[0] + t[1] + t[2]
            t=( hashlib.md5(h.encode()).hexdigest(),) + t
            #print(t)
            #db.insert_oceny(conn,"oceny",t)
            db.insert_oceny(conn,"oceny_nowe",t)

            
        except IndexError:
            continue
        except:
            raise
    """
    rows = db.select_oceny(conn,"oceny")
    print(rows)

    print("\n\n\n\n\n\n")

    rows = db.select_oceny(conn,"oceny_nowe")
    print(rows)
    """

    #rows_diff = db.select_oceny(conn,"oceny_nowe")
    print("\n\n\nROW DIFF:")
    rows_diff = db.select_diff(conn)
    #print(rows_diff)
    ID=[]
    for row in rows_diff:
        strx=""
        for txt in row:
            strx = strx + txt + " | "
        ID.append(row[0])
        print(strx)

    print(ID)
    #datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    db.oceny_copy(conn)
    db.query(conn,"DELETE FROM oceny_nowe;")

    conn.commit()
    conn.close()
    #sendEmail("TEST","auto@danilewicz.com","l.danilewicz@gmail.com","TEST lalala")


    file = open("plik.html","w") 
    file.write(html) 
    file.close() 
    # Keep the page loaded for 8 seconds
    time.sleep(8)

    # Log out
    browser.find_element_by_link_text('Wyloguj')
    time.sleep(2)
    #browser.find_element_by_id("dialog_button_ok").click()
    #time.sleep(1)

    browser.delete_all_cookies()
    browser.close()
    killXvfb()

def killXvfb():
    p = subprocess.Popen(['ps', '-A'],
                           shell=True,
                           stdout=subprocess.PIPE,
                           universal_newlines=True).communicate()[0]
    #out, err = p.communicate()
    #print(p.splitlines())

    for line in p.splitlines():
        if 'Xvfb' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)


if __name__ == '__main__':
    main()