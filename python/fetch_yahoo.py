import yfinance as yf
import json
import os,sys
from pprint import pprint

def fetch_yfinance(ticket):
  ticket = yf.Ticker(ticket)
  return ticket.info

def helloworld123231():
  ctx = XSCRIPTCONTEXT.getComponentContext()
  serviceManager = ctx.ServiceManager
  desktop = XSCRIPTCONTEXT.getDesktop()
  doc = desktop.getCurrentComponent()
  sheets = doc.getSheets() #XSpreadSheets
  sheet = sheets.getByIndex(0)

  # Introducimos texto
  xCell = sheet.getCellByPosition(1, 3)

  # xCell.setValue("123321")
  info_json = fetch_yfinance('MSFT')
  xCell.setString(info_json['open'])

  # xCell.insertString(textCursor, json.dumps(msft.info), False)
