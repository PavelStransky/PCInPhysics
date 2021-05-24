import sounddevice as sd
import soundfile as sf

def Read(file):
    sound, fs = sf.read(file, dtype='float32')
    return sound, fs

def Play(sound, fs):
    sd.play(sound, fs)
    sd.wait()

if __name__ == "__main__":
    Play(*Read("../../sounds/a.wav"))