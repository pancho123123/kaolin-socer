import pygame, random
from random import randint

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)
BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Earth Spirith")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BROWN, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/earth_spirit.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.hp = 100


class Player1(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 500
		self.rect.y = 133
		
	def update(self):
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -3
		if keystate[pygame.K_d]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -3
		if keystate[pygame.K_s]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

class Player2(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 900
		self.rect.y = 133
				
	def update(self):
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -3
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -3
		if keystate[pygame.K_DOWN]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

class Stamp1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/blue.png").convert(),(65,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 500
		self.rect.y =  133

	def update(self):
		if player1.hp == 0:
			self.kill()

class Stamp2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/purple.png").convert(),(65,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 900
		self.rect.y =  133

	def update(self):
		if player2.hp == 0:
			self.kill()

class Stone(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = stone_images[0]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 750
		self.rect.centery = 266
		self.speedx = 0
		self.speedy = 0

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.speedx > 0:
			self.speedx -= 0.09
		if self.speedx < 0:
			self.speedx += 0.09
		if self.speedy > 0:
			self.speedy -= 0.09
		if self.speedy < 0:
			self.speedy += 0.09

		if self.rect.right > WIDTH + 50:
			self.speedx -= 8
		if self.rect.left < 250:
			self.speedx += 8
		if self.rect.y < 30:
			self.speedy += 8
		if self.rect.y > 500:
			self.speedy -= 8

class Borde1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/borde.png").convert(),(1000,1))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 290
		self.rect.y = 80

class Borde2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/borde.png").convert(),(1000,1))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 290
		self.rect.y = 550

class Borde3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/borde.png").convert(),(1,800))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 0

class Borde4(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/borde.png").convert(),(1,800))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH
		self.rect.y = 0

def show_go_screen():
	
	screen.fill(BLACK)
	draw_text1(screen, "Kaolin Socer", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Hit the stone", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

stone_images = []
stone_list = ["img/stone.png"]
for img in stone_list:
	stone_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(50,65)))

def show_game_over_screenp1():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 1 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp2():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 2 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

background = pygame.transform.scale(pygame.image.load("img/5.png").convert(), (1300,700))

game_over1 = False
game_over2 = False
running = True
start = True
while running:
	if game_over1:

		show_game_over_screenp1()
		borde1 = Borde1()
		borde2 = Borde2()
		borde3 = Borde3()
		borde4 = Borde4()
		
		screen.blit(background,(0,0))
		game_over1 = False
		
		all_sprites = pygame.sprite.Group()
		all_sprites.add(borde1, borde2, borde3, borde4)
		stone_list = pygame.sprite.Group()
		stamp1 = Stamp1()
		stamp2 = Stamp2()
		all_sprites.add(stamp1, stamp2)
		player1 = Player1()
		player2 = Player2()
		all_sprites.add(player1, player2)
		stone = Stone()
		all_sprites.add(stone)
		stone_list.add(stone)
		start_time = pygame.time.get_ticks()

	if game_over2:

		show_game_over_screenp2()
		borde1 = Borde1()
		borde2 = Borde2()
		borde3 = Borde3()
		borde4 = Borde4()
		
		screen.blit(background,(0,0))
		game_over2 = False
		all_sprites = pygame.sprite.Group()
		all_sprites.add(borde1, borde2, borde3, borde4)
		stone_list = pygame.sprite.Group()
		stamp1 = Stamp1()
		stamp2 = Stamp2()
		all_sprites.add(stamp1, stamp2)
		player1 = Player1()
		player2 = Player2()
		all_sprites.add(player1, player2)
		stone = Stone()
		all_sprites.add(stone)
		stone_list.add(stone)
		start_time = pygame.time.get_ticks()

	if start:
		show_go_screen()
		
		start = False
		borde1 = Borde1()
		borde2 = Borde2()
		borde3 = Borde3()
		borde4 = Borde4()
		
		screen.blit(background,(0,0))
		all_sprites = pygame.sprite.Group()
		all_sprites.add(borde1, borde2, borde3, borde4)
		stone_list = pygame.sprite.Group()
		stamp1 = Stamp1()
		stamp2 = Stamp2()
		all_sprites.add(stamp1, stamp2)
		player1 = Player1()
		player2 = Player2()
		all_sprites.add(player1, player2)
		stone = Stone()
		all_sprites.add(stone)
		stone_list.add(stone)
		start_time = pygame.time.get_ticks()
		
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

	now = (pygame.time.get_ticks() - start_time)//1000
	
	if player1.hp <= 0:
		game_over2 = True
	if player2.hp <= 0:
		game_over1 = True
	
	all_sprites.update()
	
	# Checar colisiones - sello - stone
	hits = pygame.sprite.spritecollide(stamp1, stone_list, False)
	for hit in hits:
		
		if player1.hp > 0:
			player1.hp -= 0.8
			
	# Checar colisiones - sello - stone
	hits = pygame.sprite.spritecollide(stamp2, stone_list, False)
	for hit in hits:
		
		if player2.hp > 0:
			player2.hp -= 0.8
			
	# Checar colisiones - player1 - stone
	hits = pygame.sprite.spritecollide(player1, stone_list, False)
	for hit in hits:
		
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a] and keystate[pygame.K_e]:
			stone.speedx = -10
		if keystate[pygame.K_d] and keystate[pygame.K_e]:
			stone.speedx = 10
		
		if keystate[pygame.K_w] and keystate[pygame.K_e]:
			stone.speedy = -10
		if keystate[pygame.K_s] and keystate[pygame.K_e]:
			stone.speedy = 10
		
	# Checar colisiones - player2 - stone
	hits = pygame.sprite.spritecollide(player2, stone_list, False)
	for hit in hits:
		
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT] and keystate[pygame.K_p]:
			stone.speedx = -10
		if keystate[pygame.K_RIGHT] and keystate[pygame.K_p]:
			stone.speedx = 10
		
		if keystate[pygame.K_UP] and keystate[pygame.K_p]:
			stone.speedy = -10
		if keystate[pygame.K_DOWN] and keystate[pygame.K_p]:
			stone.speedy = 10
		
	# Checar colisiones - borde1 - stone
	hits = pygame.sprite.spritecollide(borde1, stone_list, False)
	for hit in hits:
		if stone.speedy < 0:
			stone.rect.top = borde1.rect.bottom
			stone.speedy = -stone.speedy
		
	# Checar colisiones - borde2 - stone
	hits = pygame.sprite.spritecollide(borde2, stone_list, False)
	for hit in hits:
		if stone.speedy > 0:
			stone.rect.bottom = borde2.rect.top
			stone.speedy = -stone.speedy
		
	# Checar colisiones - borde3 - stone
	hits = pygame.sprite.spritecollide(borde3, stone_list, False)
	for hit in hits:
		if stone.speedx < 0:
			stone.rect.left = borde3.rect.right
			stone.speedx = -stone.speedx

	# Checar colisiones - borde4 - stone
	hits = pygame.sprite.spritecollide(borde4, stone_list, False)
	for hit in hits:
		if stone.speedx > 0:
			stone.rect.right = borde4.rect.left
			stone.speedx = -stone.speedx
		
	screen.blit(background, [0, 0])

	all_sprites.draw(screen)
	
	# Escudo.
	draw_text1(screen, "P1", 20, 310, 6)
	draw_text1(screen, "P2", 20, 800, 6)
	
	draw_hp_bar(screen, 320, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 370, 6)
	if player1.hp > 0:
		draw_hp_bar(screen, player1.rect.x, player1.rect.y - 10, player1.hp)

	draw_hp_bar(screen, 815, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 870, 6)
	if player2.hp > 0:
		draw_hp_bar(screen, player2.rect.x, player2.rect.y - 10, player2.hp)

	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)
		
	pygame.display.flip()
pygame.quit()