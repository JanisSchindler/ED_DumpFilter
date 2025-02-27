import filter
import zipreader
import argparse
import re
from fileoutput import FileOutput
from point import Point

parsedArgs: vars
maxDistanceSquared: int
origin: Point
output: FileOutput

def main():
    # get command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to the file")
    parser.add_argument("--maxDistance", help="The maximum distance from origin", type=int, default=1500)
    parser.add_argument("--origin", help="The origin coordinates in x|y|z", type=Point.fromArgument, default="0|0|0")
    
    # initialize global variables
    global parsedArgs
    parsedArgs = vars(parser.parse_args())
    
    global maxDistanceSquared
    maxDistanceSquared = parsedArgs["maxDistance"] * parsedArgs["maxDistance"];

    global origin
    origin = parsedArgs["origin"]

    global output
    output = FileOutput()
    output.initialize(parsedArgs["path"] + ".filtered.json")

    # print (parsedArgs)
    # print ("origin:" + f'{origin.X}' + "|" + f'{origin.Y}' + "|" + f'{origin.Z}')

    # process the file
    zipreader.streamzip(parsedArgs["path"], processline)

    output.close()
    return

def processline(line):    
  filter.filter(line, lambda: output.onAccepted(line), maxDistanceSquared, parsedArgs["origin"])

# Runs the program
main()