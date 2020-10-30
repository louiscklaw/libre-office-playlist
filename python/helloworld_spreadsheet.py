# https://github.com/luisperlaz/curso_python_ayto_2013/blob/f56898d07e21a75cdcbd17cfc61faeedf6224ff4/openoffice/examples/4_calc_create_save/create_modify_save_spreadsheet.py

def HelloworldSpreadsheet( ):
    """Prints the string 'Hello World(in Python)' into the current document"""
#get the doc from the scripting context which is made available to all scripts
    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.getCurrentComponent()
#check whether there's already an opened document. Otherwise, create a new one
    if not hasattr(model, "Text"):
        model = desktop.loadComponentFromURL(
            "private:factory/scalc","_blank", 0, () )

    doc = model

    sheets = model.getSheets() #XSpreadSheets
    sheets.insertNewByName("Primera hoja", 0)
    sheet = sheets.getByIndex(0)
    xCell = sheet.getCellByPosition(0, 0)
    xCell.setValue(123)

    doc.storeAsURL("file:///home/logic/_del/testsheet.ods", ())

    return None

# vim: set shiftwidth=4 softtabstop=4 expandtab:
