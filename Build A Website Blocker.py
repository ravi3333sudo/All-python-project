import datetime
import time

end_time = datetime.datetime(2024,10,30)
site_block= ["www.wscubetech.com","www.facebook.com"]
host_path ="C:/Windows/System32/drivers/etc/hosts"
redirect ="127.0.0.1"

while True:
    if datetime.datetime.now()<end_time:
        print("Start blocking")
        with open(host_path,"r") as host_file :
            content = host_path.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect +" "+website+"\n")
                else:
                    pass
    else:
        with open(host_path,"r+") as host_file :
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)

            host_file.truncate()

        time.sleep(5)