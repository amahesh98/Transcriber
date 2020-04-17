import argparse
import io
import os
import time

from google.oauth2 import service_account
from google.cloud import speech
from google.cloud.speech import enums, types

credentials = service_account.Credentials.from_service_account_file('keys/GoogleKey.json')

def transcribeFile(speechFile, outputFilePath):
  initializationTime = time.time()

  print("Transcribing song "+speechFile)

  client = speech.SpeechClient(credentials=credentials)

  with io.open(speechFile, 'rb') as audioFile:
    content = audioFile.read()
  
  audio = types.RecognitionAudio(content=content)

  config = types.RecognitionConfig(
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC,
    language_code = 'en-US',
    enable_word_time_offsets = True,
  )

  response = client.recognize(config, audio)

  buffer = []

  for result in response.results:
    alternative = result.alternatives[0]
    transcript = alternative.transcript
    confidence = alternative.confidence

    for wordInfo in alternative.words:
      word = wordInfo.word
      startTime = wordInfo.start_time
      endTime = wordInfo.end_time
      buffer.append(f'{word} - {startTime.seconds + startTime.nanos * 1e-9}\n')

  if not os.path.exists('transcribedSongs'):
      os.mkdir('transcribedSongs')

  print("Finished transcribing song in "+str(time.time() - initializationTime) + ' seconds.')
  outputFile = open(outputFilePath, 'w')
  outputFile.write("".join(buffer))
  outputFile.close()
  print("Writing to transcribedSongs/rachel.out")

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument(dest='audioFilePath', help="Enter the path to the .FLAC file. Maximum length must be 60 seconds and it must be Mono (not stereo).\nUse command: ./trim [args]+ to trim file.")
  args = parser.parse_args()
  outputFilePath= 'transcribedSongs/' + args.audioFilePath[args.audioFilePath.rfind('/') + 1:len(args.audioFilePath)-5] + '.out'
  
  # transcribeFile('./testFiles/sickoMode_trimmed.flac')
  transcribeFile('audioFiles/' + args.audioFilePath, outputFilePath)