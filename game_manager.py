import csv
import random
import time
import base64
import yaml

def new_game(player_file_path, game_file_path):
    """
    Creates a new game file
    """
    with open(player_file_path) as player_file:
        player_list = list(csv.DictReader(player_file))

    player_count = len(player_list)

    if player_count < 2:
        raise Exception("Less than two players")

    """
    Base64 encoding for obfuscation purposes
     this allows a human to manually check the game.yml file and verify that 
     a "cycle" is closed betweem players without spoiling the surpise.
    """
    #TODO: Validate uniqueness of names 
    for p in player_list:
        p["name"]=base64.b64encode(p["name"].encode("utf-8")) 
        p["email"]=base64.b64encode(p["email"].encode("utf-8"))

    random.shuffle(player_list)

    """
    Each player is a "Giver" who gifts a "Reciever" all players must be Givers and 
    Recievers, so that the game order follows a Circular Linked List behaviour
    """

    giver_list=[]

    for i in range(player_count):
        giver_list.append({
            "giver":player_list[i],
            #The reciever is the next player, circling arround so the first player 
            # recieves a gift from the last one
            "reciever": player_list[(i+1)%player_count]["name"] 
        })

    game = {"timestamp":time.time(),"giver_list":giver_list}
    print(game)
    with open(game_file_path,mode="w") as game_file:
        yaml.dump(game,game_file)

def load_game(game_file_path):
    """
    Loads a game file, decodes the data, and saves it in a file
    """
    with open(game_file_path) as game_file:
        game = yaml.safe_load(game_file)

    for p in game["giver_list"]:
        p["reciever"]=base64.b64decode(p["reciever"]).decode("utf-8")
        p["giver"]["name"]=base64.b64decode(p["giver"]["name"]).decode("utf-8")
        p["giver"]["email"]=base64.b64decode(p["giver"]["email"]).decode("utf-8")   
    print(game)
    game["decode_timestamp"] = time.time()
    with open(game_file_path+"_decoded",mode='w') as decoded_game_file:
        yaml.dump(game,decoded_game_file)