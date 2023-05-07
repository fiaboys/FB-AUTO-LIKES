# ระวัง Error Indent นะครับ <3
import requests as XMLHttpRequest
from os import system
from time import sleep
import webbrowser
from bs4 import BeautifulSoup as bs
from application import Likers

def banner():
	print('''
     ╔═══╦══╗╔╗──╔══╦╗╔═╦═══╦═══╦═══╗
     ║╔══╣╔╗║║║──╚╣╠╣║║╔╣╔══╣╔═╗║╔═╗║
     ║╚══╣╚╝╚╣║───║║║╚╝╝║╚══╣╚═╝║╚══╗
     ║╔══╣╔═╗║║─╔╗║║║╔╗║║╔══╣╔╗╔╩══╗║
     ║║──║╚═╝║╚═╝╠╣╠╣║║╚╣╚══╣║║╚╣╚═╝║
     ╚╝──╚═══╩═══╩══╩╝╚═╩═══╩╝╚═╩═══╝
           สคริปต์นี้สร้างขึ้นโดยช่อง GENIX SHOP ทำเพื่อการศึกษา
	''')
	
def step3():
	system("clear")
	banner()
	data = XMLHttpRequest.get("https://az-like.com/login_v2").text
	getdata = bs(data, "html.parser")
	usercode = getdata.find("input", attrs={"id": "user-code"})['value']
	session = getdata.find("button", attrs={"id": "btn-verify-login"})['onclick'][19:51]
	linkverify = "https://fb.com/device?user_code=" + usercode
	webbrowser.open(linkverify)
	print(f"                   รหัสยืนยันตัวตน : {usercode}")
	print()
	print("     (STEP 3) ตัวเลือกหน้านี้ :")
	print()
	print("          [1] ยืนยันตัวตน")
	print("          [2] ยกเลิก")
	print()
	choice = input("     กรุณาใส่หมายเลข : ")
	print()
	if (choice == "1" or choice == "01"):
		res = XMLHttpRequest.post("https://az-like.com/verifyLogin",json={"code": session})
		if (res.status_code == 200):
			print("        เข้าสู่ระบบสำเร็จ! กรุณารอสักครู่...")
			tokens = res.json()['access_token']
			sleep(2)
			system("clear")
			banner()
			cookies = XMLHttpRequest.post("https://az-like.com/loginWithToken_v2",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","cookie": "__gads=ID=e7afc2688ac82e35-22abbe80f1db0044:T=1678352964:RT=1678352964:S=ALNI_MbLbU3pcFSslRZGAIzTJQ7TD6zZpw;_gid=GA1.2.627146000.1682435051;__gpi=UID=00000bd4dc223ab2:T=1678352964:RT=1682471433:S=ALNI_Mb8_Py3rv5RW-PuTrPjU-J-M56rTQ;_ga_Q6G7B4WRCL=GS1.1.1682471432.6.1.1682471482.0.0.0;_ga=GA1.2.606891092.1678352956;az_likecom_session=eyJpdiI6InhRRnZaakp0eVlZclZrR3RkOHVBWUE9PSIsInZhbHVlIjoiRXdWUm9FQU5IWGhyUks1Z3Q4R25Bc0lNOFZkcFdmdnE0ZEVGblU5ajdJcEhjdWIrVnFScFZ2TkdIT3BkMTh1TkpjOFQ5K3gvaEJPRlhZOWVpUStIMnBFZFBQeDdmcnpuUG1XRzFaUXpjcjFmRnVLWEhCM0JFTC9WQUYvWWJodUUiLCJtYWMiOiJhMDM5ZTFhYTBjMDI1NjM5MWY5NGZlMzEwNjIwZjM5MTU3ZjgxOGQ2N2Q5ZTk3OThkZDA2NzcwYzNkNmNhYjBhIn0%3D"},json={"access_token": tokens})
			cookie = cookies.headers['set-cookie'][:349]
			print("     (DONE) คุณสามารถเริ่มปั๊มไลค์ได้แล้ว !")
			print()
			target = input("       URL/ID : ")
			print()
			Likers(cookie,target)
		elif (res.status_code == 400):
			print("        ไม่สามารถเข้าสู่ระบบได้! ลองอีกครั้ง...")
			sleep(2)
			step3()
		else:
			print("        เกิดข้อผิดพลาดที่ไม่รู้จัก! โปรดติดต่อผู้สร้างสคริปต์")
			exit()
			
		
	else:
		exit()
		

	
def step2():
	system("clear")
	banner()
	print("     (STEP 2) ตัวเลือกหน้านี้ :")
	print()
	print("          [1] เปิดลิงก์เพื่อยืนยันตัวตน (กรอกรหัส)")
	print()
	choice = input("     กรุณาใส่หมายเลข : ")
	print()
	if (choice == "1" or choice == "01"):
		print("        กรุณายืนยันลิงก์ดังกล่าวเพื่อเข้าสู่ระบบ...")
		sleep(2)
		step3()
	else:
		print("        กรุณายืนยันลิงก์ดังกล่าวเพื่อเข้าสู่ระบบ...")
		sleep(2)
		step3()


def main_process():
	system("clear")
	banner()
	print("     (STEP 1) ตัวเลือกหน้านี้ :")
	print()
	print("          [1] เข้าสู่ระบบเพื่อดำเนินการต่อ")
	print()
	choice = input("     กรุณาใส่หมายเลข : ")
	print()
	if (choice == "1" or choice == "01"):
		print("        ระบบกำลังพาคุณไปหน้าล็อกอิน...")
		sleep(2)
		step2()
	else:
		print("        ระบบกำลังพาคุณไปหน้าล็อกอิน...")
		sleep(2)
		step2()
		

main_process()