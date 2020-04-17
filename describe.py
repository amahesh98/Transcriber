import argparse
import os
import time

from pynput.keyboard import Key, Controller


def describe(transcribedSongFile, waitPeriod=3):
  if not os.path.exists('transcribedSongs'):
    print("Transcribed songs do not exist yet. Run transcribe before running describe")

  if not os.path.isfile(transcribedSongFile):
    print ("[ERROR] Transcribed file does not exist")
    exit(0)

  # print("Describing: ", transcribedSongFile)

  keyboard = Controller()
  # time.sleep(waitPeriod)

  # for i in range(0, 10):
  #   keyboard.press('a')
  #   keyboard.release('a')
  #   keyboard.press('b')
  #   keyboard.release('b')

  transcribedSong = open(transcribedSongFile)
  words = []
  times = []
  for line in transcribedSong:
    splitLine = line.split(' ')
    words.append(splitLine[0])
    times.append(splitLine[2][:len(splitLine[2])-1])
  
  print("Words:", words)
  print("Times:", times)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument(dest='transcribedFile', help='Enter file prefix of transcribed file. Path not needed.')
  args = parser.parse_args()

  transcribedFile = 'transcribedSongs/'+args.transcribedFile+'.out'
  describe(transcribedFile)