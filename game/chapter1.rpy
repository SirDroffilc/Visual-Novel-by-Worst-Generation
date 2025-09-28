label chapter1:
    scene black with fade

    show screen chapter_title_text("Chapter 1 Shadows Ahead")
    pause 3.0
    hide screen chapter_title_text

    call screen objective_text(chap0_objective_find_clues)
    show screen objective_text(chap0_objective_find_clues, 0.97, 0.03)

    show screen chapter_label_screen(1) 
    jump f1_p1

label elevator1:
    scene black with fade
    if not key_card1_acquired:
        "Access Denied. F1 Key Card Required."
        ethan "I need the Key Card."
    
    else:
        "Elevator door opening..."
        hide screen chapter_label_screen
        jump chapter2

label f1_p1:
    scene bg f1p1 with fade
    
    while True:
        if pieces_count == 9 and not all_pieces_obtained:
            $ all_pieces_obtained = True
            call screen objective_text(chap1_objective_go_puzzle_room)
            show screen objective_text(chap1_objective_go_puzzle_room, 0.98, 0.1)

        call set_back_btn_clicked(False)
        call set_puzzle_missing_pieces_clicked(False)

        show screen f1_p1_buttons
        pause

    return

label f1_p2:
    if not from_locked_room:
        scene bg f1p2 with fade
        
    $ from_locked_room = False
    while True:
        if pieces_count == 9 and not all_pieces_obtained:
            $ all_pieces_obtained = True
            call screen objective_text(chap1_objective_go_puzzle_room)
            show screen objective_text(chap1_objective_go_puzzle_room, 0.98, 0.1)

        call set_back_btn_clicked(False)
        call set_puzzle_missing_pieces_clicked(False)

        show screen f1_p2_buttons
        pause

    return

label f1_p3:
    scene bg f1p3 with fade
    
    while True:
        if pieces_count == 9 and not all_pieces_obtained:
            $ all_pieces_obtained = True
            call screen objective_text(chap1_objective_go_puzzle_room)
            show screen objective_text(chap1_objective_go_puzzle_room, 0.98, 0.1)

        call set_back_btn_clicked(False)
        call set_puzzle_missing_pieces_clicked(False)

        show screen f1_p3_buttons
        pause

    return

label f1_p4:
    scene bg f1p4 with fade
    
    while True:
        if pieces_count == 9 and not all_pieces_obtained:
            $ all_pieces_obtained = True
            call screen objective_text(chap1_objective_go_puzzle_room)
            show screen objective_text(chap1_objective_go_puzzle_room, 0.98, 0.1)

        call set_back_btn_clicked(False)
        call set_puzzle_missing_pieces_clicked(False)

        show screen f1_p4_buttons
        pause

    return

label room101: # Empty Room (Starting Room)
    scene bg room101_1 with fade
    if not room101_pieces_taken:
        show screen puzzle_missing_pieces("101", x=0.37, y=0.53, zoom_size=0.1, clickable=False) 

    "This is where I woke up."
    "Nothing's here—just a bed and a table with a bunch of random junk on top of it."
    window hide

    call set_back_btn_clicked(False)
    call set_puzzle_missing_pieces_clicked(False)
    while not back_btn_clicked:
        if not room101_pieces_taken:
            show screen puzzle_missing_pieces("101", x=0.37, y=0.53, zoom_size=0.1, clickable=True)
            if puzzle_missing_pieces_clicked: # piece-2, 4, 9
                hide screen back_btn
                hide screen puzzle_missing_pieces
                show screen puzzle_missing_pieces_zoomed("101")
                if puzzle_evt_flag:
                    show frame_overlay at frame_slide_from_left
                    show ethan smile at sprite_slide_from_left
                    ethan "Found the pieces."

                elif pieces_count <= 0:
                    show frame_overlay at frame_slide_from_left
                    show ethan confused at sprite_slide_from_left
                    ethan "Are these puzzle pieces? What are these for?"

                else:
                    show frame_overlay at frame_slide_from_left
                    show ethan confused at sprite_slide_from_left
                    ethan "Again? What are these pieces for?"

                menu: 
                    "Take the pieces?"
                    "Yes":
                        ethan "I'll take them."
                        $ pieces_count += 3
                        $ room101_pieces_taken = True
    
                        if puzzle_evt_flag:
                            "I got [pieces_count] of these pieces now."
                            show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
                    "No":
                        ethan "I'll leave them here."
                        hide screen puzzle_missing_pieces_zoomed
                        hide frame_overlay
                        hide ethan
                        show screen puzzle_missing_pieces("101", x=0.37, y=0.53, zoom_size=0.1, clickable=False)
                        call set_puzzle_missing_pieces_clicked(False)
        show screen back_btn

        pause
    
    hide back_btn
    hide screen puzzle_missing_pieces
    hide screen puzzle_missing_pieces_zoomed
    
    jump f1_p1

