import torch
from TTS.api import TTS
# from pprint import pprint

# Get device
# device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
# pprint(TTS().list_models())

# Init TTS with the target model name
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False, gpu=True)

# Run TTS
@torch.compile
def fn():
    tts.tts_to_file(
        text="This is some sample text for User Empathy Day", 
        ile_path="/home/xmfan/empathy/coqui-ai-TTS/out_compiled.wav"
    )

fn()
