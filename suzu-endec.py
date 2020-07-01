#Mau recode ? Gpp buat belajar saja
#Tools ini tidak semua coding sendiri ada yang sebagian cp
import os
import urllib2                                             
import json
import time
from termcolor import colored, cprint                      
from time import sleep
from base64 import *

#banner
os.system('clear')
time.sleep(2)
print ("\33[1;32m###################################################")
time.sleep(0.1)
print ("#          \33[1;33mTOOLS TERMUX BY SUZU\33[1;31mX\33[1;33mPLOIT v1          \33[1;32m#")
time.sleep(0.1)
print ("###################################################")
time.sleep(0.1)
print ("#    \33[1;33mAuthor \33[1;31m: \33[1;33mSuzu\33[1;31mx\33[1;33mploit                          \33[1;32m#")
time.sleep(0.1)
print ("#    \33[1;33mTeam   \33[1;31m: \33[1;33mDark \33[1;31mClown \33[1;33mSecurity                 \33[1;32m#")
time.sleep(0.1)
print ("#    \33[1;33mGithub \33[1;31m: \33[1;33mhttps://github.com/suzu-\33[1;31mx\33[1;33mploit      \33[1;32m#") 
time.sleep(0.1)
print ("###################################################")
time.sleep(0.1)
print ("")
time.sleep(0.1)
print ("\33[1;37m{\33[1;31m+\33[1;37m} \33[1;33mMenu Pilihan \33[1;37m{\33[1;31m+\33[1;37m}")
time.sleep(0.1)
print ("")
time.sleep(0.1)
print ("\33[1;37m{\33[1;31m1\33[1;37m} \33[1;33mEncrypt     \33[1;37m{\33[1;32mON\33[1;37m}")
time.sleep(0.1)
print ("\33[1;37m{\33[1;31m2\33[1;37m} \33[1;33mDecrypt     \33[1;37m{\33[1;32mON\33[1;37m}")
time.sleep(0.1)
print ("")
pilih = raw_input('\33[1;37m{\33[1;32m?\33[1;37m} \33[1;33mPilih \33[1;31m~>\33[1;32m ')
if pilih == "1":
      teks = raw_input("\33[1;37m{\33[1;31m+\33[1;37m} \33[1;33mMasukan Text \33[1;31m~>\33[1;32m ")
      enc = b64encode(teks)
      print ("\33[1;37m{\33[1;31m+\33[1;37m} \33[1;33mHasil Encrypt \33[1;31m~>\33[1;32m"),enc
      time.sleep(2)
elif pilih == "2":
      teks = raw_input("\33[1;37m{\33[1;31m+\33[1;37m} \33[1;33mMasukan Encrypt \33[1;31m~>\33[1;32m ")
      dec = b64decode(teks)
      print ("\33[1;37m{\33[1;31m+\33[1;37m} \33[1;33mHasil Decrypt \33[1;31m~>\33[1;32m"),dec
