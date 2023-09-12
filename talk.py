from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
import os


class Talk():
  # download and load all models
  # preload_models() (SEEING IF LOADING ONLY ON RUN HELPS WITH VRAM)

  def run(self, text_prompt):
    preload_models()
    audio_array = generate_audio(text_prompt, history_prompt="v2/en_speaker_9")

    # save audio to disk
    write_wav("new.wav", SAMPLE_RATE, audio_array)
      
    # play text in notebook
    Audio(audio_array, rate=SAMPLE_RATE)