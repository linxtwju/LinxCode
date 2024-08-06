import pygame
import random
 
# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
pygame.font.init()
 
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


 
# SHAPE FORMATS
 
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
      
      ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
 
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape
#(red,green, blue); 255 is the highest, see rgb
#black - (0,0,0)
#white - (255, 255, 255)
#green - (0, 255, 0)

 
class Piece(object):
    def __init__ (self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0
 
def create_grid(locked_positions={}): #dict is going to be like {(1,1):(255,0,0), position: color (later we fill it)}
    grid = [[(0, 0, 0) for j_columns_x in range (10)] for i_rows_y in range (20)] #This is the grid, 2 dimensional list
    
    for i in range (len(grid)): #rows
        for j in range (len(grid[i])): #columns
            if (j, i) in locked_positions:
                c = locked_positions[(j,i)] #c is going to be a color, because we are taking it of the dictionary(locked_positions)
                grid[i][j] = c #we are assigning the color to the position of the grid
    return grid

 
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len (shape.shape)] #contains the strings with the "picture" of the shape of the piece
    
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0": 
                positions.append((shape.x + j, shape.y + i))
    
    for i, pos in enumerate(positions): 
        positions[i] = (pos[0]-2, pos[1]-4)
    
    return positions
 
def valid_space(shape, grid):
    accepted_pos = [[(j,i) for j in range (10) if grid[i][j]== (0,0,0)] for i in range(20)]     #accepted positions are empty
    accepted_pos = [j for sub in accepted_pos for j in sub]             #[(),()] 1-n list                          #[[(0,1)],[(2,3)]] -> [(0,1), (2,3)]
    
    formatted = convert_shape_format(shape)         #[(),()]   positions of 0 in the shapes
    
    for pos in formatted:                   #iterating the positions of 0
        if pos not in accepted_pos:         #checking if the positions of 0 are in accepted positions
            if pos[1] > -1:                 #we substrated - 4 before to this position, if its greater than -1 is not valid
                return False                   #this is checking if the position is inside the grid 
    return True
 
def check_lost(positions):  #this functions checks if the pieces are above the screen
    for pos in positions: 
        x, y = pos 
        if y < 1: #if pos y is lower than 1 it means that the piece has arrived to the top 
            return True 
    return False 
 
def get_shape():
    return Piece(5, 0, random.choice(shapes)) #chosing random shape of the list shapes 
    #(x, y)values x is the middle of the screen (then 5) and y is the beginning
 
 
def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render (text, 1, color)   
    
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + play_height/2 - label.get_height()/2))
    
def draw_grid(surface, grid): #draw the lines of the grid
    sx = top_left_x
    sy = top_left_y
    
    for i in range (len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*block_size),(sx+play_width, sy+ i*block_size))#grey( color code stadard) , then the positions
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128,128,128), (sx+ j*block_size, sy),(sx+ j*block_size, sy+ play_height))
   
    
    
    
def clear_rows(grid, locked):
    #check if the locked position on the grid are not black in the entire x axis
    inc = 0 
    ind = 0
    for i in range (len(grid)-1, -1, -1): 
        row = grid[i]
        if (0,0,0) not in row: 
            inc += 1
            index_of_row_cleared = i 
            for j in range (len(row)): 
                try: 
                    del locked [(j,i)]
                except: 
                    continue
    
    if inc > 0: 
        for key in sorted(list(locked), key = lambda x : x[1])[::-1]: #x[1] is the y value, the locked list is going to be sorted by the y values
            x, y = key                                                           #the for loop is going to increment -1 (from bottom to top)
            if y < index_of_row_cleared: 
                newKey = (x, y + inc) #here is increasing the y position
                locked[newKey] = locked.pop(key) #here is taking the color of the position that is removing, and assigning to the new position (1 minus) 
    return inc
    
def draw_next_shape(shape, surface):
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", 1, (255,255,255))
    
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100
    
    format = shape.shape[shape.rotation % len(shape.shape)]
    
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row): 
            if column == "0": 
                pygame.draw.rect (surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)
    
    
    
    surface.blit (label, (sx - 10 ,sy - block_size * 2 ))
    
    
 
 
