import soundfile as sf
sample_rate = sf.read("chirpingbirds.wav")
print(f"Sample rate: {sample_rate[1]} Hz")