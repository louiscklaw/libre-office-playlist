import json
import os,sys
from pprint import pprint

import yfinance as yf

sys.path.append('/home/logic/.config/libreoffice/4/user/Scripts/python')
sys.dont_write_bytecode = True

from test_func_return import *

def helloworld():
  ctx = XSCRIPTCONTEXT.getComponentContext()
  serviceManager = ctx.ServiceManager
  doc = XSCRIPTCONTEXT.getDocument()

  sheets = doc.getSheets() #XSpreadSheets
  status_sheet = sheets.getByName('Sheet1')
  helloworld_sheet = sheets.getByName('Sheet2')

  xCell = status_sheet.getCellByPosition(1, 3)
  temp = self_test()
  xCell.setString('')
  xCell.setString(temp)
