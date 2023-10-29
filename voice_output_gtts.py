from gtts import gTTS
import pygame
import tempfile
import time
from datetime import datetime, date, time

time_checker = datetime.now()


# Создание экземпляра класса gTTS

def speaker_assistant(text):
    tts = gTTS(text, lang='ru')
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts.save(temp_file.name)
    pygame.init()
    pygame.mixer.music.load(temp_file.name)
    pygame.mixer.music.load(temp_file.name)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

# Это пример с сохранением записи в файл----------------------------------------------
# Сохранение аудио во временный файл
# tts.save('tts_google1.mp3')
#
# # Загрузка аудиофайла в pygame
# pygame.mixer.music.load('tts_google1.mp3')


# # Сохранение аудио во временный файл -----------------------------------
# temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
# tts.save(temp_file.name)

# Инициализация библиотеки pygame
# pygame.init()

# Загрузка аудиофайла в Pygame
# pygame.mixer.music.load(temp_file.name)

# Воспроизведение аудио
# pygame.mixer.music.play()

# Ожидание окончания проигрывания
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)

# Удаление временного файла
# pygame.mixer.music.stop()
# pygame.mixer.quit()


# speaker_assistant(f"Привет! Я говорящий ассистент. Меня зовут Николь или просто Ника. Сейчас: {time_checker.hour} часа "
#         f"{time_checker.minute} минут")
