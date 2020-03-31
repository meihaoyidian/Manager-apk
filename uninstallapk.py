# coding:utf8
# Author:daben_chen

"""
批量卸载apk
"""

import os
import shutil
import sys
import subprocess
import zipfile
import re
import mobileinfo


def uninstall_apk(device):
	"""
	:params:批量卸载apk
	:return:
	"""

	apklist = []
	apkdir = "uninstallapk"
	if len(sys.argv) == 1:	
		for f in os.listdir(apkdir):
			extname = os.path.splitext(f)[1]
			if extname == ".apk" :
				apklist.append(f)
		for apk in apklist:
			print("uninstall "+apk+" on "+device)
			pkgname = get_packaganame("uninstallapk" +"/"+apk)
			res = os.system("adb -s " + device + " uninstall " + pkgname)
			res = res>>8
			if res != 0:
				print("Failed to uninstall " + apk +"\n")
				return False
			else:
				print("Success to uninstall " + apk +"\n")
	elif len(sys.argv) > 1:
		argvlen = len(sys.argv)
		for l in range(argvlen):
			if l != 0 :
				apk = sys.argv[l]
				print("uninstall "+apk+" on "+device)
				pkgname = get_packaganame("uninstallapk" +"/"+apk)
				res = os.system("adb -s " + device + " uninstall " + pkgname)
				res = res>>8
				if res != 0:
					print("Failed to uninstall " + apk +"\n")
					return False
				else:
					print("Success to uninstall " + apk +"\n")



def get_packaganame(apk):
	"""
	:params:获取应用主包名
	:return:package_name
	"""
	zf = zipfile.ZipFile(apk, "r")
	zf.extract("AndroidManifest.xml", "temp")
	zf.close()
	child = subprocess.Popen("java -jar AXMLPrinter2.jar temp/AndroidManifest.xml", stdout=subprocess.PIPE, shell=True)
	message = child.stdout.read().decode()
	reg = re.compile(r"(?<=package=)\"(.*)\"")
	m = re.search(reg, message)
	package_name =  m.group(1)
	print(package_name)
	return package_name


def main():
	mounted_devices = mobileinfo.find_devices()
	if mounted_devices is not None:
		for device in mounted_devices:
			uninstall_apk(device)


if __name__ == '__main__':
	main()