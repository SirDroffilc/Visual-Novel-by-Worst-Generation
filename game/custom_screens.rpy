screen splash_screen():
    add Movie(play="gui/splashscreen.webm", loop=False, size=(650, 650)) xalign 0.5 yalign 0.5

# custom screens created 
screen chapter_title_text(txt):
    text txt:
        font gui.chapter_title_text 
        xalign 0.5
        yalign 0.5
        size 100 
        at chapter_fade

screen chapter_label_screen(chapter):
    zorder 100
    if chapter == 1:
        add "chapter1_label" xpos 30 ypos -20
    elif chapter == 2:
        add "chapter2_label" xpos -20 ypos 10
    elif chapter == 3:
        add "chapter3_label" xpos 50 ypos 0


transform chapter_fade:
    alpha 0.0 # start invisible
    linear 1.0 alpha 1.0   # fade in
    pause 1.0
    linear 1.0 alpha 0.0   # fade out

screen objective_text(txt, x=0.5, y=0.5):
    text txt:
        font gui.objective_text
        xalign x
        yalign y
        
    key "dismiss" action Return()

screen back_btn:
    zorder 100
    hbox:
        xalign 0.9
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("back_btn"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.5 yalign 0.5

screen main_key(filepath="keys/key1.png", x=0.5, y=0.5, zoom_size=1.0, clickable=False):
    if clickable:
        imagebutton:
            xalign x
            yalign y

            idle Transform(filepath, zoom=zoom_size)
            hover Transform(filepath, zoom=zoom_size+0.05)
            action [Hide("main_key"), Call("set_main_key_clicked", True)]
    else:
        add Transform(filepath, zoom=zoom_size) xalign x yalign y

screen keycard(filepath="keys/keycard1.png", x=0.5, y=0.5, zoom_size=1.0, clickable=False):
    if clickable:
        imagebutton:
            xalign x
            yalign y

            idle Transform(filepath, zoom=zoom_size)
            hover Transform(filepath, zoom=zoom_size+0.05)
            action [Hide("keycard"), Call("set_keycard_clicked", True)]
    else:
        add Transform(filepath, zoom=zoom_size) xalign x yalign y
        
#  <===== Chapter 1 Screens =====

screen puzzle_missing_pieces(num="101", x=0.5, y=0.5, zoom_size=0.3, clickable=True):
    if clickable:
        imagebutton:
            xalign x
            yalign y

            idle Transform(f"puzzle/missing_{num}_idle.png", zoom=zoom_size)
            hover Transform(f"puzzle/missing_{num}_hover.png", zoom=zoom_size)
            action [Hide("puzzle_missing_pieces"), Call("set_puzzle_missing_pieces_clicked", True)]
    else:
        add Transform(f"puzzle/missing_{num}_idle.png", zoom=zoom_size) xalign x yalign y

screen puzzle_missing_pieces_zoomed(num="101", x=0.8, y=0.5, zoom_size=1.2):
    imagebutton:
        xalign x
        yalign y 

        idle Transform(f"puzzle/zoomed_{num}.png", zoom=zoom_size)

screen f1_p1_buttons:

    hbox: # Enter elevator
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("elevator1")]

        text "Enter elevator" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 101 button
        xalign 0.35
        yalign 0.65
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("room101")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 102 button
        xalign 0.65
        yalign 0.65
        spacing 0

        text "Enter room" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("room102")]

    hbox: # Move to f1_p2
        xalign 0.5
        yalign 0.58
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("f1_p2")]

        text "Walk forward" xalign 0.0 yalign 0.5 size 25

screen f1_p2_buttons:

    hbox: # Move back to f1_p1
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("f1_p1")]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Main Room
        xalign 0.5
        yalign 0.55
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("main_room1")]

        text "Enter Main Room" xalign 0.0 yalign 0.5 size 25

    hbox: # Turn left, Move to f1_p3
        xalign 0.28
        yalign 0.6
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("f1_p3")]

        text "Turn left" xalign 0.0 yalign 0.5 size 25

    hbox: # Turn right, Move to f1_p4
        xalign 0.72
        yalign 0.6
        spacing 0

        text "Turn right" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("f1_p4")]

screen f1_p3_buttons:

    hbox: # Move back to f1_p2
        xalign 0.6
        yalign 0.9
        spacing 0

        text "Go back" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p3_buttons"), Jump("f1_p2")]

        

    hbox: # Enter Room 103
        xalign 0.5
        yalign 0.55
        spacing 0

        text "Enter room" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p3_buttons"), Jump("room103")]

