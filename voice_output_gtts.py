from gtts import gTTS
import pygame
import os
import tempfile

# Создание экземпляра класса gTTS
text = "Привет! Я говорящий ассистент. Меня зовут Николь или просто ника"
tts = gTTS(text, lang='ru')

# Это пример с сохранением записи в файл----------------------------------------------
# Сохранение аудио во временный файл
# tts.save('tts_google1.mp3')
#
# # Загрузка аудиофайла в pygame
# pygame.mixer.music.load('tts_google1.mp3')


# Сохранение аудио во временный файл -----------------------------------
temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
tts.save(temp_file.name)

# Инициализация библиотеки pygame
pygame.init()

# Загрузка аудиофайла в Pygame
pygame.mixer.music.load(temp_file.name)

# Воспроизведение аудио
pygame.mixer.music.play()

# Ожидание окончания проигрывания
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Удаление временного файла
pygame.mixer.music.stop()
pygame.mixer.quit()
