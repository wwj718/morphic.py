import pygame
for i in dir(pygame): 
    try: 
        print(i,":", getattr(pygame, i))
    except:
        pass
