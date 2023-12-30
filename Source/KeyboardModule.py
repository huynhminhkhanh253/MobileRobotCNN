import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))

keyValue = 0

def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()

    return ans

def main():
    if getKey('UP'):
        print('Key Up was pressed')
    if getKey('DOWN'):
        print('Key Down was pressed')
    if getKey('LEFT'):
        keyValue = 0.3
        print('Key Left was pressed')
    if getKey('RIGHT'):
        keyValue = -0.3
        print('Key Right was pressed')

if __name__ == '__main__':
    init()
    while True:
        main()