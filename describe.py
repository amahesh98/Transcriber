import argparse
import os
import time

from pynput.keyboard import Key, Controller

def describe(transcribedSongFile, waitPeriod=3):
  startTime = time.time()
  if not os.path.exists('transcribedSongs'):
    print("Transcribed songs do not exist yet. Run transcribe before running describe")
    exit(0)

  if not os.path.isfile(transcribedSongFile):
    print ("[ERROR] Transcribed file does not exist")
    exit(0)

  keyboard = Controller()
  print("Describing song  "+transcribedSongFile)
  print("Start playing music once the BEGIN appears")
  transcribedSong = open(transcribedSongFile)
  words = []
  times = []
  for line in transcribedSong:
    splitLine = line.split(' ')
    words.append(splitLine[0])
    times.append(float(splitLine[2][:len(splitLine[2])-1]))
  
  timeDifferentials = [times[0]]
  for i in range(1, len(times)):
    differential = times[i] - times[i-1]
    timeDifferentials.append(differential)

  time.sleep(waitPeriod)
  print("BEGIN")
  time.sleep(0.4)
  for i in range(0, len(words)):
    time.sleep(timeDifferentials[i])
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    keyboard.type(words[i] + ' ')

  keyboard.press(Key.enter)
  keyboard.release(Key.enter)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument(dest='transcribedFile', help='Enter file prefix of transcribed file. Path not needed.')
  args = parser.parse_args()

  transcribedFile = 'transcribedSongs/'+args.transcribedFile+'.out'
  describe(transcribedFile, waitPeriod=2)