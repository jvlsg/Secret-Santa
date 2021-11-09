# Secret Santa's little helper

Written by [jvlsg](https://github.com/jvlsg)

This is a small CLI utility to create a Secret Santa game, sending notifications via a SMTP.

## Quick-start

### New Game
* First, create a .csv file (default name `players.csv`) with the names and emails of the players with `name,email` as the first line. See the see `players_example.csv` file

```
python3 secret_santa new
```
This creates a new "Game File" (saved as "game.yml" by default, but you can change it). 

A "Game File" is a yaml stores the giver-reciever order, with base64 *obsfuscated* (i.e. not human readable) names.

### Email participants

Do a `--dryrun` to see if you can successfully connect to your SMTP server

```
python3 secret_santa email --dryrun ORGANIZER SERVER
```
Where
* `ORGANIZER` is the email address of the organizer, e.g. `cecile@example.com`
* `SERVER` is the SMTP server of your email provider, e.g. `smtp.example.com`

_**Please notice**_

**You will be prompted for your email password**, this is used to authenticate to the SMTP server to send the emails. 

Feel free to look at the `messager.py` to see how the password is handled.

Once you're good to go, you can email each participant using running the above command without the `--dryrun` flag


### Post-game review

```
python3 secret_santa load
```

Will load the game file, decode the base64, print it's results and save them in a a `_decoded.yml` file

The participants will also recieve in the email message a "game code" which is a **SHA256 hex digest** of the game file. 

You can use the hash and the `load` command to make the game as trasparent as possible, not that anyone will care