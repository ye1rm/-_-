import pygame
import os
import threading
from gtts import gTTS

# 알파벳 사운드 캐싱 딕셔너리
cached_sounds = {}

# 캐싱된 파일 유지 (알파벳 26개 음성 파일 크기 (MP3): 약 10KB ~ 20KB × 26개 = 260KB ~ 520KB)
# 최대 약 1MB 이내로 모든 알파벳 음성 파일을 저장할 수 있으므로 캐시 파일을 유지하며 빠르게 재사용하는 방식으로 최적화.
def play_tts_sound(word, effect_channel):
    def generate_and_play():
        sound_file = f"cache/{word}.mp3"
        try:
            # 디렉토리가 없으면 생성
            if not os.path.exists("cache"):
                os.makedirs("cache", exist_ok=True)

            # 파일이 없으면 생성
            if word not in cached_sounds:
                if not os.path.exists(sound_file):
                    tts = gTTS(text=word, lang='en')
                    tts.save(sound_file)
                cached_sounds[word] = pygame.mixer.Sound(sound_file)  # Sound 객체 캐싱

            # 사운드 재생 (effect_channel 사용)
            effect_channel.play(cached_sounds[word])
        except Exception as e:
            print(f"Error playing sound for letter '{word}': {e}")

    # 음성 파일 생성 및 재생을 별도의 스레드에서 처리
    threading.Thread(target=generate_and_play, daemon=True).start()