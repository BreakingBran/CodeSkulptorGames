# implementation of card game - Memory

import simplegui
import random

#Globals

Card_Height = 200
Card_Width = 100
Highscore = 100

# helper function to initialize globals
def new_game():
    global random_values_list, memoary, selected, selected2, last_click, Turn_Counter, Clicks, Highscore
    random_values_list = [x for x in range(8)]
    random_values_list.extend(random_values_list)
    random.shuffle(random_values_list)
    random.shuffle(random_values_list)
    random_values_list.append(10)
    memoary = {}
    for values in range(16):
        memoary[values] = random_values_list[values]
    selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    selected2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    last_click = -1
    Turn_Counter = 0
    Clicks = 0
    label.set_text('Turns = '+str(Turn_Counter))
    #print random_values_list

     
# define event handlers
def mouseclick(pos):
    global selected, selected2, last_click, random_values_list, Turn_Counter, Clicks    
    click = list(pos)
    click = click[0]/100
    if not selected[click] == 2 and not selected[click] == 1:
        selected[click] = 1 
    else:
        last_click = click
        return
    #print '_________________________________________'    #Print    
    #print 'Test 1 rv', random_values_list   #Print
    #print 'Test 1 s1', selected				#Print
    #print 'Test 1 s2', selected2, '\n'		#Print
    #print 'Sum test', selected.count(1), '\n'    #Print      
    if selected.count(1) >= 3:        
        selected = list(selected2)
        if not selected[click] == 2:
            selected[click] = 1  
    #    print 'Test 3 s1', selected			#Print
    #    print 'Test 3 s2', selected2, '\n'  #Print      
    elif random_values_list[click] == random_values_list[last_click] and not last_click == click:
        selected2[click] = 2
        selected2[last_click] = 2
    #    print 'Test 4 s1', selected			#Print        
    #    print 'Test 4 s2', selected2, '\n'	#Print
    if not last_click == -1 and not click == last_click and selected.count(1) == 2:
            Turn_Counter += 1
            label.set_text('Turns = '+str(Turn_Counter))
    last_click = click     
    #print 'Test 2 s1', selected				#Print
    #print 'Test 2 s2', selected2			#Print
    #print '_________________________________________'	#Print
    print Turn_Counter
     
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):    
    global random_values_list, memoary, selected, selected2, Highscore
    polygon_pos = [[0,0],[0,Card_Height],[Card_Width,Card_Height],[Card_Width,0]]
    polygon_pos2 = polygon_pos    
    for values in range(16):
        polygon_pos = polygon_pos2
        canvas.draw_polygon(polygon_pos,1,'yellow','Green')
        if not values == 15:canvas.draw_line(polygon_pos[2],polygon_pos[3],8,'orange')        
        if selected[values] == 1 or selected[values] == 2: 
            canvas.draw_text(str(memoary[values]),[polygon_pos[1][0]+35,polygon_pos[1][1]-80],50,'black')
            if selected2[values] == 2:
                canvas.draw_polygon(polygon_pos,1,'orange','Orange')
                canvas.draw_text(str(memoary[values]),[polygon_pos[1][0]+35,polygon_pos[1][1]-80],50,'black')
            elif selected[values] == 1:
                canvas.draw_polygon(polygon_pos,1,'yellow','black')
                canvas.draw_text(str(memoary[values]),[polygon_pos[1][0]+35,polygon_pos[1][1]-80],50,'white')
        for ints in range(4):
             polygon_pos2[ints][0] = polygon_pos[ints][0] + Card_Width    
    canvas_size = [(0,0),(0,200),(1600,200),(1600,0)]
    if selected2.count(2) == 16:
        if Turn_Counter < Highscore:
            Highscore = Turn_Counter
            print Turn_Counter
            print Highscore
        canvas.draw_polygon(canvas_size,1,'orange','orange')
        canvas.draw_text('Your Highscore is '+str(Highscore),[Card_Width*4,Card_Height/2+20],70,'black')        
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory",Card_Width*16 , Card_Height)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
