import os
import sys
from my_commands import command_dict
from selenium import webdriver
from datetime import datetime
import random
import speech_recognition
from voice_output_gtts import speaker_assistant

chrome_driver_path = '~/Vitaly Education/Python_projects/voice_assistent/chromedriver'
# Настройте переменную окружения PATH со ссылкой на путь к драйверу Chrome
os.environ['PATH'] += ':' + chrome_driver_path


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


def create_note():
    """Create a note"""
    speaker_assistant('Слушаю! Какую добавить заметку?')
    query = listen_command()

    with open('notes-list.txt', 'a') as file:
        file.write(f'{query}\n')

    return speaker_assistant(f'Я записала, Вы добавили заметку: {query}')


def time_now():
    time_checker = datetime.now()
    return speaker_assistant(f'Сейчас питерское время: {time_checker.hour} точка {time_checker.minute}')


def play_music():
    """Play a random mp3 file"""
    speaker_assistant('Хорошо включаю')
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open {random_file}')
    return f'Танцуй под {random_file.split("/")[-1]}'


def restart_pc():
    os.system('shutdown -r +5')
    return speaker_assistant('Компьютер будет перезагружен через 5 минут. Для отмены скажите: отмена')


def cancel_restart_pc():
    os.system('shutdown -c')
    return speaker_assistant('Перезагрузка компьютера успешно отменена')


def exit():
    return speaker_assistant('Спасибо! До свидания')


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
        return speaker_assistant(f'Поиск по {query} успешно запущен')

    elif 'youtube' in query:
        speaker_assistant('Что будем смотреть?')
        query = listen_command()
        query = query.split()
        driver.get('https://www.youtube.com/results?search_query=' + '+'.join(query))
        return speaker_assistant('Приятного просмотра')

    else:
        return speaker_assistant('Не понял тебя')


class Assistant:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        """Greeting function"""
        return speaker_assistant(f'Привет! Я говорящий ассистент. Меня зовут {self.name}')

    def main(self):
        while True:
            query = listen_command()
            if self.name.lower() in query.lower():
                command = query.lower().replace(self.name.lower(), '').strip()
                if command:
                    command_matched = False
                    for k, v in command_dict['commands'].items():
                        if command in v:
                            if k == 'exit':
                                return exit


if __name__ == '__main__':
    assistant = Assistant(name="Assistant")
    assistant.main()
