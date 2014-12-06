#!/usr/bin/python
##################################
# File Name: Game.py
# Author: 	 Group 3
# Date: 	 11/10/2014
# Class:	 CS360
# Assignment:Jungle Jamboree
# Purpose: 	 Game class
##################################

import pygame 
from pygame.locals import *
from Party import *
from Store import *
import sys

"""
The Game Module
"""

class Game :

	def __init__(self) :
		"""sets running to true, and creates a party and begins setting
		 up a pygame display """
		self._running = True
		self._display = None
		self._party = Party()
		self._store = Store ()
		self._store.setUpStore ()
		#self._party.setUpParty () #don't forget to add this not in init
		self._state = "Start"
		self._width = 800
		self._height = 600
		self._size = (self._width, self._height)
		pygame.init()
		self._display = pygame.display.set_mode(self._size)
		self._myFont1 = pygame.font.Font('freesansbold.ttf', 15)
		self._myFont2 = pygame.font.Font('freesansbold.ttf', 25)
		self._myFont3 = pygame.font.Font('freesansbold.ttf', 12)
		pygame.display.set_caption('Jungle Jamboree')
	
	def on_loop (self):
		self._display.blit(imgStart, (imgx,imgy))
		self._display.blit(start, (400,400))
		while(True):
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				#allows you to see what the last input was in the geany output window
				print event

				#called when you hit the X
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
					
				if self._state == "Start":
					self.startButton (mouse, event)
															
				elif self._state == "Store":
					self.store (mouse, event)
										
				elif self._state == "Home":
					self.home (mouse, event)
									
				elif self._state == "Inventory":
					self.inventory (mouse, event)
					
				elif self._state == "Party":
					self.party (mouse, event)

			#the update for the screen		
			pygame.display.update()
			
	def startButton (self, mouse, event) :
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 395, 460, 395, 415) :
				self._state = "Store"
							
	def store (self, mouse, event) :
		self._display.blit(imgStore, (imgx, imgy))
		self._display.blit(funds, (297, 279))
		self._display.blit(leave1, (20, 279))
		self.displayInventory (self._store, mouse, event)
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 20, 60, 279, 291) :
				self._state = "Home"
							
	def home (self, mouse, event) :
		self._display.blit(imgJungle, (imgx, imgy))
		self._display.blit(imgPerson1, (imgxP1, imgyP1))
		self._display.blit(imgPerson2, (imgxP2, imgyP2))
		self._display.blit(imgPerson3, (imgxP3, imgyP3))
		self._display.blit(imgPerson4, (imgxP4, imgyP4))
		self._display.blit(imgPerson5, (imgxP5, imgyP5))
		self._display.blit(store, (10, 380))
		self._display.blit(forage, (10, 410))
		self._display.blit(inventory, (10, 440))
		self._display.blit(party, (10, 470))
		self._display.blit(day, (170, 205))
		self._display.blit(distance, (170, 225))
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 8, 95, 380, 405) :
				self._state = "Store"
		
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 8, 160, 440, 465) :
				self._state = "Inventory"
				
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 8, 95, 470, 500) :
				self._state = "Party"
		
	def inventory (self, mouse, event) :
		self._display.blit(imgInventory, (imgx, imgy))
		self._display.blit(leave2, (20, 279))
		self.displayInventory (self._party.getInventory(), mouse, event)
		if event.type == MOUSEBUTTONDOWN:
			if self.checkMouse (mouse, 26, 60, 279, 291) :
				self._state = "Home"

	def checkMouse (self, mouse, left, right, top, bottom):
		isIn = False
		if mouse[0]	> left and mouse[0] < right \
		and mouse[1] > top and mouse[1] < bottom :
			isIn = True
		return isIn
		
	def party (self, mouse, event):
		self._display.blit(imgParty, (imgx, imgy))
		self._display.blit(imgPerson1, (15, 15))
		self._display.blit(imgPerson2, (15, 215))
		self._display.blit(imgPerson3, (15, 415))
		self._display.blit(imgPerson4, (400, 15))
		self._display.blit(imgPerson5, (400, 215))
		
		
	def displayInventory (self, inventory, mouse, event) :
		"""displays the inventory in a nice fashion"""
		myFont = pygame.font.Font('freesansbold.ttf', 15) # figure out different way
		
		stringHeight = 40
		cashString = "Cash:  $" + str(inventory.getCash())
		cash = myFont.render(cashString, 1, (255,255,255))
		self._display.blit(cash, (10, stringHeight))
		stringHeight += 30
		foodString = "Food:  " + str(inventory.getFood())
		food = myFont.render(foodString, 1, (255,255,255))
		self._display.blit(food, (10, 70))
		stringHeight += 30

		count = 0
		for item in inventory.generateItem() :
			itemTexts = myFont.render(str(item), 1, (255, 255, 255))	
			self._display.blit(itemTexts, (10, stringHeight))								
			stringHeight += 30
			count += 1
			
	def getItemSelection (self, inventory, mouse, event) :
		myFont = pygame.font.Font('freesansbold.ttf', 15)	
		
		stringHeight = 70
		if event.type == MOUSEBOTTONDOWN:
			if self.checkMouse (mouse, 5, 100, stringHeight - 5, \
			stringHeight + 25) :
				pass
					
									
	
#setDisplay = pygame.display.set_mode((400,300))
pygame.display.set_caption('Jungle Jamboree')
imgStart = pygame.image.load('Images/StartScreen.png')
imgJungle = pygame.image.load('Images/HomeScreen.png')
imgStore = pygame.image.load('Images/Shopkeep.png')
imgParty = pygame.image.load('Images/PartyScreen.png')
imgInventory = pygame.image.load('Images/Backpack.png')
imgPerson1 = pygame.image.load('Images/Explorer1.png')
imgPerson2 = pygame.image.load('Images/Person2.png')
imgPerson3 = pygame.image.load('Images/Explorer3.png')
imgPerson4 = pygame.image.load('Images/Person4.png')
imgPerson5 = pygame.image.load('Images/Explorer5.png')
imgx = 0
imgy = 0
imgxP1 = 281
imgyP1 = 400
imgxP2 = 386
imgyP2 = 407
imgxP3 = 200
imgyP3 = 380
imgxP4 = 145
imgyP4 = 400
imgxP5 = 563
imgyP5 = 440


testGame = Game()
start = testGame._myFont1.render("START", 1, (255,255,255))
store = testGame._myFont2.render("STORE", 1, (255,255,255))
forage = testGame._myFont2.render("FORAGE", 1, (255,255,255))
inventory = testGame._myFont2.render("INVENTORY", 1, (255,255,255))
party = testGame._myFont2.render("PARTY", 1, (255,255,255))
day = testGame._myFont3.render("DAY:", 1, (255,255,255))
distance = testGame._myFont3.render("DISTANCE:", 1, (255,255,255))
funds = testGame._myFont3.render("MONEY:", 1, (0,0,0))
leave1 = testGame._myFont3.render("LEAVE", 1, (255,0,0))
leave2 = testGame._myFont3.render("LEAVE", 1, (0,255,255))
testGame.on_loop()

