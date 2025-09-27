label chapter1:
    scene black with fade

    show screen chapter_title_text("Chapter 1: Shadows Ahead")
    pause 3.0
    hide screen chapter_title_text

    call screen objective_text(chap0_objective_find_clues)
    show screen objective_text(chap0_objective_find_clues, 0.98, 0.1)

    jump f1_p1

label elevator1:
    scene black with fade
    if not key_card1_acquired:
        "Access Denied. F1 Key Card Required."
        ethan "I need the Key Card."
    
    else:
        "Elevator door opening..."
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
    scene bg darkroom with fade
    pause

    show ethan default at left with dissolve
    ethan "This is where I woke up."
    ethan "Nothing's here—just a bed and a table with a bunch of random junk on top of it."
    hide ethan with dissolve
    window hide

    while not back_btn_clicked:
        show screen back_btn
        if not room101_pieces_taken:
            show screen puzzle_missing_pieces("101")

            if puzzle_missing_pieces_clicked: # piece-2, 4, 9
                hide screen puzzle_missing_pieces
                show screen puzzle_missing_pieces_zoomed("101")
                if puzzle_evt_flag:
                    ethan "Found the pieces."

                elif pieces_count <= 0:
                    ethan "Are these puzzle pieces?"

                else:
                    ethan "Again? What are these pieces for?"

                menu: 
                    "Take the pieces?"
                    "Yes":
                        ethan "I'll take them."
                        $ pieces_count += 3
                        $ room101_pieces_taken = True
    
                        if puzzle_evt_flag:
                            ethan "I got [pieces_count] of these pieces now."
                            show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
                    "No":
                        ethan "I'll leave them here."
                        hide screen puzzle_missing_pieces_zoomed

        pause
    
    hide back_btn
    hide screen puzzle_missing_pieces
    hide screen puzzle_missing_pieces_zoomed
    
    jump f1_p1

label room102: # Puzzle Room
    if all_pieces_obtained:
        jump puzzle_mini_game

    scene bg darkroom with fade
    pause

    if puzzle_evt_flag:
        show ethan default at left with dissolve
        ethan "I have to look for the puzzle pieces."
        ethan "...the other rooms, maybe?"
    
    else:
        show ethan default at left with dissolve
        ethan "This place is packed."
        ethan "...it's like someone dumped an entire storage unit in here."
        ethan "Where do I even start looking?"
        show ethan confused
        ethan "Wait... something's written on the wall."
        ethan "\"Assemble the pieces\"?"
        hide ethan with dissolve
        call screen objective_text(chap1_objective_puzzle_evt)
        show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
        $ puzzle_evt_flag = True

        show ethan confused at left
        ethan "A jigsaw puzzle? Seriously?"
        show ethan smacked
        ethan "Ugh, but it's the only lead I've got."
        ethan "...fine."

        hide ethan with dissolve
    
    while not back_btn_clicked:
        show screen back_btn
        pause
    
    jump f1_p1

label room103: # Office Room
    scene bg darkroom with fade

    ethan "This room looks like an office… maybe for some kind of company."
    ethan "...It doesn't feel like anyone's worked here in years."
    
    while not back_btn_clicked:
        show screen back_btn
        if not room103_pieces_taken: 
            show screen puzzle_missing_pieces("103")

            if puzzle_missing_pieces_clicked: # piece 6, 8
                ethan "...Wait, what's that under the chair?"
                hide screen puzzle_missing_pieces
                show screen puzzle_missing_pieces_zoomed("103")
                if puzzle_evt_flag:
                    ethan "Found them."

                elif pieces_count <= 0:
                    ethan "Are these puzzle pieces?"

                else:
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

        pause
    
    hide back_btn
    hide screen puzzle_missing_pieces
    hide screen puzzle_missing_pieces_zoomed
    
    jump f1_p3

label room104: # Messy Room
    scene bg darkroom with fade

    ethan "Ugh, what's that smell?"
    ethan "It's like a mix of dust, dirty laundry, and… rotten food left out for weeks."
    ethan "This whole place feels like a garbage dump, not a bedroom."

    while not back_btn_clicked:
        show screen back_btn
        if not room104_pieces_taken:
            show screen puzzle_missing_pieces("104")

            if puzzle_missing_pieces_clicked: # piece-1, 3, 5, 7
                ethan "...Wait, is that—on the bed?"
                hide screen puzzle_missing_pieces
                show screen puzzle_missing_pieces_zoomed("104")

                if puzzle_evt_flag:
                    ethan "Oh, the pieces! There they are."

                elif pieces_count <= 0:
                    ethan "Are these puzzle pieces?"

                else:
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
        
        pause

    hide back_btn
    hide screen puzzle_missing_pieces
    hide screen puzzle_missing_pieces_zoomed
    jump f1_p4

label puzzle_mini_game:
    scene bg darkroom with fade

    if main_key1_acquired:
        ethan "I already got the Main Key."
        jump f1_p1

    "PUZZLE MINI GAME"
    "DRAG DRAG DROP"

    "Main Key acquired."
    
    call screen objective_text(chap1_objective_go_main_room)
    $ main_key1_acquired = True
    show screen objective_text(chap1_objective_go_main_room, 0.98, 0.1)
 
    jump f1_p1

label main_room1:
    if not main_key1_acquired:
        $ from_locked_room = True
        "door locked sfx"
        if puzzle_evt_flag:
            if all_pieces_obtained:
                ethan "It's locked. But, I have all the pieces now. Solving the puzzle might give me a clue."
            else:
                ethan "It's locked. Maybe I should solve the puzzle first."
        else:
            ethan "It's locked. I have to find the key."
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