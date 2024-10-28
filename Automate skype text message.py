from skpy import Skype
import os.path

slogin = Skype("id name", "password")

contact = slogin.contacts["live id input"]
with open(" input path of the image include name","rb") as f:
    contact.chat.sendfile(f,"file name input",image=True)





# group = slogin.chats.create(["input live id1","input live id2"])
#
# contact = slogin.contacts["live id "]
# contact.chat.sendMsg("welcome to My world")
# for i in contact :
#     print(i)
