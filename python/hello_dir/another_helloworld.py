
def HelloworldSpreadsheet( ):
    """Prints the string 'Hello World(in Python)' into the current document"""
#get the doc from the scripting context which is made available to all scripts
    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.getCurrentComponent()
#check whether there's already an opened document. Otherwise, create a new one
    if not hasattr(model, "Text"):
        model = desktop.loadComponentFromURL(
            "private:factory/scalc","_blank", 0, () )

    sheets = model.getSheets() #XSpreadSheets
    sheets.insertNewByName("Primera hoja", 0)
    sheet = sheets.getByIndex(0)
    xCell = sheet.getCellByPosition(0, 0)
    xCell.setValue(123)
    return None
