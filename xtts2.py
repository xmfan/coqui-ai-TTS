import torch
from TTS.api import TTS
import time

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
# print(TTS().list_models())

# Init TTS
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
def fn():
    # Text to speech to a file
    # tts.tts_to_file(text="Hello from XTTS2", speaker_wav="en_sample.wav", language="en", file_path="out_xtts2.wav")

    # Text to speech list of amplitude values as output
    tts.tts(text="Hello from XTTS2. I am being tested for the torch.compile User Empathy Day on Nov 20th 2024.", speaker_wav="en_sample.wav", language="en")

def warmup(its=5):
    for i in range(its):
        start = time.time()
        fn()
        duration = time.time() - start
        print(f"warm up i={i} took {duration}s")

def bench(its=30):
    total = 0
    for i in range(its):
        start = time.time()
        fn()
        duration = time.time() - start
        print(f"bench i={i} took {duration}s")
        total += duration
    print(f"avg runtime={total/its}s")

print("bench eager")
warmup()
bench()

# need to compile after loaded
print("bench compiled")
tts.synthesizer.tts_model.gpt = torch.compile(tts.synthesizer.tts_model.gpt)
warmup()
frozen = torch._dynamo.run(bench)
frozen()
