#!/user/bin/env python
# _*_ coding:utf-8 _*_
# Filename: imfont.py
# Time: 2018-12-08 21:06:07
# Created by 2048K, kairan2048@163.com

from PIL import ImageFont

font = ImageFont.truetype('hei.ttf', size=4)
print(font.getsize('#'))
print(font.getsize(' '))
print(font.getsize('1'))
