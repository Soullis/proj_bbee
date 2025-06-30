import pygame as pg
import drone


mA = drone.Motor()
mB = drone.Motor()
mC = drone.Motor()
mD = drone.Motor()
d = drone.Drone(mA, mB, mC, mD)

# Initialize Pygame
pg.init()

class DronePlayer(pg.sprite.Sprite):
    def __init__(self, image_path, pos_x, pos_y):
        super().__init__()
        self.orig_imag = pg.image.load(image_path).convert_alpha()
        self.image = self.orig_imag.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def rotate(self):
        """Rotates the sprite's image and updates its rect to maintain center."""
        # Rotate the original image to avoid quality loss
        self.image = pg.transform.rotate(self.orig_imag, d.rot)
        # Get the new rect and preserve the old center
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)

    def update(self, keys):
        if keys[pg.K_UP]:
            d.throttle()
        if keys[pg.K_DOWN]:
            d.throttle(-1)
        if keys[pg.K_LEFT]:
            d.yaw(-1)
            self.rotate()
        if keys[pg.K_RIGHT]:
            d.yaw()
            self.rotate()
        if keys[pg.K_w]:
            d.pitch(-1)
            self.rect.y = d.pos[2]
        if keys[pg.K_s]:
            d.pitch()
            self.rect.y = d.pos[2]
        if keys[pg.K_a]:
            d.roll(-1)
            self.rect.x = d.pos[0]
        if keys[pg.K_d]:
            d.roll()
            self.rect.x = d.pos[0]
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        
        d.print_mob()
        
        

# Set up the game window

screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Drone Simulation")
font = pg.font.Font(None, 36)

drone = DronePlayer('drone.png', d.pos[0], d.pos[2])

all_sprites = pg.sprite.Group()
all_sprites.add(drone)

# Game loop
running = True
clock = pg.time.Clock()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    key_pressed = pg.key.get_pressed()
    all_sprites.update(key_pressed)
    
    screen.fill((135, 206, 235))
    all_sprites.draw(screen)

    pos_text = f"FL: {d.mFL.t:.2f} FR: {d.mFR.t:.2f} BL: {d.mBL.t:.2f} BR: {d.mBR.t:.2f} Lidar {d.pos[1]:.2f} R {d.rot:.2f}"
    text_surface = font.render(pos_text, True, (0, 0, 0)) 
    screen.blit(text_surface, (10, 10))

    pg.display.flip()
    clock.tick(60)

# Quit Pygame
pg.quit()