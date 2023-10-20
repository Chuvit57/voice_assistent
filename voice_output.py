import pyttsx3

engine = pyttsx3.init()  # — это метод, который необходимо вызвать для инициализации движка.
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-150)
engine.say('Hi everyone, my name is Vitaly')
# engine.say('Привет ребята! Меня зовут Виталий')

engine.runAndWait()