import pygame
import random
import math
pygame.init() #initialize pygame

class DrawInformation:
    #define colors
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    # GREY = 128, 128, 128
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    BACKGROUND_COLOR = WHITE
    SIDE_PADDING =100
    TOP_PADDING = 150

    GRADIENTS = [
        (128,128,128),
        (160,160,160),
        (192,192,192),
    ]
    FONT = pygame.font.SysFont("Verdana",20)
    LARGE_FONT = pygame.font.SysFont(" Verdana", 30)

    def __init__(self, height,width, dataList):
        self.height = height
        self.width = width

        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithm Vizualization")
        self.set_list(dataList)

    def set_list(self, dataList):
        self.dataList = dataList
        self.minimum = min(dataList)
        self.maximum = max(dataList)

        self.block_width = round((self.width - self.SIDE_PADDING) / len(dataList))
        self.block_height = math.floor((self.height - self.TOP_PADDING) / (self.maximum - self.minimum))
        self.start_x = self.SIDE_PADDING // 2


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    
    title = draw_info.LARGE_FONT.render(f"{algo_name} - { 'In Ascending Order' if ascending  else 'Decsending Order'}", 1, draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 , 5))
    controls = draw_info.FONT.render(" R Reset | A Sort Ascending | D sort descending  SPACE to sort", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 , 35))
    sorting = draw_info.FONT.render("I insertion sort | B bubble sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2 , 65))
    drawingList(draw_info)
    pygame.display.update()

def drawingList(draw_info, colorPositions={}, clear_background=False):
    dataList = draw_info.dataList

    if clear_background:
        clear_rect = (draw_info.SIDE_PADDING // 2, draw_info.TOP_PADDING,
            draw_info.width - draw_info.SIDE_PADDING , 
            draw_info.height - draw_info.TOP_PADDING
        )
        pygame.draw.rect(draw_info.window,draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(dataList):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.minimum) * draw_info.block_height
        color = draw_info.GRADIENTS[1 % 3]
        if i in colorPositions:
            color = colorPositions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_background:
        pygame.display.update()

        

#generate the starting list
def generate_starting_list(values,min_value, max_value):
    dataList = []

    for _ in range(values):
        value = random.randint(min_value, max_value)
        dataList.append(value)
    print(dataList)
    return dataList

def bubble_sort(draw_info, ascending=True):
    #implementation of thr bubble sort
    myList = draw_info.dataList

    for number in range(len(myList)):
        for k in range(0, len(myList) - number -1):
            if (myList[k] > myList[k + 1] and ascending) or myList[k] < myList[k + 1] and not ascending:
                temp_number = myList[k]
                myList[k] = myList[k + 1]
                myList[k + 1] = temp_number
                drawingList(draw_info, {k : draw_info.GREEN, k+1 : draw_info.RED}, True)
            yield True
    print(myList)
    return myList




#the pygame event loop
def main():
    run = True
    clock = pygame.time.Clock()

    values = 100
    min_value = 20
    max_value = 500
    my_list = generate_starting_list(values,min_value, max_value)
    displayInfo = DrawInformation(800, 1200,my_list)
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None
    while run:
        clock.tick(120)#change the clock to move faster
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopAsyncIteration:
                sorting = False
        else:
            draw(displayInfo,sorting_algorithm_name, ascending)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                #The R key to reset the list
                myList = generate_starting_list(values,min_value, max_value) #regenerate the list
                displayInfo.set_list(myList) #redraw the list on the window
                sorting = False
            
            elif event.key == pygame.K_SPACE and sorting == False: #the space bar key to sort the list
                print('sorting now .....')
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(displayInfo, ascending)
            elif event.key == pygame.K_a and not sorting:#the A  key to sort the list in ascending order
                ascending = True
                print('sorting ascending ****')
            elif event.key == pygame.K_d and not sorting: #sorting in descending order
                ascending = False
    pygame.quit()

#
if __name__ == '__main__':
    main()
