import argparse
import io

from google.oauth2 import service_account
from google.cloud import speech
from google.cloud.speech import enums, types

credentials = service_account.Credentials.from_service_account_file('keys/GoogleKey.json')

def transcribeFile(speechFile):
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

  for result in response.results:
    alternative = result.alternatives[0]
    transcript = alternative.transcript
    confidence = alternative.confidence
    for wordInfo in alternative.words:
      word = wordInfo.word
      startTime = wordInfo.start_time
      endTime = wordInfo.end_time
      print(f'{word} - {startTime.seconds + startTime.nanos * 1e-9}')

if __name__ == '__main__':
  transcribeFile('./testFiles/sickoMode_trimmed.flac')