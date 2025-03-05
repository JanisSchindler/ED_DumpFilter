from filter import Filter
import zipreader
import argparse
import re
from fileoutput import FileOutput
from point import Point

parsedArgs: vars
maxDistanceSquared: int
origin: Point
output: FileOutput
filter: Filter

def main():
    # get command line arguments
    defaultColumns = "id64, name, coords, population, allegiance, government, primaryEconomy, secondaryEconomy, security, controllingPower, powerState"
    
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to the file")
    parser.add_argument("--maxDistance", help="The maximum distance from origin", type=int, default=1500)
    parser.add_argument("--origin", help="The origin coordinates in x|y|z", type=Point.fromArgument, default="0|0|0")
    parser.add_argument('--columns', help="Add columns to select, separated by a comma (e.g. 'id64, name, coords')", type=str, default=defaultColumns)
    # initialize global variables
    global parsedArgs
    parsedArgs = vars(parser.parse_args())
    
    global maxDistanceSquared
    maxDistanceSquared = parsedArgs["maxDistance"] * parsedArgs["maxDistance"];

    global origin
    origin = parsedArgs["origin"]

    columns = parsedArgs["columns"].split(',')
    columns = [c.strip() for c in columns]
    global filter
    filter = Filter(columns)

    global output
    output = FileOutput()
    output.initialize(parsedArgs["path"] + ".filtered.json")

    # process the file
    zipreader.streamzip(parsedArgs["path"], processline)

    output.close()
    return

def processline(line):    
  filter.filter(line, lambda l: output.onAccepted(l), maxDistanceSquared, parsedArgs["origin"])

# Runs the program
main()