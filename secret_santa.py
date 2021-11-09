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
    new_game_parser.add_argument('--players','-p', help='path for players file', default=constants.DEFAULT_PLAYER_FILE_PATH)
    new_game_parser.add_argument('--game','-g', help='path for game file')

    ## Subcommand: load
    load_game_parser = subparsers.add_parser('load', help='Load game, decode data')
    load_game_parser.add_argument('--game','-g', help='path for game file', type=str, default=constants.DEFAULT_GAME_FILE_PATH )

    ## Subcommand email
    email_parser = subparsers.add_parser('email', help='email players')
    email_parser.add_argument('organizer', help='Email address of the organizer')
    email_parser.add_argument('server', help='URL/IP of the SMTP server')
    email_parser.add_argument('--ssl','-s', help='SSL port, default 465', type=int, default=constants.DEFAULT_SSL)
    email_parser.add_argument('--game','-g', help='path for game file', type=str, default=constants.DEFAULT_GAME_FILE_PATH )
    email_parser.add_argument('--dryrun','-n', action='store_true', help='Test email connection', default=False)

    args = base_parser.parse_args()

    if args.version:
        print("version: {}".format(constants.VERSION))
        exit(0)

    if args.subcommand == "new":
        game_manager.new_game(
            player_file_path=args.players,
            game_file_path=args.game or email_parser.get_default("game")
        )

    elif args.subcommand == "email":
        messager.email_players(
            organizer_email=args.organizer,
            smtp_url=args.server,
            game_file_path=args.game or email_parser.get_default("game"),
            ssl_port=args.ssl or email_parser.get_default("ssl"),
            dryrun=args.dryrun or email_parser.get_default("dryrun")
        )

    elif args.subcommand == "load":
        game_manager.load_game(game_file_path=args.game or load_game_parser.get_default("game"))