import xlwt

wb = xlwt.Workbook()
sh = wb.add_sheet('电影安全')

sh.write(0,0,'影片')
sh.write(0,1,'综合票房')
sh.write(0,2,'票房占比')
sh.write(0,3,'排片场次')

sh.write(1,0,'如果声音不记得')
sh.write(1,1,361.57)
sh.write(1,2,33.3)
sh.write(1,3,95371)

sh.write(2,0,'赤虎先生')
sh.write(2,1,193.24)
sh.write(2,2,17.9)
sh.write(2,3,79980)




wb.save('01_电影数据.xlsx')
