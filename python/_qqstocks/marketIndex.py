import os,sys
from pprint import pprint

import requests
from config import *

def parseIndex(result_from_qq_stock):
  temp = result_from_qq_stock.split('~')
  return temp

def getHSI():
  r = requests.get('https://qt.gtimg.cn/q=s_r_hkHSI')
  return 'parseIndex(r.text)'

def getSZ399001():
  r = requests.get('https://qt.gtimg.cn/q=s_sz399001')
  return parseIndex(r.text)

def getSH000001():
  r = requests.get('https://qt.gtimg.cn/q=s_sh000001')
  return parseIndex(r.text)


def helloworld_get_ticket():
  print('helloworld get ticket')

def selfTestHelloworld():
  return '_qqstocks.selfTestHelloworld'
