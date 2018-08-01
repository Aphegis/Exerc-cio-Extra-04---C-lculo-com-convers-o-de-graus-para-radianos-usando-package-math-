from pygame import mixer
mixer.init()
mixer.music.load('bby.mp3')
mixer.music.play()
input()
mixer.event.wait()



