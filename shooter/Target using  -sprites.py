import pygame , sys
from random import randrange

class crosshair(pygame.sprite.Sprite):
	def __init__(self,pic_path):
		super().__init__()

		self.image = pygame.image.load(pic_path)
		self.rect = self.image.get_rect()
		self.shot = pygame.mixer.Sound('shot.wav')
	
	def shoot(self):
		self.shot.play()
		pygame.sprite.spritecollide(crosshair,target_group,True)
	def update(self):
		self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
	def __init__(self, pic_path,pos_x,pos_y):
		super().__init__()

		self.image = pygame.image.load(pic_path)
		self.image= pygame.transform.scale(self.image,(70,70))
		self.rect = self.image.get_rect()
		self.rect.center=[pos_x,pos_y]


#game screens s 
pygame.init()
screen_width =900
screen_height =600
screen=pygame.display.set_mode((screen_width,screen_height))
clock =pygame.time.Clock()
background= pygame.image.load('bg_blue.png')
background=pygame.transform.scale(background,(900,600))
pygame.mouse.set_visible(False)


#crosshair
crosshair=crosshair('cross.png')

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Target

target_group = pygame.sprite.Group()
for  target in range(17):
	new_target=Target('target.png',randrange(0,screen_width),randrange(0,screen_height))
	target_group.add(new_target)
#game loop
while True:
	# evnt 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN :
			crosshair.shoot()

			
	pygame.display.flip()

	screen.blit(background,(0,0))
	target_group.draw(screen)
	crosshair_group.draw(screen)
	crosshair.update()
	clock.tick(60)
	