screen f1_p4_buttons:

    hbox: # Move back to f1_p2
        xalign 0.3
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p4_buttons"), Jump("f1_p2")]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 104
        xalign 0.55
        yalign 0.5
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p4_buttons"), Jump("room104")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

screen drag_puzzle:
    modal True
    tag puzzle
    
    add Transform("puzzle/frame.png", size=(700, 700)) xalign 0.5 yalign 0.5 alpha 1

    key "rollback" action Return("back")
    draggroup:

        # Pieces
        drag:
            drag_name "piece_1"
            draggable True
            droppable False
            dragged drag_placed
            xpos 0.15
            ypos 0.7
            add Transform("puzzle/piece_1.png", size=(350, 350)) alpha 1

        drag:
            drag_name "piece_2"
            draggable True
            droppable False
            dragged drag_placed
            xpos 0.1
            ypos 0.1
            add Transform("puzzle/piece_2.png", size=(350, 350)) alpha 1

        drag:
            drag_name "piece_3"
            draggable True
            droppable False
            dragged drag_placed
            xpos 0.8
            ypos 0.05
            add Transform("puzzle/piece_3.png", size=(350, 350)) alpha 1
        drag:
            drag_name "piece_4"
            draggable True
            droppable False
            dragged drag_placed
            xpos 0.7
            ypos 0.1
            add Transform("puzzle/piece_4.png", size=(350, 350)) alpha 1
        drag:
            drag_name "piece_5"
            draggable True
            droppable False
            dragged drag_placed
            xpos 0.8
            ypos 0.6
            add Transform("puzzle/piece_5.png", size=(350, 350)) alpha 1
        drag:
            drag_name "piece_6"
            draggable True
            droppable False
            dragged drag_placed
            xpos 0.0
            ypos 0.5
            add Transform("puzzle/piece_6.png", size=(350, 350)) alpha 1
        drag:
            drag_name "piece_7"
            draggable True
            droppable False
            dragged drag_placed
            xpos 0.2
            ypos -0.05
            add Transform("puzzle/piece_7.png", size=(350, 350)) alpha 1
        drag:
            drag_name "piece_8"
            draggable True
            droppable False
            dragged drag_placed
            xpos 0.7
            ypos 0.4
            add Transform("puzzle/piece_8.png", size=(350, 350)) alpha 1
        drag:
            drag_name "piece_9"
            draggable True
            droppable False
            dragged drag_placed
            xpos 0.65
            ypos 0.7
            add Transform("puzzle/piece_9.png", size=(350, 350)) alpha 1
        # Drop zones
        drag:
            drag_name "1"
            draggable False
            droppable True
            xpos 0.315
            ypos 0.185
            add Transform("puzzle/slot_1.png", size=(350, 350)) alpha 0

        drag:
            drag_name "2"
            draggable False
            droppable True
            xpos 0.407
            ypos 0.1625
            add Transform("puzzle/slot_2.png", size=(350, 350)) alpha 0

        drag:
            drag_name "3"
            draggable False
            droppable True
            xpos 0.506
            ypos 0.19
            add Transform("puzzle/slot_3.png", size=(350, 350)) alpha 0
        drag:
            drag_name "A"
            draggable False
            droppable True
            xpos 0.3245
            ypos 0.335
            add Transform("puzzle/slot_4.png", size=(350, 350)) alpha 0
        drag:
            drag_name "B"
            draggable False
            droppable True
            xpos 0.4085
            ypos 0.335
            add Transform("puzzle/slot_5.png", size=(350, 350)) alpha 0
        drag:
            drag_name "C"
            draggable False
            droppable True
            xpos 0.493
            ypos 0.3355
            add Transform("puzzle/slot_6.png", size=(350, 350)) alpha 0
        drag:
            drag_name "D"
            draggable False
            droppable True
            xpos 0.3085
            ypos 0.4855
            add Transform("puzzle/slot_7.png", size=(350, 350)) alpha 0
        drag:
            drag_name "E"
            draggable False
            droppable True
            xpos 0.408
            ypos 0.51
            add Transform("puzzle/slot_8.png", size=(350, 350)) alpha 0
        drag:
            drag_name "F"
            draggable False
            droppable True
            xpos 0.5055
            ypos 0.483
            add Transform("puzzle/slot_9.png", size=(350, 350)) alpha 0
    
screen ethan_picture:
    add Transform("puzzle/frame.png", size=(630,630)) xalign 0.5 yalign 0.3
    add Transform("puzzle/ethan_picture.png", size=(500,500)) xalign 0.499 yalign 0.345



# ===== Chapter 1 Screens =====>


