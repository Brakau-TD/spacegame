import pygame

pygame.init()


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 25)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


def main():
    # Set the width and height of the screen (width, height), and name the window.
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Joystick example")

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Get ready to print.
    text_print = TextPrint()

    # This dict can be left as-is, since pygame will generate a
    # pygame.JOYDEVICEADDED event for every joystick connected
    # at the start of the program.
    joysticks = {}
    pos = [50,100]
    image = pygame.image.load("roboter.png")
    roboter = image.get_rect()
    joystick = pygame.joystick.Joystick(0)
    done = False
    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                print(f"pressed {joystick.}")
            

                
            if joystick.get_button(0): #A
                print(0)
            if joystick.get_button(1): #B
                print(1)
            if joystick.get_button(2): #X
                print(2)
            if joystick.get_button(3): #Y
                print(3)





        # Drawing step
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill((255, 255, 255))
        text_print.reset()


        # Movement of player
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
            pos[0]+=axis*5 if i == 0 else 0
            pos[1]+=axis*5 if i ==1 else 0

        buttons = joystick.get_numbuttons()


        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        hat = joystick.get_hat(0)
        match (hat):
            case (1,0):
                print(1,0) # special 1
            case (0,1):
                print(0,1) # special 2
            case (-1,0):
                print(-1,0) # special 3
            case (0,-1):
                print(0,-1) # special 4
        

        screen.blit(image,pos)
        

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 30 frames per second.
        clock.tick(30)


if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()