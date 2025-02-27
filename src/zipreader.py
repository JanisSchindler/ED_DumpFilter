import gzip
from progress import Progress 
import os
 
 # Takes the zipPath and opens it
 # Reads blocks of 4KB and passes it to onChunk
 # Keeps track of the progress
def streamzip(zipPath, onChunk):
  chunk_size = 4096
  remainder = ''
  with gzip.open(zipPath, 'rt') as zipfile:

      # Get the size of the uncompressed file for the progress calculation
      zipfile.seek(0, os.SEEK_END)
      size = zipfile.tell()
      read = 0
      p = Progress(size)

      # Reset to the beginning
      zipfile.seek(0, os.SEEK_SET)

      # Read the content
      chunk = zipfile.read(chunk_size)
      while chunk:
        remainder = onChunk(remainder + chunk)
        chunk = zipfile.read(chunk_size)
        read += chunk_size
        p.onprogress(read)