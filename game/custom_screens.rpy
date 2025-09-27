# custom screens created 

screen chapter_title_text(txt):
    text txt:
        xalign 0.5
        yalign 0.5
        at chapter_fade

transform chapter_fade:
    alpha 0.0 # start invisible
    linear 1.0 alpha 1.0   # fade in
    pause 1.0
    linear 1.0 alpha 0.0   # fade out

screen objective_text(txt, x=0.5, y=0.5):
    text txt:
        xalign x
        yalign y
        
    key "dismiss" action Return()

screen back_btn:
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

screen puzzle_pieces(x=0.5, y=0.5, zoomSize=0.05):
    vbox:
        xalign x
        yalign y
        spacing 0
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 0
            imagebutton:
                idle Transform("buttons/enter_room_button_idle.png", zoom=zoomSize)
                hover Transform("buttons/enter_room_button_hover.png", zoom=zoomSize)
                action [Hide("puzzle_pieces"), Call("set_puzzle_pieces_clicked", True)]
            imagebutton:
                idle Transform("buttons/enter_room_button_idle.png", zoom=zoomSize)
                hover Transform("buttons/enter_room_button_hover.png", zoom=zoomSize)
                action [Hide("puzzle_pieces"), Call("set_puzzle_pieces_clicked", True)]
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=zoomSize)
            hover Transform("buttons/enter_room_button_hover.png", zoom=zoomSize)
            action [Hide("puzzle_pieces"), Call("set_puzzle_pieces_clicked", True)]

screen puzzle_pieces_zoomed(x=0.8, y=0.5, zoomSize=0.4):
    vbox:
        xalign x
        yalign y
        spacing 0
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 0
            imagebutton:
                idle Transform("buttons/enter_room_button_idle.png", zoom=zoomSize)
                hover Transform("buttons/enter_room_button_hover.png", zoom=zoomSize)
            imagebutton:
                idle Transform("buttons/enter_room_button_idle.png", zoom=zoomSize)
                hover Transform("buttons/enter_room_button_hover.png", zoom=zoomSize)
        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=zoomSize)
            hover Transform("buttons/enter_room_button_hover.png", zoom=zoomSize)

screen f1_p1_buttons:

    hbox: # Enter elevator
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("elevator1")]

        text "Enter elevator" xalign 0.0 yalign 0.5

    hbox: # Enter Room 101 button
        xalign 0.1
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("room101")]

        text "Enter room" xalign 0.0 yalign 0.5

    hbox: # Enter Room 102 button
        xalign 0.85
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("room102")]

        text "Enter room" xalign 0.0 yalign 0.5

    hbox: # Move to f1_p2
        xalign 0.5
        yalign 0.5
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p1_buttons"), Jump("f1_p2")]

        text "Walk forward" xalign 0.0 yalign 0.5

screen f1_p2_buttons:

    hbox: # Move back to f1_p1
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("f1_p1")]

        text "Go back" xalign 0.0 yalign 0.5

    hbox: # Enter Main Room
        xalign 0.5
        yalign 0.35
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("main_room1")]

        text "Enter Main Room" xalign 0.0 yalign 0.5

    hbox: # Turn left, Move to f1_p3
        xalign 0.2
        yalign 0.5
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("f1_p3")]

        text "Turn left" xalign 0.0 yalign 0.5

    hbox: # Turn right, Move to f1_p4
        xalign 0.8
        yalign 0.5
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p2_buttons"), Jump("f1_p4")]

        text "Turn right" xalign 0.0 yalign 0.5

screen f1_p3_buttons:

    hbox: # Move back to f1_p2
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p3_buttons"), Jump("f1_p2")]

        text "Go back" xalign 0.0 yalign 0.5

    hbox: # Enter Room 103
        xalign 0.8
        yalign 0.5
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p3_buttons"), Jump("room103")]

        text "Enter room" xalign 0.0 yalign 0.5

