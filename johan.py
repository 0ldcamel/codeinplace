from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 500
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

def main():
    button_vs_num = draw_buttons() # get dict from function draw_buttons
    buttons = list(button_vs_num.keys()) # get list of keys in dict
    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        overlap = canvas.find_overlapping(x, y, x, y)
        if len(overlap) == 1:
            if canvas.get_new_mouse_clicks(): # A click in a defined shape.
                print("")
                print("Click in shape.")
                print(overlap, f"; x = {x}, y = {y}")
                button_value = button_vs_num[overlap[0]]
                print('You clicked', button_value, 'button.')
                
        if canvas.get_new_mouse_clicks(): # A click outside any shape.
            print("")
            print("Click outside shape.")
            print(overlap, f"; x = {x}, y = {y}")

def draw_buttons():
    # Button GUI.
    numbers = [7, 8, 9,'reset', 'BP', 4, 5, 6, 'CE', 'BCE', 1, 2 ,3, 'Nah', 'Nada', 'Yuck', 0, 'None']
    distance_x, distance_y = 50, 40
    start_x, start_y = 100, 285
    button_vs_num = {}
    for j in range(4): # as there are 4 rows of buttons
        y = start_y + j * distance_y
        row = j * 5
        for i in range(5): # as there are 5 columns of buttons
            if j == 2 and i == 3: # draw big button =
                equal_to = canvas.create_rectangle(250, 365, 335, 390, 'white', 'black')
                canvas.create_text(290, 372, "=") # Shape 28
                button_vs_num[equal_to] = '='
            elif j == 2 and i == 4: # skip left of button 0
                continue
            elif j == 3 and (i == 0 or i > 1): # skip right of button 0
                continue
            else: # draw button from 0 - 9 and other small buttons (CE, BCE, BP, reset)
                x = start_x + i * distance_x
                num_button = button_gui(x, y)
                num_text = canvas.create_text(x + 18, y + 13, text = str(numbers[i + row]), anchor='center')
                button_vs_num[num_button] = numbers[i + row]
    print(button_vs_num)
    return button_vs_num

def button_gui(x, y):
    # The button's source code, excluding equal_to.
    button_width, button_height = 35, 25
    button = canvas.create_rectangle(x, y, x + button_width, y + button_height,'white', 'black')
    return button

if __name__ == '__main__':
    main()

