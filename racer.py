#!/usr/bin/env python
"""
Brownian motion racer used to determine if myself or my roomate get the big
bedroom in our new apartment. First node to find the big bedroom wins!
(Technically this is not Brownian motion but a much simpler random walk,
 it gets the job done though)
"""

import random
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
        apartment.step()
        apartment.draw()
        winner = apartment.victory()
    # Declair Victory
    print winner + " Wins!"

STARTx = -5 + 100
STARTy = 0 + 100
# (x,y) bottom left (x,y) upper right
victory_square = (0 + 200,0 + 200,5 + 200,5 + 200)

class Apartment():

    def __init__(self, name1, name2):
        #sets up roomates and map.
        self.node1 = {'x': STARTx, 'y': STARTy, 'name': name1, 'trail': [(0,0)]}
        self.node2 = {'x': STARTx, 'y': STARTy, 'name': name2, 'trail': [(0,0)]}
        self.Map = 1232123212321
       
        # Draw stuff 
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))

    def victory(self):
        if victory_square[0] <= self.node1['x'] <= victory_square[2] \
        and victory_square[1] <= self.node1['y'] <= victory_square[3]:
            return self.node1['name']
        if victory_square[0] <= self.node2['x'] <= victory_square[2] \
        and victory_square[1] <= self.node2['y'] <= victory_square[3]:
            return self.node2['name']
        else:
            return False

    def draw(self):
        self.window.fill((0,0,0))
        # Draw Apartment


        # Draw Players (trail and node)
        pygame.draw.lines(self.window, (255,255,255), False, self.node1['trail'])
        pygame.draw.lines(self.window, (255,255,255), False, self.node2['trail'])

        pygame.display.flip()

    def step(self):
        # Takes two random steps, makes sure that they aren't stepping into
        # walls or eachother.
        self.node1['trail'].append((self.node1['x'],self.node1['y']))
        self.node2['trail'].append((self.node2['x'],self.node2['y']))

        self.node1['x'] += random.randint(-5, 5)
        self.node1['y'] += random.randint(-5, 5)
        self.node2['x'] += random.randint(-5, 5)
        self.node2['y'] += random.randint(-5, 5)

if __name__ == '__main__':
    main()
