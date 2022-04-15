# -*- coding = utf-8 -*-
from bs4 import BeautifulSoup
import sqlite3
import re
import xlwt
import urllib
import sys

def main():
    url = "https://movie.douban.com/top250?start="
    datalist = getData(url)
    savepath = ".\\豆瓣电影TOP250.xls"


def getData(url):
    datalist = []
    return datalist

def saveData(savepath):



if __name__ == "__main__":


