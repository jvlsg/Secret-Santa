import csv
import random
import time
import base64
import yaml
with open("players.csv") as player_file:
    player_list = list(csv.DictReader(player_file))

    # Base64 encoding for obfuscation purposes
    # this allows a human to manually check the game.yml file and verify that 
    # a "cycle" is closed betweem players without spoiling the surpise.
    for p in player_list:
        p["name"]=base64.b64encode(p["name"].encode("utf-8"))
        p["email"]=base64.b64encode(p["email"].encode("utf-8"))

    player_count = len(player_list)
    random.shuffle(player_list)
    
    giver_list=[]
    for i in range(player_count):
        giver_list.append({
            "giver":player_list[i],
            "reciever": player_list[(i+1)%player_count]["name"]  
            })

    game = {"timestamp":time.time(),"giver_list":giver_list}

with open("game.yml",mode="w") as game_file:
    yaml.dump(game,game_file)
    