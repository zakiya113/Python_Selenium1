import openpyxl

wk = openpyxl.Workbook()
sh = wk.active
sh.title = "Test"

print(sh.title)

sh['A4'].value="test.com"

#2nd Sheet is Created
wk.create_sheet(title="TestingW")
sh1 = wk['TestingW']
sh1['A3']='9876543210'

#Saving
wk.save("D:/TestData.xlsx")