def draw_window(surface, grid, score = 0): #this function draws the play area
    surface.fill((0,0,0)) #black
    
    pygame.font.init() #setting up font and getting ready to draw to the screen
    font = pygame.font.SysFont("comicsans", 60) #creating a font, you can check other fonts on pygame website 
    label = font.render ("Tetris", 1, (255,255,255)) #(text, antialiasing (set it 1), color (in this case is white))
    #label2 = font.render ("Tetris 2.0", 1, (255,255,255))
    
    surface.blit (label, (top_left_x + play_width/2 - (label.get_width()/2),30)) #this serves to show the label in the screen, (label, position)
    #surface.blit (label2, (top_left_x + play_width/2 - (label2.get_width()/2),0))
    
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Score: " + str(score), 1, (255,255,255))
    
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100
    
    surface.blit(label, (sx + 10 , sy + block_size * 4))
    
    
    for i in range (len(grid)): 
        for j in range (len(grid[i])): 
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)#draws the rectangles of the grid (surface, COLOR, rect(posx, posy, width(x), height(y)), border size = 0 ) //// the lines are drawn in draw_grid
    pygame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4) #the red rectangle of the play area
    #draw main rectangle(surface, COLOR, (rectangle measure), border size = 4  )
    draw_grid(surface, grid)
    

 
def main(win):
    locked_positions = {} #same dict of the blank one set in create_grid
    grid = create_grid(locked_positions) 
    
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27 #time that takes the pieces to fall
    level_time = 0
    score = 0

    
    while run: 
        grid = create_grid(locked_positions) #every time that we move, has a chance to adding something to locked positions
        fall_time += clock.get_rawtime() #get_rawtime takes the amount of time since the clock.tick
        level_time += clock.get_rawtime()
        clock.tick()                        #these two lines serve to run at the exact same speed on everyone's computer
        
        if level_time/ 1000 > 5 : 
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005
        
        
        if fall_time / 1000 > fall_speed: #if the miliseconds of the fall_time become greater than fall_speed 
            fall_time = 0                   # the fall_time becomes 0
            current_piece.y += 1            # the piece is going to fall 1 
            if not (valid_space(current_piece, grid)) and current_piece.y > 0: #checking if the piece can be in a valid_space and is not in the top
                current_piece.y -= 1 #this cancells the previous moving if the space is invelid  
                change_piece = True     #then new piece
                
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if you close the window
                run = False 
                pygame.display.quit()
                
            if event.type == pygame.KEYDOWN: #if you press a key
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1 #this moves the block left 
                     # TO SOLVE 
                    if not (valid_space(current_piece, grid)):
                        current_piece.x += 1
                
                if event.key == pygame.K_RIGHT:
                    
                    current_piece.x += 1 #this moves the block right
                                        # IF THE MOVE IS > THAN THE PLAY AREA IT CAN'T GO 
                    if not (valid_space(current_piece, grid)):
                        current_piece.x -= 1
                
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1 #to move downwards
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1
                    
                
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1 #rotates the shape
                    if not (valid_space(current_piece, grid)):
                        current_piece.rotation -= 1
        
        shape_pos = convert_shape_format(current_piece) #check all the positions of 0's
        
        for i in range(len(shape_pos)): # for each set of positions of the current piece (ex:0,1,2,3)    
            x,y = shape_pos [i]         #assign them to the variables x and y
            if y > -1:                  # if y is valid, greater than -1 (not above the screen)
                grid[y][x] = current_piece.color #here is assigning the color of the piece to the grid
        
        if change_piece:                                            #{(1,2):(255,0,0)}
            for pos in shape_pos:                                   #for each set of positions of the current piece ex: (1,2), (2,3)
                p = (pos[0], pos[1])                                #assign to p a tuple with this position
                locked_positions[p] = current_piece.color           #and then the dict of locked position, assign the value of the position to the color of the piece
            current_piece = next_piece                              #once we have the positions of the piece assigned to a color and locked, we change to new piece
            next_piece = get_shape() #maybe this is not necessary because we have at the beginning of the function all the variables
            change_piece = False                            #once we have changed the piece, change_piece becomes false 
            score += clear_rows(grid, locked_positions)  * 10                                                                                                    
        
        
        draw_window(win, grid, score)
        draw_next_shape(next_piece, win)
        pygame.display.update()    #to show the changes made (pygame.draw. ...)
     
        
        if check_lost(locked_positions): #this checks if we lose 
            draw_text_middle(win, "You lost!", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False   
    
 
def main_menu(win):  #*
    run = True
    while run: 
        win.fill((0,0,0))
        draw_text_middle(win, "Press Any Key To Play", 30, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
            if event.type == pygame.KEYDOWN: 
                main (win)
        
    pygame.display.quit()

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")
main_menu(win)  # start game

