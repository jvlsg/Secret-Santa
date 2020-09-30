# Secret Santa's little helper

Written by [jvlsg](https://github.com/jvlsg)

This is a small CLI utility to create a Secret Santa game.

## Quick-start
1. Create a .csv file (default name `players.csv`) with the names and emails of the players with `name,email` as the first line. See the example below
```
name,mail
alice,alice@example.com
bob,bob@example.com
```
2. run `python3 secret_santa new` to create a new game. It will save the giver-reciever order in a encoded YAML file.
3. Once you're done, you can email each participant using `python3 secret_santa email ORGANIZER SERVER` where:
   1. ORGANIZER is the email address of the organizer, e.g. `cecile@example.com`
   2. SERVER is the SMTP server of your email provider, e.g. `smtp.example.com`
   3. You will be prompted for your email password, this is used to authenticate to the SMTP server to send the emails. Feel free to look at the `messager.py` to see how the password is handled.
4. The YAML file can be decoded using `python3 secret_santa load` , it will be save as a `_decoded` file
