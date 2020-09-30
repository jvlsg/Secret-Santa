import messager
import game_manager
import argparse
import constants

if __name__ == "__main__":
    base_parser = argparse.ArgumentParser(prog="secret_santa",
            description='Helper utility for Secret Santa Games')

    base_parser.add_argument('--version','-v',action='store_true', help='Print version and exit')
    subparsers = base_parser.add_subparsers(help='sub-command help',dest="subcommand")
    ## Subcommand: new
    new_game_parser = subparsers.add_parser('new', help='new game')
    new_game_parser.add_argument('--players','-p', help='path for players file')
    new_game_parser.add_argument('--game','-g', help='path for game file')

    ## Subcommand: load
    load_game_parser = subparsers.add_parser('load', help='Load game, decode data')
    load_game_parser.add_argument('--game','-g', help='path for game file')

    ## Subcommand email
    email_parser = subparsers.add_parser('email', help='email players')
    email_parser.add_argument('organizer', help='Email address of the organizer')
    email_parser.add_argument('server', help='URL/IP of the SMTP server')
    email_parser.add_argument('--ssl','-s', help='SSL port, default 465', type=int)
    email_parser.add_argument('--game','-g', help='path for game file')

    args = base_parser.parse_args()

    if args.version:
        print("version: {}".format(constants.VERSION))
        exit(0)

    game_file_path = args.game if args.game != None else constants.DEFAULT_GAME_FILE_PATH  

    if args.subcommand == "new":
        player_file_path = args.players if args.players != None else constants.DEFAULT_PLAYER_FILE_PATH  
        game_manager.new_game(player_file_path=player_file_path,game_file_path=game_file_path)

    elif args.subcommand == "email":
        ssl_port = args.ssl if args.ssl != None else constants.DEFAULT_SSL
        messager.email_players(organizer_email=args.organizer,smtp_url=args.server,game_file_path=game_file_path,ssl_port=ssl_port)

    elif args.subcommand == "load":
        game_manager.load_game(game_file_path=game_file_path)