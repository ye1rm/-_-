import pygame

def load_and_scale_image(image_path, scale_factor):
    image = pygame.image.load(image_path)
    rect = image.get_rect()
    new_width = int(rect.width * scale_factor)
    new_height = int(rect.height * scale_factor)
    image = pygame.transform.scale(image, (new_width, new_height))
    return image, new_width, new_height
