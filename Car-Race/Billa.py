import pygame,sys

class Car(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		self.original_image = pygame.image.load('images/Audi.png')
		self.image = self.original_image
		self.rect = self.image.get_rect(center=(450,300))
		self.rotation_speed = 1
		self.angle = 0
		self.direction =0
		self.forward = pygame.math.Vector2(0,-1)
		self.accelerator = False
	def rotation(self):
		if self.direction == 1:
			self.angle -= self.rotation_speed 
			self.forward.rotate_ip(self.rotation_speed)


		if self.direction == -1:
			self.angle += self.rotation_speed 
			self.forward.rotate_ip(-self.rotation_speed)
		
		self.image = pygame.transform.rotozoom(self.original_image,self.angle+1,0.25)
		self.rect  = self.image.get_rect(center = self.rect.center)
	

	def speed(self):
		if self.accelerator:
			self.rect.center += self.forward * 5



	def update(self):
		self.rotation()
		self.speed()



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900,600))
bg = pygame.image.load('images/Track.png')
bg =pygame.transform.scale(bg,(900,600))


car = pygame.sprite.GroupSingle(Car())


#game loop
while True:
	# evnt 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT: car.sprite.direction +=1
			if event.key == pygame.K_LEFT:  car.sprite.direction -=1
			if event.key == pygame.K_SPACE: car.sprite.accelerator = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT: car.sprite.direction -=1
			if event.key == pygame.K_LEFT: car.sprite.direction +=1
			if event.key == pygame.K_SPACE: car.sprite.accelerator = False

	screen.blit(bg,(0,0))
	car.draw(screen)
	car.update()
	pygame.display.update()
	clock.tick(60)