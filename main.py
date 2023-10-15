import os
import random
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

command_dict = {
    'commands': {
        'greeting': ['Привет друг','Привет', 'Хай', 'Приветствую'],
        'create_note': ['Добавить заметку', 'Заметка', 'Создать заметку'],
        'play_music': ['Включи музыку', 'Музыку', 'Музыка']
    }
}


def listen_command():
    """The function will return the recognized command"""

    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').capitalize()
        return query
    except speech_recognition.UnknownValueError:
        return 'Damm... Не понял что ты сказал :/'


def greeting():
    """Greeting function"""
    return 'Привет дружище!'


def create_note():
    """Create a note"""
    print('Какую добавим заметку?')

    query = listen_command()

    with open('notes-list.txt', 'a') as file:
        file.write(f'{query}\n')

    return f'Заметка: "{query}" добавлена в note-list'


def play_music():
    """Play a random mp3 file"""

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


    # if query == 'Привет друг':
    #     print(greeting())
    # elif query == 'Добавить заметку':
    #     print(create_note())
    # elif query == 'Включи музыку':
    #     print(play_music())
    # else:
    #     print('Прожуй потом разговаривай! >:|')


if __name__ == '__main__':
    main()
