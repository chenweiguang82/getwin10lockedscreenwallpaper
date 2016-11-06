# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 17:39:46 2016

@author: ChenWeiguang
"""

import getpass
import os
import shutil

##############引用别人的代码#############
## http://blog.csdn.net/shuifa2008/article/details/9333193 ####
## http://www.pythontab.com/html/2015/pythonhexinbiancheng_1108/977.html ##
import struct
# 支持文件类型 
# 用16进制字符串的目的是可以知道文件头是多少字节 
# 各种文件头的长度不一样，少则2字符，长则8字符 
def typeList(): 
  return { 
    "FFD8FF": "JPEG", 
    "89504E47": "PNG"} 
   
# 字节码转16进制字符串 
def bytes2hex(bytes): 
  num = len(bytes) 
  hexstr = u"" 
  for i in range(num): 
    t = u"%x" % bytes[i] 
    if len(t) % 2: 
      hexstr += u"0"
    hexstr += t 
  return hexstr.upper() 
   
# 获取文件类型 
def filetype(filename): 
  binfile = open(filename, 'rb') # 必需二制字读取 
  tl = typeList() 
  ftype = 'unknown'
  for hcode in tl.keys(): 
    numOfBytes = len(hcode) / 2 # 需要读多少字节 
    binfile.seek(0) # 每次读取都要回到文件头，不然会一直往后读取 
    hbytes = struct.unpack_from("B"*numOfBytes, binfile.read(numOfBytes)) # 一个 "B"表示一个字节 
    f_hcode = bytes2hex(hbytes) 
    if f_hcode == hcode: 
      ftype = tl[hcode] 
      break
  binfile.close() 
  return ftype 
  
##############################

username=getpass.getuser()
#print username

dir1 = 'C:/Users/'+username+'/AppData/Local/Packages'
#print dir1
filename1=os.listdir(dir1)
length=len('Microsoft.Windows.ContentDeliveryManage')
#print length
for i in filename1:
    if (i[0:length] == 'Microsoft.Windows.ContentDeliveryManage'):
#        print i
        dir2=dir1+'/'+i+'/LocalState/Assets'
        

#print dir2
os.chdir(dir2)
filename2=os.listdir('./')
j=len(os.listdir('E:/win10wallpaper'))

for i in filename2:
    filesize=os.path.getsize('./'+i)
    if (filetype('./'+i) == 'JPEG' or filetype('./'+i) == 'PNG'):
        if (filesize/1024 >= 100):
#            print i, filetype('./'+i),filesize/1024,'KB'
            newfile='E:/win10wallpaper/'+str(j)+'.'+filetype('./'+i)
            oldfile=dir2+'/'+i
            print oldfile
            print newfile
            shutil.copy(oldfile,newfile)
            j=j+1
            
            

            
    



