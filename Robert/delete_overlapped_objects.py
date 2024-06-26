from graphics import Canvas
import random

def main():
    canvas = Canvas(400, 400)
    list_of_objects = create_objects(canvas)
    delete_object(canvas, list_of_objects)

def create_objects(canvas):
    size = 30
    list_of_objects = []
    for i in range(6):
        row = i * 60
        for j in range(7):
            left_x = 30 + 50 * j
            top_y = 30 + row
            color = get_color()
            obj = canvas.create_oval(left_x, top_y, left_x + size, top_y + size, color=color)
            list_of_objects.append(obj) # add object to list so they can be tracked.
    return list_of_objects

def delete_object(canvas, list_of_objects):
    start_list = list_of_objects
    while len(start_list) > 0: # quite program when no more object to click
        canvas.wait_for_click()
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        ol = canvas.find_overlapping(x, y, x + 1, y + 1)
        for item in ol:
            print(f'delete object {item} at coordinates {x}, {y}')
            canvas.delete(item)
            start_list.remove(item) # update list, removing the deleted object.

            canvas.update()
    
def get_color():
    colors = ['green', 'red', 'blue', 'white', 'yellow']
    return random.choice(colors)
    

if __name__ == '__main__':
    main()