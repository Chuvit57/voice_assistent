import pyttsx3

# engine = pyttsx3.init()  # — это метод, который необходимо вызвать для инициализации движка.
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-150)
# engine.say('Hi everyone, my name is Vitaly')
# # engine.say('Привет ребята! Меня зовут Виталий')
#
# engine.runAndWait()


speaker = pyttsx3.init()
speaker.setProperty('rate', 100)
speaker.setProperty('volume', 0.9)
voices = speaker.getProperty('voices')

# Получение списка из доступных языков
# for index, voice in enumerate(voices):
#     print(f'Index: {index}\nVoice: {voice.name}\n{"#" * 20}')

# for voice in voices:
#     print('------------------------')
#     print(f'Имя: {voice.name}')
#     print(f'ID:{voice.id}')
#     print(f'Язык:{voice.languages}')
#     print(f'Пол:{voice.gender}')
#     print(f'Возраст:{voice.age}')

ru_voices_id = 'russian'
speaker.setProperty('voice', ru_voices_id)
speaker.say('Привет ребята')

# speaker.setProperty('voice', voices[61].id)
# speaker.say('Привет друг')
speaker.runAndWait()
