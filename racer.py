#!/usr/bin/env python
"""
Brownian motion racer used to determine if myself or my roomate get the big
bedroom in our new apartment. First node to find the big bedroom wins!
(Technically this is not Brownian motion but a much simpler random walk,
 it gets the job done though)
"""

#import random
import numpy.random as random
import pygame

def main():
    # Get name 1
    s = raw_input("Roomate one: ")
    name1 = s
    # Get name 2
    s = raw_input("Roomate two: ")
    name2 = s
    apartment = Apartment(name1, name2)
    # Run simulation
    winner = False;
    while not winner:
        apartment.Step()
        apartment.Draw()
        winner = apartment.Victory()
    # Declair Victory
    print winner + " Wins!"

class Apartment():

    def __init__(self, name1, name2):
        # Sets up roomates and map.
        STARTx = 250
        STARTy = 410
        self.node1 = {'x': STARTx, 'y': STARTy, 'name': name1, 'trail': [(250,400)]}
        self.node2 = {'x': STARTx, 'y': STARTy, 'name': name2, 'trail': [(250,400)]}
        self.Map = ((70,70),(570,70), (570, 410), (70, 410))
        self.victory_square = (70,70,120,120)      
        self.vict_rect = pygame.Rect(70, 70, 50, 50)
        # Draw stuff 
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))

    def Victory(self):
        if self.vict_rect.collidepoint(self.node1['x'], self.node1['y']):
            return self.node1['name']
        if self.vict_rect.collidepoint(self.node2['x'], self.node2['y']):
            return self.node2['name']
        else:
            return False

    def Draw(self):
        self.window.fill((0,0,0))
        # Draw Apartment
        pygame.draw.line(self.window, (255,0,0), self.Map[0], self.Map[1])
        pygame.draw.line(self.window, (255,0,0), self.Map[1], self.Map[2])
        pygame.draw.line(self.window, (255,0,0), self.Map[2], self.Map[3])
        pygame.draw.line(self.window, (255,0,0), self.Map[3], self.Map[0])

        # Draw Victory Box
        pygame.draw.rect(self.window, (255,255,255), self.vict_rect)

        # Draw Players (trail and node)
        pygame.draw.lines(self.window, (0,255,0), False, self.node1['trail'])
        pygame.draw.lines(self.window, (0,0,255), False, self.node2['trail'])

        pygame.display.flip()

    def Step(self):
        # Takes two random steps, makes sure that they aren't stepping into
        # walls.
        self.node1['trail'].append((self.node1['x'],self.node1['y']))
        self.node2['trail'].append((self.node2['x'],self.node2['y']))

        # This might need to be more random. The nodes seem to mirror eachother
        # A lot.
        rands = random.random_integers(-5, 5, 4)
        
        f = lambda old,lower,upper,new: lower < new < upper and new or old
        
        new = self.node1['x'] + rands[0]
        self.node1['x'] = f(self.node1['x'],70,570,new)
        new = self.node1['y'] + rands[1]
        self.node1['y'] = f(self.node1['y'],70,410,new)
        new = self.node2['x'] + rands[2]
        self.node2['x'] = f(self.node2['x'],70,570,new)
        new = self.node2['y'] + rands[3]
        self.node2['y'] = f(self.node2['y'],70,410,new)

if __name__ == '__main__':
    main()
