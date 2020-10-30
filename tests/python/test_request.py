import requests
import json

ctx = XSCRIPTCONTEXT.getComponentContext()
serviceManager = ctx.ServiceManager
desktop = XSCRIPTCONTEXT.getDesktop()
doc = desktop.getCurrentComponent()
sheets = doc.getSheets() #XSpreadSheets
sheet = sheets.getByIndex(0)

def HelloRequest( ):
    """Prints the string 'Hello World(in Python)' into the current document"""
    r = requests.get('https://api.github.com/events')

    # xCell.setValue(json.dumps([1,2,3,4,5,]))
    xCell = sheet.getCellByPosition(1, 3)
    textCursor = xCell.createTextCursor() # xCell implementa XText

    xCell.insertString(textCursor, json.dumps(r.json()), False)


    # doc.storeAsURL("file:///home/logic/_del/testsheet.ods", ())

    return None

# vim: set shiftwidth=4 softtabstop=4 expandtab:
