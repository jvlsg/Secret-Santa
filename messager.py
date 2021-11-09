import smtplib
import ssl
import yaml
import getpass
import base64
import random
import hashlib
import constants
#SMTP_URL = "smtp.gmail.com"

def email_players(organizer_email, smtp_url, game_file_path, ssl_port, dryrun):

    game_hash = hashlib.sha256()

    with open(game_file_path) as game_file:
        game = yaml.safe_load(game_file)

    #Take Hash of game file
    with open(game_file_path,"rb") as game_file:
        for byte_block in iter(lambda: game_file.read(4096),b""):
            game_hash.update(byte_block)
    
    password = getpass.getpass("SMTP password: ")

    with smtplib.SMTP_SSL(smtp_url, port=ssl_port, context=ssl.create_default_context()) as server:
        
        try: server.login(organizer_email, password)
        except smtplib.SMTPAuthenticationError: print("Authentication Failed!")
        else:
            print("Successfully Logged In")
            
            print("Shuffling List")
            random.shuffle(game["giver_list"])
            for pair in game["giver_list"]:
                giver_email = base64.b64decode(pair["giver"]["email"]).decode("utf-8")
                giver_name = base64.b64decode(pair["giver"]["name"]).decode("utf-8")
                reciever_name = base64.b64decode(pair["reciever"]).decode("utf-8")
                
                message ='From: <{}>\r\nSubject: {}\r\n\n{}'.format(
                    organizer_email,
                    constants.MESSAGE_SUBJECT, 
                    constants.MESSAGE_BODY.format(
                        reciever_name, game_hash.hexdigest()
                    )
                )
                
                if dryrun:
                    print("[-] Dry-run, would send to: {} <{}>\n{}".format(giver_name,giver_email,message))
                else:          
                    try:
                        server.sendmail(organizer_email, giver_email, message.encode("utf-8"))
                    except e:
                        print("[!] Failure on {}".format(giver_name))
                        pass
                    else:
                        print("[+] Email sent to: {} <{}>".format(giver_name,giver_email))
            server.quit()