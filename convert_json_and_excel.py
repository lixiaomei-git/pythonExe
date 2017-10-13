import os
import sys
import getopt
import json
import xlrd
import xlsxwriter
from collections import OrderedDict

def get_options():

    json_file = "umicode.json"
    excel_file = "umicode.xls"

    try:
        opts, args = getopt.getopt(sys.argv[0:], "h", ["json=", "excel="])
    except getopt.GetoptError as e:
        print (e)
        sys.exit(2)

    for opt, value in opts:
        if "--json" == opt :
            json_file = value

        if "--excel" == opt :
            excel_file = value

    return json_file,excel_file

def convert_json_to_excel(json_file, excel_file):
    with open(json_file, 'r') as json_f:
        json_data = json.load(json_f, object_pairs_hook=OrderedDict)

    xls = xlsxwriter.Workbook(excel_file)
    sheet = xls.add_worksheet("Sheet1")
   
    sheet.write_string(0, 0, "UMI CODE")
    sheet.write_string(0, 1, "SHORT_MSG")
    sheet.write_string(0, 2, "LONG_MSG")

    row = 1 
    for umi, messages in json_data.items():
        sheet.write_string(row, 0, umi)
        for message in messages:
            if message.__contains__('SHORT_MSG'):
                sheet.write_string(row, 1, message['SHORT_MSG'])
            if message.__contains__('LONG_MSG'):
                sheet.write_string(row, 2, message['LONG_MSG'])
        row = row + 1

    xls.close()
    print("\n")
    print("*"*60)
    print("{} convert to {} Finished...".format(json_file, excel_file))

def convert_excel_to_json(json_file, excel_file):
    xls = xlrd.open_workbook(excel_file)
    sheet = xls.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    
    result = OrderedDict()
    for i in range(1, nrows):
        row_value = sheet.row_values(i)
        short_msg = {}
        long_msg = {}
        messages = []
        short_msg['SHORT_MSG'] = row_value[1].strip()
        long_msg['LONG_MSG'] = row_value[2].strip()
        messages.append(short_msg)
        messages.append(long_msg)
        result[row_value[0].strip()] = messages

    json_data=json.dumps(result,indent = 2)
    
    with open(json_file, 'w') as json_f:
        json_f.write(json_data)

    print("\n")
    print("*"*60)
    print("{} convert to {} Finished...".format(excel_file, json_file))

def main():
    json_file, excel_file = get_options()
    print("\n")
    print("*"*60)
    option = input('1)Json convert to Excel. 2)Excel convert to Json. :')
    if option == "1":convert_json_to_excel(json_file, excel_file)
    if option == "2":convert_excel_to_json(json_file, excel_file)

if __name__=="__main__":
    main()
