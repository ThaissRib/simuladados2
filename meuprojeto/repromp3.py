from pygame import mixer
mixer.init()
#usuario vai colocar a pasta(depois de add no pycharm)#
m = input('coloque a pasta: ')
print(mixer.music.load(m))
mixer.music.play()
x = input('Pode parar a música?')
mixer.music.unload()
p = input('Coloque outra música: ')
print(mixer.music.load(p))
mixer.music.play()
input('deseja parar a música? ')
#ainda falta muita coisa para melhorar#





