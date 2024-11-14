import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512)) #width,height if 640,512 are the pixels respectively, each cell of the grid is 32 pixels wide and 32 pixels high
        clock = pygame.time.Clock()
        #Mole's position initializes at (0,0)
        mole_x=0 #i use this variables because while the game is running the position of the mole will be being updated everytime i click the screen
        mole_y=0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                     x, y = event.pos
                     row = y // 32
                     col = x // 32
                     #print(row,col) #Position of every click
                     if col == (mole_x//32) and row == (mole_y//32): #if the position of the clicks match the position of the mole then it generates a random location updating the previous one
                        mole_x=random.randrange(0,640,32) #random position generated from 0 to the width of the screen but since every square is 32x32 we need to add a step of 32
                        mole_y=random.randrange(0,512,32) #random position generated from 0 to the height of the screen but since every square is 32x32 we need to add a step of 32

            screen.fill((255,102,255)) #color of the grid in RGB color code
            #pygame.display.flip()
            clock.tick(60)
            for i in range(1, 16): #rows of 512 pixels (each cell is 32pixelsX32pixels)
                pygame.draw.line(
                    screen,                 #starts at 0, each horinzontal line changes by 32, ends at pos=640 ( the width of the screen)
                    color="Black",start_pos=(0, i * 32),end_pos=(640, i * 32))

            for j in range(1, 20): #columns of 640 pixels (each cell is 32pixelsX32pixels)
             pygame.draw.line(
                      screen,                 # the x coordinate increases with each iteration to create vertical lines. every line ends at the bottom of the screen (512 pixels hhigh)
                     color="black",start_pos=(j * 32, 0),end_pos=(j * 32, 512))
            screen.blit(mole_image,( mole_x, mole_y))
            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
