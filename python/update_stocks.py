import json
import os,sys
from pprint import pprint

import yfinance as yf

sys.dont_write_bytecode = True

# https://wiki.documentfoundation.org/Macros/Python_Guide/My_first_macro
sys.path.append('/home/logic/.config/libreoffice/4/user/Scripts/python')
sys.path.append('/home/logic/.config/libreoffice/4/user/Scripts/python/_qqstocks')

import config

# import _qqstocks.marketIndex

from marketIndex import selfTestHelloworld


def main():
  ctx = XSCRIPTCONTEXT.getComponentContext()
  serviceManager = ctx.ServiceManager
  doc = XSCRIPTCONTEXT.getDocument()

  sheets = doc.getSheets() #XSpreadSheets
  status_sheet = sheets.getByName('status')
  helloworld_sheet = sheets.getByName('helloworld')

  xCell = status_sheet.getCellByPosition(1, 3)
  xCell.setString('init script')

  xCell = helloworld_sheet.getCellByPosition(1, 3)
  # info_json = _fetch_yfinance('MSFT')
  xCell.setString(config.HELLOWORLD)

  xCell = helloworld_sheet.getCellByPosition(1,4)
  temp = selfTestHelloworld()
  xCell.setString('')
  xCell.setString(temp)

  xCell = status_sheet.getCellByPosition(1, 4)
  xCell.setString('done')

  doc.getCurrentController().setActiveSheet(helloworld_sheet)