#  <===== Chapter 2 Screens =====
screen f2_p1_buttons:
    hbox: # Go to elevator
        xalign 0.8
        yalign 0.8

        text "Go to elevator" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p1_buttons"), Jump("elevator2")]

    hbox: # Enter Room 201
        xalign 0.4
        yalign 0.6
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p1_buttons"), Jump("room201")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25
    
    hbox: # Walk forward
        xalign 0.51
        yalign 0.5
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p1_buttons"), Jump("f2_p2")]

        text "Walk forward" xalign 0.0 yalign 0.5 size 25

screen f2_p2_buttons:
    hbox: # Go back
        xalign 0.1
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p2_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Walk forward
        xalign 0.6
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p2_buttons"), Jump("f2_p3")]

        text "Walk forward" xalign 0.0 yalign 0.5 size 25

screen f2_p3_buttons:
    hbox: # Go back
        xalign 0.4
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p3_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5 size 25
    
    hbox: # Enter Room 202
        xalign 0.4
        yalign 0.6
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p3_buttons"), Jump("room202")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Walk forward
        xalign 0.6
        yalign 0.55
        spacing 0

        text "Walk forward" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p3_buttons"), Jump("f2_p4")]

screen f2_p4_buttons:
    hbox: # Go back
        xalign 0.1
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p4_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 20X
        xalign 0.6
        yalign 0.55
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p4_buttons"), Call("room20X")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Go forward
        xalign 0.75
        yalign 0.47
        spacing 0
        
        text "Go forward" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p4_buttons"), Jump("f2_p5")]

screen f2_p5_buttons:
    hbox: # Go back
        xalign 0.45
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p5_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 203
        xalign 0.47
        yalign 0.53
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p5_buttons"), Jump("room203")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Go forward
        xalign 0.62
        yalign 0.45
        spacing 0

        text "Go forward" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p5_buttons"), Jump("f2_p6")]

screen f2_p6_buttons:
    hbox: # Go back
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p6_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Main Room
        xalign 0.5
        yalign 0.45
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p6_buttons"), Jump("main_room2")]

        text "Enter Main Room" xalign 0.0 yalign 0.5 size 25

screen ladder_layer(clickable=False):
    imagebutton:
        xalign 0.0
        yalign 0.6
        idle Null(width=450, height=500)
        hover Null(width=450, height=500)
        hovered [Show("hover_bg_overlay")]
        unhovered [Hide("hover_bg_overlay")]
        action [Hide("ladder_layer"), Hide("hover_bg_overlay"), Call("set_ladder_clicked", True)]

screen hover_bg_overlay():
    zorder 0
    add "bg room201_2_cut.png" xalign 0.5 yalign 1.0

screen f2_keycard:
    imagebutton:
        xalign 0.8
        yalign 0.5

        idle Transform("buttons/enter_room_button_idle.png", zoom=0.5)
        hover Transform("buttons/enter_room_button_hover.png", zoom=0.5)
        action [Hide("f2_keycard"), Call("set_keycard_clicked", True)]
# ===== Chapter 2 Screens =====>

#  <===== Chapter 3 Screens =====
screen f3_p1_buttons:
    hbox: # Go to elevator
        xalign 0.5
        yalign 0.9

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("elevator3")]

        text "Go to elevator" xalign 0.0 yalign 0.5 size 25
            
    hbox: # Enter Room 301
        xalign 0.2
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("room301")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 302
        xalign 0.8
        yalign 0.7
        spacing 0
        text "Enter room" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("room302")]

    hbox: # Go Forward
        xalign 0.5
        yalign 0.2
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("f3_p2")]

        text "Go forward" xalign 0.0 yalign 0.5 size 25

screen f3_p2_buttons:
    hbox: # Go back
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p2_buttons"), Jump("f3_p1")]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 303
        xalign 0.75
        yalign 0.7
        spacing 0

        text "Enter room" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p2_buttons"), Jump("room303")]

    hbox: # Enter Main Room 
        xalign 0.5
        yalign 0.57
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p2_buttons"), Jump("main_room3")]

        text "Enter Main Room" xalign 0.0 yalign 0.5 size 25

screen mini_game_start_btn:
    imagebutton:
        xalign 0.5
        yalign 0.75

        idle Transform("buttons/start_button.png", zoom=0.7)
        hover Transform("buttons/start_button.png", zoom=0.75)

        action [Hide("mini_game_start_btn"), Call("set_start_btn_clicked", True)]

screen f3_keycard:
    imagebutton:
        xalign 0.8
        yalign 0.5

        idle Transform("buttons/enter_room_button_idle.png", zoom=0.5)
        hover Transform("buttons/enter_room_button_hover.png", zoom=0.5)
        action [Hide("f3_keycard"), Call("set_keycard_clicked", True)]

