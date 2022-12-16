from datetime import datetime
hostpath=""
redirect = ""
with open("path.txt",'r+') as fp:
	hostpath = fp.readline();
with open("dir.txt",'r+') as fp:
	redirect = fp.readline();

websitelist = ["youtube.com","www.youtube.com","github.com"]
mod=False
def activate():
	while hostpath != "":
		with open(hostpath,'r+') as f:
			old = f.read()
			for i in range(0,len(websitelist)):
				f.write(redirect+" "+websitelist[i]+'\n')
			print("BLOCKED")
		break
def deactive():
	while hostpath != "":
		with open(hostpath,'w+') as f:
			old = f.read()
			for i in range(0,len(websitelist)):
				f.write("")
			print("UNBLOCKED")
		break
while True:
	now=datetime.now()
	hour=now.hour
	if hour>=21:
		activate()
		break
	else:
		deactive()
		break


 