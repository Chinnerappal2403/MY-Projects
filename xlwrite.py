import xlwt;
from datetime import datetime;
from xlrd import open_workbook;
from xlwt import Workbook;
from xlutils.copy import copy
from pathlib import Path

'''style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('example.xls')
'''
def output(num,age,gender,cpt,slider,sc,fbs,rer,mh,eia,oldpeak,slope,ca,thala,output):
    my_file = Path('test.xls');
    if my_file.is_file():
        rb = open_workbook('test.xls');
        book = copy(rb);
        sh = book.get_sheet(0)
        # file exists
    else:
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)

    sh.write(num,0,int(age));
    sh.write(num,1,int(gender));
    sh.write(num,2,int(cpt));
    sh.write(num,3,int(slider));
    sh.write(num,4,int(sc));
    sh.write(num,5,int(fbs));
    sh.write(num,6,int(rer));
    sh.write(num,7,int(mh));
    sh.write(num,8,int(eia));
    sh.write(num,9,int(oldpeak));
    sh.write(num,10,int(slope));
    sh.write(num,11,int(ca));
    sh.write(num,12,int(thala));
    sh.write(num,13,float(output));
    #sh.write(num+1, 2, present);
    #You may need to group the variables together
    #for n, (v_desc, v) in enumerate(zip(desc, variables)):
    fullname='test.xls';
    book.save(fullname)
    return fullname;
