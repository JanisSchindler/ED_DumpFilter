# ED_DumpFilter

This command line script takes a zipped systems.*.json.gz from https://www.spansh.co.uk/dumps and filters it based on the distance to a reference systems coordinates.

Requirements

Python 3.13.2

orjson

py -m ensurepip --upgrade

py -m pip --install orjson 


usage: src/main.py [-h] [--maxDistance MAXDISTANCE] [--origin ORIGIN] [--columns COLUMNS] path

where

--maxDistance is the distance to check for. The default is 1500 LY

--origin is the reference system given by its coordinates in x|y|z. The default is Sol (0|0|0)

--columns defines the columns to keep from the individual lines, separated by a comma. By default these are: 

  id64, name,coords, population, allegiance, government, primaryEconomy, secondaryEconomy, security, controllingPower, powerState

path is the path to the .json.gz file


### Example

py src/main.py --origin '5000|1000|10000' --maxDistance 2000 --columns 'id64, name, coords, controllingPower' systems_1month.json.gz