screen splash_screen():
    add Movie(play="gui/splashscreen.webm", loop=False, size=(650, 650)) xalign 0.5 yalign 0.5

# custom screens created 

screen after_some_time_text(txt):
    text txt:
        font gui.after_some_time_text
        xalign 0.5
        yalign 0.5
        size 80

screen chapter_title_text(txt):
    text txt:
        font gui.chapter_title_text 
        xalign 0.5
        yalign 0.5
        size 100 
        at chapter_fade

screen chapter_label_screen(chapter):
    if chapter == 1:
        add "chapter1_label" xpos 30 ypos -20
    elif chapter == 2:
        add "chapter2_label" xpos -20 ypos 10
    elif chapter == 3:
        add "chapter3_label" xpos 50 ypos 0


transform chapter_fade:
    alpha 0.0 # start invisible
    linear 1.0 alpha 1.0   # fade in
    pause 1.0
    linear 1.0 alpha 0.0   # fade out

screen objective_text(txt, x=0.5, y=0.5):
    text txt:
        font gui.objective_text
        xalign x
        yalign y
        
    key "dismiss" action Return()

screen back_btn:
    zorder 100
    hbox:
        xalign 0.9
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("back_btn"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.5 yalign 0.5

#  <===== Chapter 1 Screens =====

screen puzzle_missing_pieces(num="101", x=0.5, y=0.5, zoom_size=0.3, clickable=True):
    if clickable:
        imagebutton:
            xalign x
            yalign y

            idle Transform(f"puzzle/missing_{num}_idle.png", zoom=zoom_size)
            hover Transform(f"puzzle/missing_{num}_hover.png", zoom=zoom_size)
            action [Hide("puzzle_missing_pieces"), Call("set_puzzle_missing_pieces_clicked", True)]
    else:
        add Transform(f"puzzle/missing_{num}_idle.png", zoom=zoom_size) xalign x yalign y
screen puzzle_missing_pieces_zoomed(num="101", x=0.8, y=0.5, zoom_size=1.2):
    imagebutton:
        xalign x
        yalign y 

        idle Transform(f"puzzle/zoomed_{num}.png", zoom=zoom_size)

screen f1_p1_buttons:

    hbox: # Enter elevator
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("elevator1")]

        text "Enter elevator" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 101 button
        xalign 0.35
        yalign 0.65
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("room101")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 102 button
        xalign 0.65
        yalign 0.65
        spacing 0

        text "Enter room" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("room102")]

    hbox: # Move to f1_p2
        xalign 0.5
        yalign 0.58
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("f1_p2")]

        text "Walk forward" xalign 0.0 yalign 0.5 size 25

screen f1_p2_buttons:

    hbox: # Move back to f1_p1
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("f1_p1")]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Main Room
        xalign 0.5
        yalign 0.55
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("main_room1")]

        text "Enter Main Room" xalign 0.0 yalign 0.5 size 25

    hbox: # Turn left, Move to f1_p3
        xalign 0.28
        yalign 0.6
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("f1_p3")]

        text "Turn left" xalign 0.0 yalign 0.5 size 25

    hbox: # Turn right, Move to f1_p4
        xalign 0.72
        yalign 0.6
        spacing 0

        text "Turn right" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("f1_p4")]

screen f1_p3_buttons:

    hbox: # Move back to f1_p2
        xalign 0.6
        yalign 0.9
        spacing 0

        text "Go back" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p3_buttons"), Jump("f1_p2")]

        

    hbox: # Enter Room 103
        xalign 0.5
        yalign 0.55
        spacing 0

        text "Enter room" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p3_buttons"), Jump("room103")]

screen f1_p4_buttons:

    hbox: # Move back to f1_p2
        xalign 0.3
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p4_buttons"), Jump("f1_p2")]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 104
        xalign 0.55
        yalign 0.5
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p4_buttons"), Jump("room104")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

screen f1_keycard:
    imagebutton:
        xalign 0.8
        yalign 0.5

        idle Transform("buttons/enter_room_button_idle.png", zoom=0.5)
        hover Transform("buttons/enter_room_button_hover.png", zoom=0.5)
        action [Hide("f1_keycard"), Call("set_keycard_clicked", True)]

# ===== Chapter 1 Screens =====>


#  <===== Chapter 2 Screens =====
screen f2_p1_buttons:
    hbox:
        xalign 0.8
        yalign 0.7

        text "Go to elevator" xalign 0.0 yalign 0.5 size 25

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p1_buttons"), Jump("elevator2")]

    hbox: # Enter Room 201
        xalign 0.4
        yalign 0.6
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p1_buttons"), Jump("room201")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25
    
    hbox: # Walk forward
        xalign 0.48
        yalign 0.52
        spacing 0

        text "Walk forward" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p1_buttons"), Jump("f2_p2")]

        

