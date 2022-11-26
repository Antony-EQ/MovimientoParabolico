import sys, os
import pygame
from math import *
import random


#CONSTANTES
V_ANCHO = 800
V_ALTO = 600
V_TAM = (V_ANCHO,V_ALTO)

FPS =100
clock = pygame.time.Clock()


# COLORES
cVerde = (0,255,0)
cNegro = (0,0,0)
cBlanco = (255,255,255)
cRojo = (255,0,0)


#INICIALIZACION
pygame.init()

pygame.display.set_caption("Movimiento Parabolico")
screen=pygame.display.set_mode(V_TAM,0,32)
screen.fill(cBlanco)

def main():
    #VERDE
    delta = 20 
    Vi = 50
    Vix = Vi *cos(radians(delta))
    Viy = Vi*sin(radians(delta))
    #NEGRO
    deltaN = -65
    ViN = 50
    VixN = Vi * cos(radians(deltaN))
    ViyN = Vi *  sin(radians(deltaN))
    
    #ROJO
    deltaR = 20 
    ViR = 50
    VixR = Vi *cos(radians(deltaR))
    ViyR = Vi*sin(radians(deltaR))
    
    Yf = 0
    Xf = 0
    Yfr = 0
    Xfr = 0
    Yfn = 0
    Xfn = 0
    Xi = 0 
    XiN = 0
    x = 0
    y=150
    t = 0
    t1 = 0
    t2 = 0
    dt = 0.05
    g = -9.8
    
    Cx = 150
    Cy = 150
    
    posVx = 150
    posVy = 150
    
    posNy = 150
    posNx=0
    
    posRy = 150
    posRx=310
    
    Rx= 310
    Ry=150
    Ly=150
    Lx=310
    Lxf=310
    trayecto=[]
    trayecto1=[]
    trayecto2=[]
    while True:
        
        screen.fill(cBlanco)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
         
        pNegro = pygame.draw.circle(screen, cNegro, (x+Xfn,y-Yfn), 10)
        pVerde = pygame.draw.circle(screen, cVerde, (Cx+Xf,Cy-Yf), 10)
        pygame.draw.line(screen, cNegro, (0,550), (800,550))
        pygame.draw.line(screen, cNegro, (0,160), (150,160))
        pygame.draw.line(screen, cNegro, (150,160), (360,550))
        linea =  pygame.draw.line(screen, cRojo, (Lx,0), (Lxf,Ly),3)
        pRojo = pygame.draw.circle(screen, cRojo, (Rx+Xfr,Ry-Yfr), 10)
        x=x+1
        
       
        
        if(x==140):
            posNx = 140           
        posN = (posNx,posNy)
        posV =(posVx,posVy)
        
        if(posNx==140):
            if(Yfn>=-390):
                Yfn = ViyN*t1 + 0.5*g*t1**2
                Xfn = XiN+VixN*t1
                t1 = t1 + dt 
            
            if(Yf>=-390):                   
                Yf = Viy*t + 0.5*g*t**2
                Xf = Xi+Vix*t
                t = t + dt
                

                posVx=posVx+1
                if(posVx>=215):
                    Rx=Rx+1
                    Ry=Ry-1
                    Lxf=Lxf+1
                    Ly=Ly-1


        trayecto.append((Cx+Xf,Cy-Yf))
        for punto in trayecto:
            pygame.draw.circle(screen, cVerde, punto, 1)
        
            
       
        
        pygame.display.update()

        clock.tick(FPS)

if __name__=="__main__":
    main()


