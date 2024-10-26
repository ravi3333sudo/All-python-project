from instabot import bot
bot=bot()
bot.login(username=" ",password="")
# bot.follow('#idname u want to flow')
# bot.upload_photo("path copy you want to upload")
# bot.unfollow("id name u want to unflow")
# bot.send_message("i love pyhton",["id name"," id name","id name"])
# followers=bot.get_user_followers(" ")
# for follower in followers:
#     print(bot.get_user info(follower))
following=bot.get_user_following("jone_python08")
for following in following:
    print(bot.get_user_info(following))