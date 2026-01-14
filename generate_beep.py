from pydub import AudioSegment
from pydub.generators import Sine

# Generate a 1000 Hz sine wave for 500 ms
beep = Sine(1000).to_audio_segment(duration=500)

# Export as WAV
beep.export("beep.wav", format="wav")
