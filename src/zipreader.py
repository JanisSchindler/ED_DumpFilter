import gzip
from progress import Progress 
import os
 
def streamzip(zipPath, processLine):
  with gzip.open(zipPath, 'rt') as zipfile:
    for line in zipfile:
      processLine(line)