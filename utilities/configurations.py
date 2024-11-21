import configparser
import json
import os

import mysql.connector
from selenium.webdriver.chrome import webdriver

from utilities.resources import WebResources


def getBrowser():
    driver=webdriver.chrome()
    driver.get(WebResources.starportal)

def getConfig():
    config = configparser.ConfigParser()
    config.read('BackEndAutomation/utilities/properties.ini')
    return config


# connect_config = {
#     'user' : getConfig()['SQL']['user'],
#     'password' : getConfig()['SQL']['password'],
#     'host' : getConfig()['SQL']['host'],
#     'database' :getConfig()['SQL']['database'],
# }


def getPassword():
    return "Srinath19830G"


def getConnection():
    # try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successful")
            return conn
    # except Error as e:
    #     print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

settings = None


# def load_settings():
#     global settings
#     with open("Data/settings.json",'settings.json') as f:
#         settings = json.load(f)
#
#
# load_settings()