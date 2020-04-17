**Steps:**

**If the song is under 1 minute**

1. run ./transcribe [youtube-url][song-name]
2. Run python3 describe.py [song-name]

**If the song is longer than 1 minute**

1. run ./downloadAndConvert [youtube-url][song-name]
2. Trim song use ./trim [args] to fit length to 1 minute (choose start and end points)
3. Run python3 transcribe.py [song-name].flac
4. Run python3 describe.py [song-name]
