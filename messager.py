import smtplib
import ssl
import yaml
import getpass
import base64

ORGANIZER_EMAIL = ""  # Enter your address
SMTP_URL = "smtp.gmail.com"

with open("game.yml") as game_file:
    game = yaml.safe_load(game_file)

port = 465  # For SSL
password = getpass.getpass("SMTP password: ")
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(SMTP_URL, port, context=context) as server:
    server.login(ORGANIZER_EMAIL, password)
    for g in game["giver_list"]:
        giver_email = base64.b64decode(g["giver"]["email"]).decode("utf-8")
        giver_name = base64.b64decode(g["giver"]["name"]).decode("utf-8")
        reciever_name = base64.b64decode(g["reciever"]).decode("utf-8")
        
        message_body = """Seu amigo secreto é: {}""".format(reciever_name).encode("utf-8")        
        message ='Subject: {}\n\n{}'.format("Seu Amigo Secreto!", message_body)
        
        try:
            server.sendmail(ORGANIZER_EMAIL, giver_email, message)
        except e:
            print("[!] Failure on {}\n{}".format(giver_name,e))
            pass
        else:
            print("[+] Email to {} was sent!".format(giver_name))
    server.quit()