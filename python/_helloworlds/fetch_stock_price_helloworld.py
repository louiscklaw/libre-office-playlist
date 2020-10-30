import yfinance as yf
import json
import os,sys
from pprint import pprint

# https://wiki.documentfoundation.org/Macros/Python_Guide/My_first_macro
sys.path.append('/home/logic/.config/libreoffice/4/user/Scripts/python')

import config

def _fetch_yfinance(ticket):
  ticket = yf.Ticker(ticket)
  return ticket.info

def helloworld123231():
  ctx = XSCRIPTCONTEXT.getComponentContext()
  serviceManager = ctx.ServiceManager
  # desktop = XSCRIPTCONTEXT.getDesktop()
  # doc = desktop.getCurrentComponent()
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
  xCell.setString(_fetch_yfinance('MSFT')['open'])

  xCell = status_sheet.getCellByPosition(1, 4)
  xCell.setString('done')

  doc.getCurrentController().setActiveSheet(helloworld_sheet)