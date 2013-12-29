#!/usr/bin/python
from time import sleep
from Parameters import Parameter

class Menu:

	# Define input buttons
	BUTTON_UP 		= 10
	BUTTON_DOWN		= 22
	BUTTON_LEFT 	= 9
	BUTTON_RIGHT	= 27
	BUTTON_SELECT	= 4
	BUTTON_BACK 	= 17
	BUTTONS			= [BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SELECT, BUTTON_BACK]

	# Define Output
	LED				= 11

	# Control screen position
	SCREEN_POS		= -1
	LAST_POS		= SCREEN_POS

	# Cursor position
	CURSOR_POS		= 1
	LAST_C_POS 		= CURSOR_POS

	# Flag to determine if configuring or not
	CONFIG 			= False

	# Initializer
	def __init__(self, LCD = None, GPIO = None, Parameter = None):
		if not LCD:
			from Adafruit_CharLCD import Adafruit_CharLCD as LCD
		if not GPIO:
			import RPi.GPIO as GPIO
		if not Parameter:
			self.PARAMETERS = Parameter()
		else:
			self.PARAMETERS = Parameter
		
		# Set the instance variables for controlling GPIO and LCD
		self.GPIO = GPIO
		self.lcd = LCD(7,8,[25, 24, 23,18])

		self.lcd.begin(16,2)

		self.GPIO.setmode(self.GPIO.BCM)
		self.GPIO.setup(self.BUTTON_UP, 	self.GPIO.IN)
		self.GPIO.setup(self.BUTTON_DOWN, 	self.GPIO.IN)
		self.GPIO.setup(self.BUTTON_LEFT, 	self.GPIO.IN)
		self.GPIO.setup(self.BUTTON_RIGHT, 	self.GPIO.IN)
		self.GPIO.setup(self.BUTTON_SELECT, self.GPIO.IN)
		self.GPIO.setup(self.BUTTON_BACK, 	self.GPIO.IN)
		self.GPIO.setup(self.LED, 			self.GPIO.OUT)
		
	def clear(self):
		self.lcd.clear()

	def message(self, text):
		self.lcd.message(text)

	def send_screen(self, text):
		self.clear()
		self.message(text)

	def get_input(self):
		screen = self.SCREEN_POS
		cursor = self.CURSOR_POS
		if not self.GPIO.input(self.BUTTON_UP):
			self.send_screen('UP!')
		elif not self.GPIO.input(self.BUTTON_DOWN):
			self.send_screen('DOWN!')
		elif not self.GPIO.input(self.BUTTON_LEFT):
			if self.CONFIG:
				self.LAST_C_POS = cursor
				if screen == 4:
					self.CURSOR_POS = (cursor - 1) if self.CURSOR_POS>0 else 8
					# self.lcd.setCursor(self.CURSOR_POS, 1)
					print 'Moved cursor at pos => {}'.format(self.CURSOR_POS)
				else:
					self.CURSOR_POS = (cursor - 3) if self.CURSOR_POS> 1 else 7
					# self.lcd.setCursor(self.CURSOR_POS, 1)
					print 'Moved cursor at pos => {}'.format(self.CURSOR_POS)
			else:
				self.LAST_POS = self.SCREEN_POS
				self.SCREEN_POS = (screen - 1) if self.SCREEN_POS>=0 else 4
		elif not self.GPIO.input(self.BUTTON_RIGHT):
			if self.CONFIG:
				self.LAST_C_POS = cursor
				if screen == 4:
					self.CURSOR_POS = (cursor + 1) if self.CURSOR_POS<8 else 0
					# self.lcd.setCursor(self.CURSOR_POS, 1)
					print 'Moved cursor at pos => {}'.format(self.CURSOR_POS)
				else:
					self.CURSOR_POS = (cursor + 3) if self.CURSOR_POS<7 else 1
					# self.lcd.setCursor(self.CURSOR_POS, 1)
					print 'Moved cursor at pos => {}'.format(self.CURSOR_POS)
			else:
				self.LAST_POS = self.SCREEN_POS
				self.SCREEN_POS = (screen + 1) if self.SCREEN_POS<5 else 0
		elif not self.GPIO.input(self.BUTTON_SELECT):
			if not self.CONFIG:
				self.CONFIG = True
				self.lcd.cursor()
				if screen == 4:
					self.CURSOR_POS = 0
					self.lcd.setCursor(self.CURSOR_POS, 1)
				else:
					self.lcd.setCursor(self.CURSOR_POS, 1)
		elif not self.GPIO.input(self.BUTTON_BACK):
			if self.CONFIG:
				self.CONFIG = False
				self.lcd.noCursor()
				self.CURSOR_POS = 1

	def update_screen(self):
		screen = self.SCREEN_POS
		last = self.LAST_POS
		cursor = self.CURSOR_POS
		last_c = self.LAST_C_POS
		p = self.PARAMETERS
		if last != screen or last_c != cursor:
			if screen == 0:
				self.send_screen("Delay\n")
				self.message('{0:02d}:{0:02d}:{0:02d}'.format(p.DELAY_H, p.DELAY_M, p.DELAY_S))
			elif screen == 1:
				self.send_screen("Longevity\n")
				self.message('{0:02d}:{0:02d}:{0:02d}'.format(p.LONG_H, p.LONG_M, p.LONG_S))
			elif screen == 2:
				self.send_screen("Interval\n")
				self.message('{0:02d}:{0:02d}:{0:02d}'.format(p.INTER_H, p.INTER_M, p.INTER_S))
			elif screen == 3:
				self.send_screen("Length\n")
				self.message('{0:02d}:{0:02d}:{0:02d}'.format(p.LENG_H, p.LENG_M, p.LENG_S))
			elif screen == 4:
				self.send_screen("Shots to take\n")
				self.message('{0:09,d}'.format(p.N))
			self.lcd.setCursor(cursor, 1)
		self.LAST_POS = screen
		self.LAST_C_POS = cursor


	def destroy(self):
		print 'Bye'
		self.send_screen("Bye")
		self.GPIO.cleanup()

if __name__ == '__main__':
	parameters = Parameter()
	menu = Menu(Parameter = parameters)
	menu.SCREEN_POS = 0
	try:
		while True:
			menu.get_input()
			menu.update_screen()
			# print 'Screen {} @ Cursor {}'.format(menu.SCREEN_POS, menu.CURSOR_POS)
			sleep(0.1)
	except KeyboardInterrupt:
		menu.destroy()
		sleep(1.0/2)