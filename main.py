import os
import sys
from selenium import webdriver
from datetime import datetime
import random
import speech_recognition
from voice_output_gtts import speaker_assistant

chrome_driver_path = '~/Vitaly Education/Python_projects/voice_assistent/chromedriver'
# Настройте переменную окружения PATH со ссылкой на путь к драйверу Chrome
os.environ['PATH'] += ':' + chrome_driver_path


# sr = speech_recognition.Recognizer()
# sr.pause_threshold = 0.5

command_dict = {
    'commands': {
        'greeting': ['привет ника', 'привет', 'хай', 'приветствую'],
        'create_note': ['добавить заметку', 'заметка', 'создать заметку'],
        'play_music': ['включи музыку', 'музыку', 'музыка'],
        'time_now': ['время', 'который час'],
        'restart_pc': ['перезагрузка', 'перезагрузить компьютер'],
        'cansel_restart_pc': ['отмена перезагрузки'],
        'open_browser': ['браузер', 'открыть браузер'],
        'exit': ['выход', 'завершение работы']
    }
}


def listen_command():
    """The function will return the recognized command"""
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5

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


def time_now():
    time_checker = datetime.now()
    speaker_assistant(f"Сейчас питерское время: {time_checker.hour} точка {time_checker.minute} ")


def play_music():
    """Play a random mp3 file"""
    speaker_assistant('Хорошо включаю')
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open {random_file}')
    return f'Танцуй под {random_file.split("/")[-1]}'


def restart_pc():
    os.system('shutdown -r +5')
    speaker_assistant('Компьютер будет перезагружен через 5 минут. Для отмены скажите: отмена')


def cansel_restart_pc():
    os.system('shutdown -c')
    speaker_assistant('Перезагрузка компьютере успешно отменена')


def open_browser():
    speaker_assistant('Какую страницу вы хотите открыть?')

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome()

    driver.implicitly_wait(1)
    driver.maximize_window()

    query = listen_command()

    if 'google' in query:
        speaker_assistant('Что будем искать?')

        query = listen_command()
        query = query.split()

        driver.get('https://www.google.com/search?q=' + '+'.join(query))
        speaker_assistant(f'Поиск по {query} успешно запущен')

    elif 'youtube' in query:
        speaker_assistant('Что будем смотреть?')

        query = listen_command()
        query = query.split()

        driver.get('https://www.youtube.com/results?search_query=' + '+'.join(query))
        speaker_assistant('Приятного просмотра')

        return

    else:
        speaker_assistant('Не понял тебя')

        return


def exit():
    speaker_assistant('Спасибо! До свидание')
    sys.exit()


# while True:
#     listen_command()
#     for k, v in command_dict['commands'].items():
#         if query in v:
#             execute = getattr()
#
#     except Exception as _ex:
#     print('Команда не распознана')
#     sys,exit()


def main():
    listen_command()
    for k, v in command_dict['commands'].items():
        if listen_command() in v:
            print(globals()[k]())


if __name__ == '__main__':
    main()
