#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，
奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分
按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，
高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，
可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，
求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义
成长整型。
"""
i = int (input(u'净利润：'.encode('gbk')))#py3中raw_input已经改为input
#这里经过试验用input也是可以的，另外，input中的中文提示如果
#不加处理会出现乱码，所以需要加raw_input(u'中文'.encode('gbk'))
#中文CMD编码默认是GB2312
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):#用来索引arr和rat中的值
    if i>arr[idx]:#arr[0]=1000000
    	r+=(i-arr[idx])*rat[idx]
    	print (i-arr[idx])*rat[idx]
    	i=arr[idx]
print r