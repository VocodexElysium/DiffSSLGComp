import os
from pydub import AudioSegment

def trim_wav_files(root_dir, max_duration_sec=10):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".wav"):
                file_path = os.path.join(subdir, file)
                try:
                    audio = AudioSegment.from_wav(file_path)
                    duration_sec = len(audio) / 1000.0
                    if duration_sec > max_duration_sec:
                        trimmed_audio = audio[:max_duration_sec * 1000]
                        trimmed_audio.export(file_path, format="wav")
                        print(f"Trimmed: {file_path} to {max_duration_sec}s")
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")

trim_wav_files("/scratch/work/guy2/DiffSSLGComp/data")