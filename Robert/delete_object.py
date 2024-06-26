from graphics import Canvas
import time

def main(): 
    canvas = Canvas(400, 400)
    canvas.create_text(200, 350, "Click to Continue", anchor='center', font_size = 24, color='blue')
    test_list(canvas)
    test_tuple(canvas)
    

def test_list(canvas):
    colliding_list = create_list(canvas)
    print('colliding list type',type(colliding_list))
    text_list1 = canvas.create_text(200, 50, "List's objects", anchor='center', font_size = 24, color='green')
    canvas.wait_for_click()

    for obj in colliding_list:
        canvas.delete(obj)
        canvas.wait_for_click()

    text_list2 = canvas.create_text(200, 200, "Done with List", anchor='center', font_size = 24, color='green')

    canvas.wait_for_click()
    canvas.delete(text_list1)
    canvas.delete(text_list2)


def test_tuple(canvas):
    colliding_tuple = create_tuple(canvas)
    print('colliding tuple type', type(colliding_tuple))
    canvas.create_text(200, 50, "Tuple's objects", anchor='center', font_size = 24, color='green')
    canvas.wait_for_click()

    for obj in colliding_tuple:
        canvas.delete(obj)
        canvas.wait_for_click()

    canvas.create_text(200, 200, "Done with tuple", anchor='center', font_size = 24, color='green')
    canvas.wait_for_click()

def create_list(canvas):
    '''
    return a list of two objects
    '''
    colliding_list = []
    for i in range(2):
        list_obj = canvas.create_rectangle(100, 100 + 100 * i, 150, 150 + 100 * i, 'red')
        colliding_list.append(list_obj)
    return colliding_list

def create_tuple(canvas):
    '''
    return a tuple of two objects
    '''
    tuple_obj_1 = canvas.create_oval(100, 100, 150, 150, 'blue')
    tuple_obj_2 = canvas.create_oval(100, 200, 150, 250, 'blue')
    return tuple_obj_1, tuple_obj_2

if __name__ == '__main__':
    main()

