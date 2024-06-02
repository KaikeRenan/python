# crie um programa que abara e reproduza o áudio de um arquivo MP3

from pygame import mixer

mixer.init()
mixer.music.load('July - John Patitucci.mp3')
mixer.music.play()

x = input('Digite algo para parar...')