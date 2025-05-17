#import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


# sampling frequency
freq = 44100

#Recording duration
duration = 5

#start recorder with the given values
#of duration and sample frequency

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

#Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)

#convert the numpy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)
