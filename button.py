class Button():
	def __init__(self, pos, text_input, font, hovering_color, selected_color, deselected_color):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.selected = False
		self.hovering_color, self.selected_color, self.deselected_color = hovering_color, selected_color, deselected_color
		self.color = self.deselected_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.color)
		self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def isClicked(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):		
			return True
		
		return False

	def render(self, position, screen):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			if self.selected == False:
				self.text = self.font.render(self.text_input, True, self.hovering_color)
			else:
				self.text = self.font.render(self.text_input, True, self.selected_color)
		else:
			self.text = self.font.render(self.text_input, True, self.color)
		
		screen.blit(self.text, self.rect)

	def select(self):
		self.selected = True
		self.color = self.selected_color
	
	def deselect(self):
		self.selected = False
		self.color = self.deselected_color