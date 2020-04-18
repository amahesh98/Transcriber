**Steps:**

**If the song is under 1 minute**

1. run ./transcribe [youtube-url][song-name]
2. Run python3 describe.py [song-name]

**If the song is longer than 1 minute**

1. run ./downloadAndConvert [youtube-url][song-name]
2. Trim song use ./trim [song-name][start-time][duration] to fit length to 1 minute (choose start and end points)
3. Run python3 transcribe.py [song-name]\_trimmed.flac
4. Run python3 describe.py [song-name]
