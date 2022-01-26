import pygame
from support import import_folder, join


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.animation_state = "idle"
        self.image = self.animations[self.animation_state][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        self.grounded = False
        self.facing_right = True

    def import_character_assets(self):
        character_path = join("graphics", "character")
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            full_path = join(character_path, animation)
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        if self.direction.y > 2:
            self.animation_state = "fall"
        if self.direction.y == 0:
            self.animation_state = "idle"
            if self.direction.x != 0:
                self.animation_state = "run"
        if self.direction.y < 0:
            self.animation_state = "jump"
        animation = self.animations[self.animation_state]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        # could be problematic down the line but its good for now i guess
        if not self.facing_right:
            image = pygame.transform.flip(image, True, False)
        self.image = image

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # changed to have more support for wasd controls
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            if self.grounded:
                self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.animate()
