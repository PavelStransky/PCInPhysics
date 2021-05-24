import sounddevice as sd
import soundfile as sf

def Read(file):
    sound, fs = sf.read(file, dtype='float32')
    return sound, fs

def Play(sound, fs):
    sd.play(sound, fs)
    sd.wait()
