import xlwt
wb = xlwt.Workbook()
sh = wb.add_sheet('数据')

ft = xlwt.Font()
ft.name = '微软雅黑' #设置字体
ft.colour_index = 2  #设置颜色
ft.height = 11 *20  # 设置字体大小
ft.bold = True
ft.underline = True
ft.italic = True


alg = xlwt.Alignment()
alg.horz = 2 #1 左， 2中，3 右
alg.vert = 0 #0 上，1中，2下


# 设置单元格高度
sh.row(3).height_mismatch = True
sh.row(3).height = 10 * 256

# 设置单元格宽度
sh.col(3).width = 20 * 256

# 设置边框
border = xlwt.Borders()
# 细实线 ：1 ，小粗实线：2，细虚线：3，中细虚线：4，大粗实线：5，双线：6,细点虚线：7
border.left = 1
border.right = 1
border.top = 1
border.bottom = 1

border.left_colour = 1
border.right_colour = 2
border.top_colour = 3
border.bottom_colour = 4


style = xlwt.XFStyle()
style.font = ft
style2 = xlwt.XFStyle()
style2.aligment = alg

style3 = xlwt.XFStyle()
style3.border = border

sh.write(1,1,'吕小布')
sh.write(2,2,'吕小布',style)
sh.write(3,3,'貂蝉',style2)
sh.write(4,4,'黄忠',style3)

wb.save('04_excel样式.xlsx')