label room102: # Puzzle Room
    if all_pieces_obtained:
        jump puzzle_mini_game

    scene bg puzzle_room_1 with fade
    pause

    if puzzle_evt_flag:
        "I have to look for the puzzle pieces."
        "...the other rooms, maybe?"
    
    else:
        show ethan default at sprite_slide_from_left
        ethan "This room looks totally different from the outside..."
        ethan "Wait... this... looks like the arcade I used to go to with a friend."
        ethan "Is it a coincidence?"
        ethan "...That's not important."
        ethan "What should I even look for?"
        show ethan confused with Dissolve(0.1)
        ethan "Wait... something's written on the wall."
        scene bg puzzle_room_2 with fade
        "\"Assemble the pieces\"?"
        hide ethan with dissolve
        call screen objective_text(chap1_objective_puzzle_evt)
        show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
        $ puzzle_evt_flag = True

        show ethan confused at sprite_slide_from_left
        ethan "A jigsaw puzzle? Seriously?"
        show ethan smacked with Dissolve(0.1)
        ethan "Ugh, but it's the only lead I've got."
        ethan "...fine."

        hide ethan with dissolve
    
    while not back_btn_clicked:
        show screen back_btn
        pause
    
    jump f1_p1

label room103: # Office Room
    scene bg room103 with fade
    if not room103_pieces_taken:
        show screen puzzle_missing_pieces("103", x=0.08, y=0.43, zoom_size=0.12, clickable=False) 
    pause
    "This room looks like an office… maybe for some kind of company."
    "...It doesn't feel like anyone's worked here in years."
    
    while not back_btn_clicked:
        show screen back_btn
        if not room103_pieces_taken: 
            show screen puzzle_missing_pieces("103", x=0.08, y=0.43, zoom_size=0.12, clickable=True)

            if puzzle_missing_pieces_clicked: # piece 6, 8
                hide screen back_btn
                ethan "...Wait, what's that on the table?"
                hide screen puzzle_missing_pieces
                show screen puzzle_missing_pieces_zoomed("103")
                if puzzle_evt_flag:
                    show frame_overlay at frame_slide_from_left
                    show ethan smile at sprite_slide_from_left
                    ethan "Found them."

                elif pieces_count <= 0:
                    show frame_overlay at frame_slide_from_left
                    show ethan default at sprite_slide_from_left
                    ethan "Are these puzzle pieces?"

                else:
                    show frame_overlay at frame_slide_from_left
                    show ethan confused at sprite_slide_from_left
                    ethan "Another set of pieces? What are these for?"

                menu: 
                    "Take the pieces?"
                    "Yes":
                        ethan "Yeah, I better take these pieces."
                        $ pieces_count += 2
                        $ room103_pieces_taken = True
    
                        if puzzle_evt_flag:
                            ethan "I got [pieces_count] of them now."
                            show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
                    "No":
                        ethan "I'll leave them here."
                        hide screen puzzle_missing_pieces_zoomed
                        hide frame_overlay
                        hide ethan
                        show screen puzzle_missing_pieces("103", x=0.08, y=0.43, zoom_size=0.12, clickable=False) 
                        call set_puzzle_missing_pieces_clicked(False)

        pause
    
    hide back_btn
    hide screen puzzle_missing_pieces
    hide screen puzzle_missing_pieces_zoomed
    
    jump f1_p3