screen f1_p4_buttons:

    hbox: # Move back to f1_p2
        xalign 0.5
        yalign 0.9
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p4_buttons"), Jump("f1_p2")]

        text "Go back" xalign 0.0 yalign 0.5

    hbox: # Enter Room 104
        xalign 0.2
        yalign 0.5
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f1_p4_buttons"), Jump("room104")]

        text "Enter room" xalign 0.0 yalign 0.5

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
        xalign 0.5
        yalign 0.85

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p1_buttons"), Jump("elevator2")]

        text "Go to elevator" xalign 0.0 yalign 0.5
        
    hbox: # Enter Room 201
        xalign 0.2
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p1_buttons"), Jump("room201")]

        text "Enter room" xalign 0.0 yalign 0.5
    
    hbox: # Walk forward
        xalign 0.6
        yalign 0.4
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p1_buttons"), Jump("f2_p2")]

        text "Walk forward" xalign 0.0 yalign 0.5

screen f2_p2_buttons:
    hbox: # Go back
        xalign 0.5
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p2_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5

    hbox: # Walk forward
        xalign 0.5
        yalign 0.4
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p2_buttons"), Jump("f2_p3")]

        text "Walk forward" xalign 0.0 yalign 0.5

screen f2_p3_buttons:
    hbox: # Go back
        xalign 0.5
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p3_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5
    
    hbox: # Enter Room 202
        xalign 0.2
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p3_buttons"), Jump("room202")]

        text "Enter room" xalign 0.0 yalign 0.5

    hbox: # Walk forward
        xalign 0.5
        yalign 0.4
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p3_buttons"), Jump("f2_p4")]

        text "Walk forward" xalign 0.0 yalign 0.5

screen f2_p4_buttons:
    hbox: # Go back
        xalign 0.5
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p4_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5

    hbox: # Enter Room 20X
        xalign 0.2
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p4_buttons"), Call("room20X")]

        text "Enter room" xalign 0.0 yalign 0.5

    hbox: # Go forward
        xalign 0.5
        yalign 0.4
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p4_buttons"), Jump("f2_p5")]

        text "Go forward" xalign 0.0 yalign 0.5

screen f2_p5_buttons:
    hbox: # Go back
        xalign 0.5
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p5_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5

    hbox: # Enter Room 203
        xalign 0.2
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p5_buttons"), Jump("room203")]

        text "Enter room" xalign 0.0 yalign 0.5

    hbox: # Go forward
        xalign 0.5
        yalign 0.4
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p5_buttons"), Jump("f2_p6")]

        text "Go forward" xalign 0.0 yalign 0.5

screen f2_p6_buttons:
    hbox: # Go back
        xalign 0.5
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p6_buttons"), Call("set_back_btn_clicked", True)]

        text "Go back" xalign 0.0 yalign 0.5

    hbox: # Enter Main Room
        xalign 0.5
        yalign 0.4
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f2_p6_buttons"), Jump("main_room2")]

        text "Enter Main Room" xalign 0.0 yalign 0.5

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
        yalign 0.85

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("elevator3")]

        text "Go to elevator" xalign 0.0 yalign 0.5
            
    hbox: # Enter Room 301
        xalign 0.2
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("room301")]

        text "Enter room" xalign 0.0 yalign 0.5

    hbox: # Enter Room 302
        xalign 0.8
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("room302")]

        text "Enter room" xalign 0.0 yalign 0.5

    hbox: # Go Forward
        xalign 0.5
        yalign 0.4
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p1_buttons"), Jump("f3_p2")]

        text "Go forward" xalign 0.0 yalign 0.5

screen f3_p2_buttons:
    hbox: # Go back
        xalign 0.5
        yalign 0.85
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p2_buttons"), Jump("f3_p1")]

        text "Go back" xalign 0.0 yalign 0.5

    hbox: # Enter Room 303
        xalign 0.8
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p2_buttons"), Jump("room303")]

        text "Enter room" xalign 0.0 yalign 0.5

    hbox: # Enter Main Room 
        xalign 0.5
        yalign 0.4
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("f3_p2_buttons"), Jump("main_room3")]

        text "Enter room" xalign 0.0 yalign 0.5
# ===== Chapter 3 Screens =====>