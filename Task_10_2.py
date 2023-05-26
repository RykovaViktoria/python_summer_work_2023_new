# import openpyxl
# wb = openpyxl.load_workbook('excel.xlsx')
# # wb.create_sheet('Итого')
# print(wb.sheetnames)
# # ws = wb.active
# # wn = wb['Итого']

import functools
print(functools.reduce(lambda x, y: x * y, [1,2,3,4,5], 100))

# with open("text.txt", 'w') as fo:
#     fo.write('')
# with open("text.txt") as f:
#     print(111, len(f.read()))
#     print(222, len(f.read()))