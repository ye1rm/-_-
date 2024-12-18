import os
import threading
from gtts import gTTS
import pygame

# 알파벳 사운드 캐싱 딕셔너리
cached_sounds = {}

# TTS 음성 파일 저장 폴더
SOUND_DIR = "sounds"
if not os.path.exists(SOUND_DIR):
    os.makedirs(SOUND_DIR)

# tts효과음 전용 채널 생성
#effect_channel = pygame.mixer.Channel(1)  # 채널 1번에 tts효과음을 할당

def generate_tts_file(word):
    """TTS 음성 파일 생성 함수 (별도 스레드에서 실행)"""
    tts_path = os.path.join(SOUND_DIR, f"{word}.wav")
    if not os.path.exists(tts_path):  # 이미 파일이 생성되어 있다면 재생성하지 않음
        tts = gTTS(text=word, lang='en')
        tts.save(tts_path)
    return tts_path


def play_tts_sound(word):
    """알파벳 발음 생성 및 재생"""
    # 음성 파일 경로
    tts_path = os.path.join(SOUND_DIR, f"{word}.wav")

    # 음성이 캐싱되어 있지 않으면 생성 (백그라운드 스레드에서 처리)
    if word not in cached_sounds:
        if not os.path.exists(tts_path):
            # 음성 파일 생성 (백그라운드에서 실행)
            thread = threading.Thread(target=generate_tts_file, args=(word,))
            thread.start()
            thread.join()  # 생성이 완료될 때까지 대기

        # pygame.mixer.Sound로 캐싱
        cached_sounds[word] = pygame.mixer.Sound(tts_path)

    # 캐싱된 음성 재생
    sound = cached_sounds[word]
    sound.play()

    
    # def generate_and_play():

    #     sound_file = f"cache/{word}.wav"  # WAV 파일 경로

    #     # 디렉토리가 없으면 생성
    #     if not os.path.exists("cache"):
    #         os.makedirs("cache", exist_ok=True)

    #     # 파일이 없으면 생성
    #     if word not in cached_sounds:
    #         if not os.path.exists(sound_file):
    #             tts = gTTS(text=word, lang='en')
    #             tts.save(sound_file)  # WAV 파일로 저장

    #         # 캐싱된 사운드 객체를 pygame.mixer.Sound로 저장
    #         cached_sounds[word] = pygame.mixer.Sound(sound_file)

    #     # 재생할 채널이 None이면 새로운 채널 찾기
    #     if effect_channel is None:
    #         effect_channel = pygame.mixer.find_channel()

    #     if effect_channel:
    #         # 채널에서 재생
    #         effect_channel.play(cached_sounds[word])

    #         # 음성이 끝날 때까지 기다리기
    #         while effect_channel.get_busy():  # 채널이 재생 중이면
    #             pygame.time.Clock().tick(10)  # 10ms마다 상태 확인
    #     else:
    #         print(f"Error: No available channel to play the sound for '{word}'.")

    # # 음성 파일 생성 및 재생을 별도의 스레드에서 처리
    # threading.Thread(target=generate_and_play, daemon=True).start()
