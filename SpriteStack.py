import pygame
import sys
import os

# dimensions and setup:
SLICE_DISTANCE = 5
SLICE_DIMENSION = 80
SLICE_DIRECTORY = "Graphics"
SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
ANGLE = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# import slice images:
sliced_images = []
for image in os.listdir(SLICE_DIRECTORY):
    img = pygame.image.load(SLICE_DIRECTORY + "/" + image).convert()
    img.set_colorkey((0,0,0))
    img = pygame.transform.scale(img, (SLICE_DIMENSION, SLICE_DIMENSION))
    sliced_images.insert(0, img)


# center the stack on the screen
stack_center_x = round(SCREEN_WIDTH/2)
stack_center_y = round(SCREEN_HEIGHT/2) + round(((len(sliced_images) - 1) * SLICE_DISTANCE) / 2)


while True:
    # pygame close event:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # increase the angle to rotate the box:
    ANGLE += 1

    # clear the screen:
    screen.fill("aqua")

    # display the slices one by one, increasing the y offset (with 'i * SLICE_DISTANCE'):
    for i, slice in enumerate(sliced_images):
        rotated_slice = pygame.transform.rotate(slice, ANGLE)
        rotation_offset_x = int(rotated_slice.get_width()/2)
        rotation_offset_y = int(rotated_slice.get_height()/2)
        screen.blit(rotated_slice, (stack_center_x - rotation_offset_x, stack_center_y - i * SLICE_DISTANCE - rotation_offset_y))

    # update the screen:
    pygame.display.flip()

    # set steady frame rate of 60:
    pygame.time.Clock().tick(60)