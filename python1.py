#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
程序源代码：
"""

for bai in range(1,5):#python都是左开右闭，所以是（1,5）
    for shi in range(1,5):
    	for ge in range(1,5):
    		if (bai != shi) and (shi != ge) and (bai != ge):
    			print bai,shi,ge