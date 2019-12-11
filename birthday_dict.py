#!/usr/bin/python3

#script that converts dictionary defined in this script to JSON format stored on the disk

import json

birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

#open JSON file to write
with open("birthday.json", "w") as f:
	json.dump(birthdays,f)


