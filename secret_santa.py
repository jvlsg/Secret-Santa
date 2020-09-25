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
    
    ## Subcommand email

    args = base_parser.parse_args()

    if args.version:
        print("version: {}".format(constants.VERSION))
        exit(0)

    if args.subcommand == "new":
        ## Check for args
        game_manager.new_game()
