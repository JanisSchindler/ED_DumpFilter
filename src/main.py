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
    zipreader.streamzip(parsedArgs["path"], onChunk)

    output.close()
    return

def isCompleteSystemLine(line):
   # Sample line:

   # {"id64":819519,"name":"Phua Fraae AA-A h0","mainStar":"B (Blue-White) Star","coords":{"x":-34608.78125,"y":513.34375,"z":26058.59375},"updateTime":"2025-02-17 03:07:01+00"},
   # A valid line must at least contain {"id64"} and updateTime:[...]"}
   result = re.search(r"\{\"id64\"\}.+updateTime:.+\}", line)
   if ('{\"id64\"' in line) and ('\"}' in line) :
      return True
   
   return False

def onChunk(chunk):    
    lines = chunk.splitlines()
    for line in lines:

       # ignore the first line in the file
      if '[' in line:
        continue

      if (isCompleteSystemLine(line) == False):
        # If the chunk starts with an invalid line, skip it
        if (lines.index(line) == 0):
          continue

        # Remember that start of the line for the next chunk.
        remainder = line
        return remainder
      
      filter.filter(line, lambda: output.onAccepted(line), maxDistanceSquared, parsedArgs["origin"])

    return ''


# Runs the program
main()