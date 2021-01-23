from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.RED)
print("Script by Zevi/Скрипт сделан Zevi")
print("┌────────────────────────────────────┐")
print("│Author :  LilZevi                   │")
print("│Github : https://github.com/LilZevi │")
print("└────────────────────────────────────┘")
print("YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ")
print("▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄")
print("█▀█ █░█░█ █ █░▀█ █░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░")
print("▄▀ ▄▀▄ █▄░▄█ █▄░▄█ █▀▀ █▄░█ ▀█▀")
print("█░ █░█ █░█░█ █░█░█ █▀▀ █░▀█ ░█░")
print("░▀ ░▀░ ▀░░░▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░▀░")
print("█▀▄ ▄▀▄ ▀█▀")
print("█▀█ █░█ ░█░")
print("▀▀░ ░▀░ ░▀░")
import amino
#инпут почты и пароля для входа в аккаунт
email=input("Email/Почта:")
password=input("Password/Пароль:")
comid=input('Type community id/Введите id сообщества:')
client = amino.Client()
client.login(email=email, password=password)
sub_client = amino.SubClient(comId=comid,profile=client.profile)
print('\nLogged in/Бот зашел!')
bloglink=input("Blog Link/Ссылка на Блог:")
blog=client.get_from_code(bloglink)
blogId=blog.objectId
comId=blog.path[1:blog.path.index('/')]
message=input("Message/Сообщение:")
sub_client = amino.SubClient(comId=comid,profile=client.profile)
while True:
	try: sub_client.comment(message=message,blogId=blogId)
	except: pass
