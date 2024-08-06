import sounddevice as sd
import wavio

def record_audio(duration, sample_rate, filename):
    print("Recording...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    
    wavio.write(filename, recording, sample_rate, sampwidth=2)
    print(f"Saved recording as {filename}")

if __name__ == "__main__":
    duration = float(input("Enter the duration of the recording in seconds: "))
    sample_rate = 44100  # Sample rate in Hz
    filename = "recor.wav"
    
    record_audio(duration, sample_rate, filename)