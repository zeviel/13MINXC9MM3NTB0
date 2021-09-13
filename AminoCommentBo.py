import AminoLab
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.RED)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminocommentbo", font="smslant"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
comment = input("Comment >> ")
blog_info = client.get_from_link(input("Blog Link >> "))
blog_id = blog_info.object_Id; ndc_Id = blog_info.ndc_Id

while True:
    try:
        client.submit_comment(ndc_Id=ndc_Id, message=comment, blog_Id=blog_id)
        print("Sended Comment")
    except Exception as e:
        print(e)
