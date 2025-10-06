from TTS import TTS
from STT import STT
from procesor import procesor
import pygame
import os


def Action():
    voice_input: str = STT()

    # remove symbols
    voice_input = voice_input.replace("?", "")
    voice_input = voice_input.replace("¿", "")
    voice_input = voice_input.replace(",", "")
    voice_input = voice_input.replace(".", "")
    voice_input = voice_input.casefold()
    commands = voice_input.split(" ")
    respuesta = procesor(commands)
    TTS(respuesta)


pygame.init()
running = True
screen = pygame.display.set_mode((700, 700))
micro = pygame.image.load("microfono.png")
pending = False

while running:
    screen.fill((220, 220, 255))
    color = (113, 224, 99) if pending else (0, 0, 0)
    pygame.draw.circle(screen, color, [350, 350], 280)
    screen.blit(micro, [94, 94])
    if os.path.exists("audios/salida_TTS.wav"):
        audio = pygame.mixer.Sound("audios/salida_TTS.wav")
        audio.play()
        os.remove("audios/salida_TTS.wav")

    if not pygame.mixer.get_busy():
        pending = False
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not pending:
                    screen.fill((220, 220, 255))
                    pygame.draw.circle(screen, (216, 230, 90), [350, 350], 280)
                    screen.blit(micro, [94, 94])
                    pygame.display.update()
                    Action()
                    pending = True

pygame.quit()
