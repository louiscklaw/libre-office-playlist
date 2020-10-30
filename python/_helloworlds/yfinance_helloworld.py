import yfinance as yf
import json

def fetch_yfinance(ticket):
  ticket = yf.Ticker(ticket)
  return ticket.info

def helloworld():
  return 'helloworld'

def hello_yfinance():
  ctx = XSCRIPTCONTEXT.getComponentContext()
  serviceManager = ctx.ServiceManager
  desktop = XSCRIPTCONTEXT.getDesktop()
  doc = desktop.getCurrentComponent()
  sheets = doc.getSheets() #XSpreadSheets
  sheet = sheets.getByIndex(0)

  # Introducimos texto
  xCell = sheet.getCellByPosition(1, 3)

  xCell.setValue(json.dumps(fetch_yfinance().info))
  # xCell.insertString(textCursor, json.dumps(msft.info), False)
