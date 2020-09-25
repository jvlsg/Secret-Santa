import smtplib
import ssl
import yaml
import getpass
import base64

#SMTP_URL = "smtp.gmail.com"

def email_players(organizer_email,smtp_url,game_file_path="game.yml",ssl_port=465):

    with open(game_file_path) as game_file:
        game = yaml.safe_load(game_file)

    password = getpass.getpass("SMTP password: ")

    with smtplib.SMTP_SSL(smtp_url, port=ssl_port, context=ssl.create_default_context()) as server:
        
        try: server.login(ORGANIZER_EMAIL, password)
        except SMTPAuthenticationError: print("Authentication Failed!")
        else:            
            for pair in game["giver_list"]:
                giver_email = base64.b64decode(pair["giver"]["email"]).decode("utf-8")
                giver_name = base64.b64decode(pair["giver"]["name"]).decode("utf-8")
                reciever_name = base64.b64decode(pair["reciever"]).decode("utf-8")
                
                message_body = """Seu amigo secreto é: {}""".format(reciever_name).encode("utf-8")        
                message ='Subject: {}\n\n{}'.format("Seu Amigo Secreto!", message_body)
                
                try:
                    server.sendmail(ORGANIZER_EMAIL, giver_email, message)
                except e:
                    print("[!] Failure on {}\n{}".format(giver_name,e))
                    pass
                else:
                    print("[+] Email sent to: {} <{}>".format(giver_name,giver_email))
            server.quit()