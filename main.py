import os
import time
import random
import speech_recognition
from voice_output_gtts import speaker_assistant

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

command_dict = {
    'commands': {
        'greeting': ['привет ника', 'привет', 'хай', 'приветствую'],
        'create_note': ['добавить заметку', 'заметка', 'создать заметку'],
        'play_music': ['включи музыку', 'музыку', 'музыка']
    }
}


def listen_command():
    """The function will return the recognized command"""

    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return speaker_assistant('Я не поняла, пожалуйста повторите команду')


def greeting():
    """Greeting function"""
    return speaker_assistant('Привет! Я говорящий ассистент. Меня зовут Николь или просто Ника')


def create_note():
    """Create a note"""
    # print('Какую добавим заметку?')
    speaker_assistant('Слушаю! Какую добавить заметку?')
    # time.sleep(5)
    query = listen_command()

    with open('notes-list.txt', 'a') as file:
        file.write(f'{query}\n')

    return speaker_assistant(f'Я записала, Вы добавили заметку: {query}')

    # return f'Заметка: "{query}" добавлена в note-list'


def play_music():
    """Play a random mp3 file"""
    speaker_assistant('Хорошо включаю')
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open {random_file}')
    return f'Танцуй под {random_file.split("/")[-1]}'


def main():
    # print(globals()) - это глобальная функция
    query = listen_command()

    for k, v in command_dict['commands'].items():
        if query in v:
            print(globals()[k]())


if __name__ == '__main__':
    main()