screen f2_p2_buttons:
    hbox: # Go back
        xalign 0.1
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p2_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Walk forward
        xalign 0.65
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p2_buttons"), Jump("f2_p3")]

        text "Walk forward" xalign 0.0 yalign 0.5 size 25

screen f2_p3_buttons:
    hbox: # Go back
        xalign 0.4
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p3_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5 size 25
    
    hbox: # Enter Room 202
        xalign 0.43
        yalign 0.6
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p3_buttons"), Jump("room202")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Walk forward
        xalign 0.6
        yalign 0.5
        spacing 0

        text "Walk forward" xalign 0.0 yalign 0.5 size 25

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p3_buttons"), Jump("f2_p4")]

        

screen f2_p4_buttons:
    hbox: # Go back
        xalign 0.1
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p4_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 20X
        xalign 0.6
        yalign 0.53
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p4_buttons"), Call("room20X")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Go forward
        xalign 0.75
        yalign 0.47
        spacing 0

        text "Go forward" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p4_buttons"), Jump("f2_p5")]

        

screen f2_p5_buttons:
    hbox: # Go back
        xalign 0.4
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p5_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 203
        xalign 0.48
        yalign 0.55
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p5_buttons"), Jump("room203")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Go forward
        xalign 0.6
        yalign 0.5
        spacing 0

        text "Go forward" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p5_buttons"), Jump("f2_p6")]

        

screen f2_p6_buttons:
    hbox: # Go back
        xalign 0.5
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p6_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Main Room
        xalign 0.5
        yalign 0.43
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p6_buttons"), Jump("main_room2")]

        text "Enter Main Room" xalign 0.0 yalign 0.5 size 25

screen ladder_inactive:
    imagebutton:
        xalign 0.2
        yalign 0.2
        idle Transform("buttons/enter_room_button_idle.png", zoom=0.3)

screen ladder_active:
    imagebutton:
        xalign 0.2
        yalign 0.2
        idle Transform("buttons/enter_room_button_idle.png", zoom=0.3)
        hover Transform("buttons/enter_room_button_hover.png", zoom=0.3)
        action Call("set_ladder_clicked", True)

screen f2_keycard:
    imagebutton:
        xalign 0.8
        yalign 0.5

        idle Transform("buttons/enter_room_button_idle.png", zoom=0.5)
        hover Transform("buttons/enter_room_button_hover.png", zoom=0.5)
        action [Hide("f2_keycard"), Call("set_keycard_clicked", True)]
# ===== Chapter 2 Screens =====>

#  <===== Chapter 3 Screens =====
screen f3_p1_buttons:
    hbox:
        xalign 0.5
        yalign 0.9

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("elevator3")]

        text "Go to elevator" xalign 0.0 yalign 0.5 size 25
            
    hbox: # Enter Room 301
        xalign 0.2
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("room301")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 302
        xalign 0.8
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("room302")]

        text "Enter room" xalign 0.0 yalign 0.5 size 25

    hbox: # Go Forward
        xalign 0.5
        yalign 0.65
        spacing 0
        
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("f3_p2")]

        text "Go forward" xalign 0.0 yalign 0.5 size 25

screen f3_p2_buttons:
    hbox: # Go back
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p2_buttons"), Jump("f3_p1")]

        text "Go back" xalign 0.0 yalign 0.5 size 25

    hbox: # Enter Room 303
        xalign 0.8
        yalign 0.7
        spacing 0

        text "Enter room" xalign 0.0 yalign 0.5 size 25
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p2_buttons"), Jump("room303")]

    hbox: # Enter Main Room 
        xalign 0.5
        yalign 0.55
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p2_buttons"), Jump("main_room3")]

        text "Enter Main Room" xalign 0.0 yalign 0.5 size 25

screen mini_game_start_btn:
    imagebutton:
        xalign 0.5
        yalign 0.75

        idle Transform("buttons/start_button.png", zoom=0.7)
        hover Transform("buttons/start_button.png", zoom=0.75)

        action [Hide("mini_game_start_btn"), Call("set_start_btn_clicked", True)]

screen f3_keycard:
    imagebutton:
        xalign 0.8
        yalign 0.5

        idle Transform("buttons/enter_room_button_idle.png", zoom=0.5)
        hover Transform("buttons/enter_room_button_hover.png", zoom=0.5)
        action [Hide("f3_keycard"), Call("set_keycard_clicked", True)]

# ===== Chapter 3 Screens =====>