label room104: # Messy Room
    scene bg room104 with fade
    if not room104_pieces_taken:
        show screen puzzle_missing_pieces("104", x=0.57, y=0.69, zoom_size=0.12, clickable=False) 
    pause

    "Ugh, what's that smell?"
    "It's like a mix of dust, dirty laundry, and… rotten food left out for weeks."
    "This whole place feels like a garbage dump, not a bedroom."

    while not back_btn_clicked:
        show screen back_btn
        if not room104_pieces_taken:
            show screen puzzle_missing_pieces("104", x=0.57, y=0.69, zoom_size=0.12, clickable=True)

            if puzzle_missing_pieces_clicked: # piece-1, 3, 5, 7
                hide screen back_btn
                ethan "...Wait, is that—under the table?"
                hide screen puzzle_missing_pieces
                show screen puzzle_missing_pieces_zoomed("104")

                if puzzle_evt_flag:
                    show frame_overlay at frame_slide_from_left
                    show ethan smile at sprite_slide_from_left
                    ethan "Oh, the pieces! There they are."

                elif pieces_count <= 0:
                    show frame_overlay at frame_slide_from_left
                    show ethan default at sprite_slide_from_left
                    ethan "Are these puzzle pieces?"

                else:
                    show frame_overlay at frame_slide_from_left
                    show ethan confused at sprite_slide_from_left
                    ethan "What's with all these puzzle pieces?"

                menu: 
                    "Take the pieces?"
                    "Yes":
                        ethan "I'll take them."
                        $ pieces_count += 4
                        $ room104_pieces_taken = True
                        if puzzle_evt_flag:
                            ethan "I got [pieces_count] of these pieces now."
                            show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
                    "No":
                        ethan "I'll leave them here."
                        hide screen puzzle_missing_pieces_zoomed
                        hide frame_overlay
                        hide ethan
                        show screen puzzle_missing_pieces("104", x=0.57, y=0.69, zoom_size=0.12, clickable=False) 
                        call set_puzzle_missing_pieces_clicked(False)
        
        pause

    hide back_btn
    hide screen puzzle_missing_pieces
    hide screen puzzle_missing_pieces_zoomed
    jump f1_p4

label puzzle_mini_game:
    scene bg puzzle_mini_game with fade

    if main_key1_acquired:
        "I already got the Main Key."
        jump f1_p1
        
    "The claw machine?"
    scene bg puzzle_room_3 with fade
    "It's the key..."
    "Main Key acquired."
    $ main_key1_acquired = True
    call screen objective_text(chap1_objective_go_main_room)
    show screen objective_text(chap1_objective_go_main_room, 0.98, 0.1)
 
    jump f1_p1

label main_room1:
    if not main_key1_acquired:
        $ from_locked_room = True
        "door locked sfx"
        if puzzle_evt_flag:
            if all_pieces_obtained:
                "It's locked. But, I have all the pieces now. Solving the puzzle might give me a clue."
            else:
                "It's locked. Maybe I should solve the puzzle first."
        else:
            "It's locked. I have to find the key."
        window hide
        jump f1_p2

    if not future_travel_done:
        scene bg darkroom with fade
        ethan "A bunch of alcohol, corporate attire, and… a coffin?"
        ethan "This is creepy."
        ethan "Wait… is that the key card for the elevator?"
        show screen f1_keycard
        while not keycard_clicked:
            "Take the Key Card"

        ethan "Wha-What's happening? I-I feel... "
        hide screen f1_keycard
        hide screen objective_text
        jump future_travel
        
    else: # future_travel is done
        if key_card1_acquired:
            scene bg darkroom with fade
            "I already have the Key Card for the elevator. I better get out of here."
            jump f1_p2
    
        scene bg darkroom with Fade(1.0, 1.0, 1.0, color="#fff")
        ethan "Haaa... haaa..."
        ethan "Thi-this is the room before."
        ethan "I'm... back?"
        ethan "Haa.. haa…"
        ethan "Wh-what just happened to me?"
        ethan "That was.. the worst."
        ethan "Was that... really my future?"
        ethan "No, no… I don't want that…"
        ethan "I... I-I have to get out of this place."
        
        "Key Card Acquired"
        $ key_card1_acquired = True
        call screen objective_text(chap1_objective_go_elevator)
        show screen objective_text(chap1_objective_go_elevator, 0.98, 0.1)

        show screen back_btn
        call set_back_btn_clicked(False)

        while not back_btn_clicked:
            pause

        jump f1_p2

label future_travel:
    scene black with Fade(1.0, 1.0, 1.0, color="#fff")

    "Time Travel Future"
    "DRINKING ALCOHOL"
    "NECKTIE STRANGLE"
    "COFFIN FUNERAL"
    "END"

    $ future_travel_done = True

    jump main_room1