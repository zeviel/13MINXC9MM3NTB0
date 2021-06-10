import amino
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.RED)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("amino", font="ogre"))
print(pyfiglet.figlet_format("commentbo", font="big"))
client = amino.Client()
email=input("Email/Почта: ")
password=input("Password/Пароль: ")
client.login(email=email, password=password)
bloglink = input("Blog Link/Ссылка на Блог: ")
blog = client.get_from_code(bloglink)
blogId = blog.objectId
comId = blog.path[1:blog.path.index('/')]
message = input("Message/Сообщение: ")
sub_client = amino.SubClient(comId=comId,profile=client.profile)
while True:
	try:
		sub_client.comment(message=message,blogId=blogId)
		print("Comment Sended/Комментарий отправлен!")
	except:
		pass
