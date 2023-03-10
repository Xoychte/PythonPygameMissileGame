
#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import*
from math import*
from random import randint
from constr import *
# Initialisation des variables
(width, height) = (800, 600)  # definit la height et la width de la fenêtre de l'application
WHITE=(255, 255, 255)   # Définit la couleur blanche
RED=(255,0,0)   #Définit la couleur rouge
BLUE=(0,0,255)
GREEN=(0,200,0)
BLACK=(0,0,0)
YELLOW=(223, 230, 0)
colors=[RED, BLUE, GREEN, BLACK, YELLOW]
missile_x=200   #Définit l'emplacement horizontal du missile
missile_y=height-50   #Définit l'emplacement horizontal du missile

listOfBalls = [Balle()]

balle_rayon=20   # taille de la balle

FPS = 60    #Nombre d'images par secondes
score=0
ballsMissed=0
missileSpeedMultiplier = 1
ballSpeedMultiplier = 1
timer = 0


#Initialisation de la bibliothèque Pygame
pygame.init()
clock = pygame.time.Clock()  # créer un système permettant de gérer le temps
fenetre = pygame.display.set_mode((width, height), RESIZABLE) #Création de la fenêtre redimensionnable
fenetre.fill(WHITE)
missile = pygame.image.load("reworkmissile.png").convert_alpha()
#Chargement image en rendant le blanc de l'image transparent

font_obj = pygame.font.Font('freesansbold.ttf', 12)  #Choix de la police et de sa taille



missile_run = 0

#BOUCLE INFINIE
continuer = True
pygame.key.set_repeat(10,10)
while continuer:
    fenetre.fill(WHITE)
    
    mouseX, mouseY =  pygame.mouse.get_pos()

    clock.tick(FPS)   

    text1_obj = font_obj.render('Score: '+str(score), True, RED, WHITE)  #Affichage d'un texte score
    text2_obj = font_obj.render('Perdu: '+str(ballsMissed), True, BLUE, WHITE)
    text3_obj = font_obj.render('Vitesse du missile / '+str(missileSpeedMultiplier), True, BLUE, WHITE)
    text4_obj = font_obj.render('Vitesse de la balle * '+str(ballSpeedMultiplier), True, RED, WHITE)
    text5_obj = font_obj.render('RESET', True, RED, WHITE)
    if missile_run == 1:
        missile_y -= 10 / missileSpeedMultiplier
        
        if missile_y < 0:
            missile_run = 0
            missile_y = height-50

    
 
    
    
    
    

    for event in pygame.event.get() :   #On parcours la liste de tous les événements reçus


        if event.type == QUIT:      #Si un de ces événements est de type QUIT (Alt+F4) ou bouton fermeture
            continuer = False       #On arrête la boucle
        keys = pygame.key.get_pressed() # Si touche appuyée

        if keys[pygame.K_LEFT] and missile_run == 0 and missile_x > 0:
            missile_x += -7

        elif keys[pygame.K_RIGHT] and missile_run == 0 and missile_x < 775:
            missile_x += 7

        elif keys[pygame.K_UP] and missile_run == 0:
            missile_run = 1

        elif keys[pygame.K_d]:
            timer += 1
            if timer == 1:
                listOfBalls.append(Balle())
            elif timer == 15:
                timer = 0
            
            
            
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouseX)
            if 0 < mouseY < 20:
                if 400 < mouseX < 532:

                    missileSpeedMultiplier += 0.5
                elif 600 < mouseX < 719:
                    print("Vitesse balle up")
                    ballSpeedMultiplier += 0.5
                elif 750 < mouseX < 800:
                    print("reset")
                    ballsMissed = 0
                    score = 0
                    ballSpeedMultiplier = 1
                    missileSpeedMultiplier = 1
                    listOfBalls.clear()
                    listOfBalls.append(Balle())

    for i in listOfBalls:     #On passe par toutes les balles
        
        if i.y > height :     #Quand la balle atteint le bas
            ballsMissed = ballsMissed + 1
            i.speedy = 0
            i.y = 50
        
        i.x=i.x+i.speedx * ballSpeedMultiplier  #rôle:déplacer la balle
        i.y=i.y+i.speedy
        
        if i.x>width-balle_rayon :  #Rebonds sur les bords
            i.speedx=-i.speedx
            i.speedy = randint(0,3)
        if i.x<balle_rayon :
            i.speedx=-i.speedx
            i.speedy = randint(0,3)
        
        dist_y = abs(missile_y - i.y)
        dist_x = abs(missile_x - i.x)
        if dist_y < 25 and dist_x < 25 and missile_run == 1:  #hitbox de la balle
            missile_run = 0
            missile_y = height-50
            i.speedy = 0
            i.y = 50
            score += 1
            i.x = randint(0 + balle_rayon, width - balle_rayon)

        pygame.draw.circle(fenetre,colors[i.color],(int(i.x),i.y),balle_rayon)
            


    fenetre.blit(text1_obj, (10,10))
    fenetre.blit(text2_obj, (100,10))

    fenetre.blit(text3_obj, (400,10))
    fenetre.blit(text4_obj, (600,10))

    fenetre.blit(text5_obj, (750,10))
    fenetre.blit(missile, (missile_x,missile_y))  #collage de l'image sur la fenêtre

    pygame.display.flip()#Rafraîchissement de l'écran

pygame.quit()
