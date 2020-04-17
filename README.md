**Steps:**

0. Place desired audio file in the audioFiles folder.
1. Convert song to mono FLAC from using ./convert [args]
2. Trim song use ./trim [args] to fit length to 1 minute (choose start and end points)
3. Run python3 transcribe.py [path to song]
4. Run python3 describe.py [transcribed song name]
