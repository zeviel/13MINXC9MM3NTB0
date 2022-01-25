import amino
from pyfiglet import figlet_format
from colorama import init, Fore, Style
init()
print(
    f"""{Fore.RED}
Script by deluvsushi
Github : https://github.com/deluvsushi"""
)
print(figlet_format("aminocommentbo", font="smslant"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
link_info = client.get_from_link(input("-- Blog link::: ")).json["linkInfoV2"]
com_id = link_info["extensions"]["linkInfo"]["ndcId"]
blog_id = link_info["extensions"]["linkInfo"]["objectId"]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = input("-- Message::: ")
while True:
	try:
		sub_client.comment(blogId=blog_id, message=message)
		print("-- Comment is sent...")
	except Exception as e:
		print(e)
