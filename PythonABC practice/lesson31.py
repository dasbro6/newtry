import openpyxl,pprint

print('Opening workbook')
workbook = openpyxl.load_workbook('salecar.xlsx')
mainsheet = workbook.active
qichexiaoliangsheet={}


for row in range(2,mainsheet.max_row+1):
    pinpai =  mainsheet['A'+ str(row)].value
    chexing = mainsheet['B'+ str(row)].value
    chekuan = mainsheet['D' + str(row)].value
    xiaoliang09 = mainsheet['E' + str(row)].value




    qichexiaoliangsheet.setdefault(pinpai, {})
    qichexiaoliangsheet[pinpai].setdefault(chexing, {})

    qichexiaoliangsheet[pinpai][chexing].setdefault(chekuan,{'shuliang':0,'xiaoliang':0})
    qichexiaoliangsheet[pinpai][chexing][chekuan]['shuliang'] += 1
    if isinstance(xiaoliang09,int):
        qichexiaoliangsheet[pinpai][chexing][chekuan]['xiaoliang'] += int(xiaoliang09)
        print(qichexiaoliangsheet[pinpai][chexing][chekuan]['xiaoliang'])
print('Writing results......')
newfile = open('xiaoliangdate.py','w')
newfile.write('allDate ='+ pprint.pformat(qichexiaoliangsheet))
print('completed')