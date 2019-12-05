import polly as pl

audioStream = pl.SynthesizeSpeech.execute()
output = "speech.mp3"
file = open(output, 'wb')
file.write(audioStream.read())


