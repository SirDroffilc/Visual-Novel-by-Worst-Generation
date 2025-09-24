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
    

screen hallway1_buttons():

    # Room 101
    hbox:
        xalign 0.1
        yalign 0.7
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("hallway1_buttons"), Call("room101")]

        text "Room 101" xalign 0.0 yalign 0.5

    # Room 102
    hbox:
        xalign 0.85
        yalign 0.7
        spacing 0

        text "Room 102" xalign 0.0 yalign 0.5

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("hallway1_buttons"), Call("room102")]

    # Room 103
    hbox:
        xalign 0.3
        yalign 0.6
        spacing 0

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("hallway1_buttons"), Call("room103")]

        text "Room 103" xalign 0.0 yalign 0.5

    # Room 104
    hbox:
        xalign 0.7
        yalign 0.6
        spacing 0

        text "Room 104" xalign 0.0 yalign 0.5 

        imagebutton:
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("hallway1_buttons"), Call("room104")]

    # Main Room
    vbox:
        xalign 0.5
        yalign 0.55
        spacing 0

        imagebutton:
            xalign 0.5
            yalign 0.5
            idle Transform("buttons/enter_room_button_idle.png", zoom=0.1)
            hover Transform("buttons/enter_room_button_hover.png", zoom=0.1)
            action [Hide("hallway1_buttons"), Call("mainrm1")]

        text "Main Room" xalign 0.5 yalign 0.5
