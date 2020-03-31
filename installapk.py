# coding:utf8
# Author:daben_chen

"""
批量安装apk
"""

import os
import shutil
import sys
import subprocess
import mobileinfo
import time


def install_apk(device):
	"""
	:params:adb批量安装
	:return:
	"""
	
	apklist = []
	apkdir = "apk"
	if len(sys.argv) == 1:	
		for f in os.listdir(apkdir):
			extname = os.path.splitext(f)[1]
			if extname == ".apk" :
				apklist.append(f)
		for apk in apklist:
			print("install "+apk+" on "+device)
			res = os.system("adb -s " + device + " install -r "+ apkdir + "/" + "\"" + apk + "\"")
			res = res>>8
			if res != 0:
				print("Failed to install " + apk +"\n")
				return False
			else:
				print("Success to install " + apk +"\n")
	elif len(sys.argv) > 1:
		argvlen = len(sys.argv)
		for l in range(argvlen):
			if l != 0 :
				apk = sys.argv[l]
				print("install "+apk+" on "+device)
				res = os.system("adb -s " + device + " install -r "+ apkdir + "/" + "\"" + apk + "\"")
				res = res>>8
				if res != 0:
					print("Failed to install " + apk +"\n")
					return False
				else:
					print("Success to install " + apk +"\n")


def main():
	mounted_devices = mobileinfo.find_devices()
	if mounted_devices is not None:
		for device in mounted_devices:
			install_apk(device)


if __name__ == '__main__':
	main()