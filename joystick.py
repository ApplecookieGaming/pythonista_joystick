# Joel Paul
# Wednesday 30th November 2016

from scene import *

''' CONSTANTS '''
# Area where the joystick can spawn, the larger the number, the smaller the area
JOYSTICK_AREA = 2
# How far the knob can move away from its origin
KNOB_RESTRICTION = 11
''' --------- '''

class Joystick (Scene):
	def setup(self):
		# The joystick isn't being used, so we tell the program to return a false boolean
		self.using_joystick = False
		
		''' Create the joystick base and knob '''
		self.joystickbase = SpriteNode(color="#FFFFFF", alpha=0.2, size=(self.size.h/4, self.size.h/4))
		self.joystickknob = SpriteNode(color="#FFFFFF", alpha=0.2, size=(self.size.h/16, self.size.h/16))
		''' --------------------------------- '''
	
	def update(self):
		# If the joystick isn't being used, remove it
		if self.using_joystick == False:
			self.remove_joystick()
		
	def remove_joystick(self):
		self.joystickbase.remove_from_parent()
		self.joystickknob.remove_from_parent()
	
	def touch_began(self, touch):
		x, y = touch.location
		
		""" Add joytick """
		# Check if the user is touching within the bottom-left quadrant..
		if x < self.size.w/JOYSTICK_AREA and y < self.size.h/JOYSTICK_AREA:
			# Create a new variable to use the quadrant value
			self.x, self.y = x, y
			''' Create the joystick at the new position '''
			self.joystickbase.position = (self.x, self.y)
			self.add_child(self.joystickbase)
			self.joystickknob.position = (self.x, self.y)
			self.add_child(self.joystickknob)
			''' --------------------------------------- '''
			# Tell the program the joystick is being used
			self.using_joystick = True
		""" ----------- """
	
	def touch_moved(self, touch):
		x, y = touch.location
		
		""" Move joystick knob """
		# If the touched location is inside the bottom-left quadrant...
		if x < self.size.w/JOYSTICK_AREA and y < self.size.h/JOYSTICK_AREA:
			x_moved, y_moved = x, y # Only allows certain coordinates to pass
			
			''' if the touch has moved past the right side joystick base limit... '''
			if x_moved > self.x + self.size.h/KNOB_RESTRICTION:
				# Set the knob's x-coordinate to the right side joystick base limit
				knob_x = self.x + self.size.h/KNOB_RESTRICTION
				''' else if the touch has moved past the left side joystick base limit... '''
			elif x_moved < self.x - self.size.h/KNOB_RESTRICTION:
				# Set the knob's x-coordinate to the left side joystick base limit
				knob_x = self.x - self.size.h/KNOB_RESTRICTION
				''' else keep it where it is (which is inside the horizontal joystick base limits) '''
			else:
				knob_x = x_moved
			
			''' if the touch has moved past the top joystick base limit... '''				
			if y_moved > self.y + self.size.h/KNOB_RESTRICTION:
				# Set the knob's y-coordinate to the top joystick base limit
				knob_y = self.y + self.size.h/KNOB_RESTRICTION
				''' if the touch has moved past the bottom joystick base limit... '''
			elif y_moved < self.y - self.size.h/KNOB_RESTRICTION:
				# Set the knob's y-coordinate to the bottom joystick base limit
				knob_y = self.y - self.size.h/KNOB_RESTRICTION
				''' else keep it where it is (which is inside the vertical joystick base limits) '''
			else:
				knob_y = y_moved
			
			# Set the joystick position to the previous calculations	
			self.joystickknob.position = (knob_x, knob_y)
		""" ------------------- """
				
	def touch_ended(self, touch):
		x, y = touch.location
		
		# If the player stops touching inside quadrant, tell the program the joystick isn't being used
		# Used to later remove the joystick in 'remove_joystick(self)''
		if x < self.size.w/JOYSTICK_AREA and y < self.size.h/JOYSTICK_AREA:
			self.using_joystick = False

if __name__ == '__main__':
	run(Joystick(), show_fps=True, orientation=LANDSCAPE)
