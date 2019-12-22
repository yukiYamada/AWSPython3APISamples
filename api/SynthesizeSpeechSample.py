import polly as pl

audioStream = pl.SynthesizeSpeech.execute("default")
output = "speech.mp3"
file = open(output, 'wb')
file.write(audioStream.read())


