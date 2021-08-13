import amino
import asyncio
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.RED)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("amino", font="ogre"))
print(pyfiglet.figlet_format("commentbo", font="big"))

async def main():
	client = amino.Client()
	email = input("Email >> ")
	password = input("Password >> ")
	await client.login(email=email, password=password)
	bloglink = input("Blog Link >> ")
	blog_info = await client.get_from_code(bloglink)
	blogId = blog_info.objectId
	communityid = blog_info.path[1:blog_info.path.index('/')]
	message = input("Message >> ")
	sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
	while True:
		try:
			await sub_client.comment(message=message, blogId=blogId)
			print("Comment Sended")
		except:
			pass

asyncio.get_event_loop().run_until_complete(main())
