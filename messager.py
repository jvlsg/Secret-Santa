import smtplib
import ssl
import yaml
import getpass
import base64
import random
#SMTP_URL = "smtp.gmail.com"

def email_players(organizer_email,smtp_url,game_file_path,ssl_port):

    with open(game_file_path) as game_file:
        game = yaml.safe_load(game_file)

    password = getpass.getpass("SMTP password: ")

    with smtplib.SMTP_SSL(smtp_url, port=ssl_port, context=ssl.create_default_context()) as server:
        
        try: server.login(organizer_email, password)
        except SMTPAuthenticationError: print("Authentication Failed!")
        else:            
            random.shuffle(game["giver_list"])
            for pair in game["giver_list"]:
                giver_email = base64.b64decode(pair["giver"]["email"]).decode("utf-8")
                giver_name = base64.b64decode(pair["giver"]["name"]).decode("utf-8")
                reciever_name = base64.b64decode(pair["reciever"]).decode("utf-8")
                
                message_body = """Seu amigo secreto é: {}""".format(reciever_name)
                message ='Subject: {}\n\n{}'.format("Seu Amigo Secreto!", message_body)
                try:
                    server.sendmail(organizer_email, giver_email, message.encode("utf-8"))
                except e:
                    print("[!] Failure on {}".format(giver_name))
                    pass
                else:
                    print("[+] Email sent to: {} <{}>".format(giver_name,giver_email))
            server.quit()