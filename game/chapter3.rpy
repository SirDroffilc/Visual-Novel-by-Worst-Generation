label chapter3:
    hide screen objective_text
    
    show screen chapter_title_text("Chapter 3: Turning Point")
    pause 3.0
    hide screen chapter_title_text
    show screen chapter_label_screen(3) 
    
    "go straight toward main room animation"
    "banging sfx"
    ethan "Please... open! {size=+10}OPEN!{/size}"
    ethan "Come on, come on... why won't you open?!"
    ethan "{size=+20}FUCK!{/size}"
    ethan "Haaa... haaa..."
    ethan "Calm down... it's no good. I'll have to find the key again."

    jump f3_p1

label elevator3:
    scene bg darkroom with fade

    if not key_card3_acquired:
        "Access Denied. 3F Key Card Required."
        ethan "Figures."
        jump f3_p1

    else:
        ethan "What's next?"
        hide screen chapter_label_screen
        jump rooftop

label f3_p1:
    scene bg f3p1 with fade

    if not objective_find_main_key3_flag:
        call screen objective_text(chap3_objective_find_main_key)
        show screen objective_text(chap3_objective_find_main_key, 0.98, 0.1)
        $ objective_find_main_key3_flag = True

    while True:
        show screen f3_p1_buttons
        pause

label f3_p2:
    if not from_locked_room:
        scene bg f3p2 with fade
    $ from_locked_room = False
    while True:
        show screen f3_p2_buttons
        pause
        
label room301: # Storage Room
    scene bg darkroom with fade

    if not key_card3_acquired:
        ethan "Ugh, dust everywhere... just boxes stacked on top of each other."
        if not main_key3_acquired:
            ethan "Nothing useful... maybe I should check the other rooms."
    else:
        ethan "I should get out of here."

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    hide screen_back_btn
    jump f3_p1

label room302: # Living Room
    scene bg darkroom with fade
    if not key_card3_acquired:
        ethan "This looks... familiar, like someone actually lived here."
        ethan "A sofa... a TV that doesn't work anymore... broken remote on the floor."
        if not main_key3_acquired:
            ethan "...but no key."
    else:
        ethan "I should get out of here."

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    hide screen_back_btn
    jump f3_p1

label room303: # Game Room
    scene bg darkroom with fade

    if not key_card3_acquired:
        if not guessing_game_won:
            if not tried_guessing:
                ethan "This... is the arcade we used to go to."
                ethan "...stop showing me these places..."
                ethan "Haaa.. haa... breathe..."
                ethan "I need to move forward..."
            else:
                ethan "Let's try this again..."
            "one arcade machine turns on"
            jump guessing_mini_game
        elif not main_key3_acquired:
            "key dropping from the arcade machine"
            ethan "...the key."
            ethan "What are all these games for?"
            "Main Key Acquired."
            $ main_key3_acquired = True

            call screen objective_text(chap3_objective_go_main_room)
            show screen objective_text(chap3_objective_go_main_room, 0.98, 0.1)
            
        else:
            ethan "I already got the key from this stupid machine."
        
    else:
        ethan "I should get out of here."
    
    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    hide screen_back_btn
    jump f3_p2

label guessing_mini_game:
    scene bg guessing with fade
    play music "audio/retro_bgm.ogg"
    if not tried_guessing:
        ethan "What's this?"
        ethan "\"Guessing Game\"?"
    else:
        ethan "I'm gettin' it right this time..."
    scene bg guessing_instructions
    pause
    if not tried_guessing:
        ethan "Five tries..."
        ethan "...fine."
    call set_start_btn_clicked(False)

    while not start_btn_clicked:
        show screen mini_game_start_btn
        pause
    
    $ tried_guessing = True
    scene bg guessing
    hide screen mini_game_start_btn

    $ answer_correct = False
    $ clue_number = 1
    while not answer_correct and clue_number <= 5:
        if clue_number == 5:
            stop music
            play sound "audio/slamdunk_op_cut.ogg" volume 0.4
        show screen mini_game_clue(clue_number)
        $ answer = ""
        while answer == "":
            $ answer = renpy.input("Answer: ")
        
        call check_answer(answer)
        if not answer_correct:
            "{size=+20}WRONG{/size}"
        if clue_number == 5:
            stop sound
        $ clue_number += 1
    
    stop music
    hide screen mini_game_clue
    if answer_correct:
        "..."
        play sound "audio/retro_win.ogg"
        scene bg guessing_won
        ethan "That..."
        ethan "That... was Noah's..."
        ethan "DON'T FUCK WITH ME!"
        ethan "WHO'S BEHIND THIS?!"
        ethan "WHY ARE YOU DOING THIS?!"
        ethan "...I"
        ethan "...I-I just want to get out of here."
        $ guessing_game_won = True
    else:
        "..."
        play sound "audio/retro_lose.ogg"
        scene bg guessing_lost
        ethan "What's the answer?"
        ethan "Are there any more clues?"
        ethan "Maybe in the other rooms..."

    stop sound
    play sound "audio/retro_game_over.ogg"
    scene bg guessing_gameover
    pause
    jump room303

label main_room3:
    if not main_key3_acquired:
        $ from_locked_room = True
        "door locked sfx"
        ethan "It's locked. I better search the other rooms for the key."
        jump f3_p2
    
    

    if not present_travel_done:
        scene bg darkroom with fade
        call set_keycard_clicked(False)
        ethan "Please... don't be another nightmare."

        while not keycard_clicked:
            show screen f3_keycard
            pause
        
        hide screen f3_keycard
        jump present_travel

    elif not key_card3_acquired:
        scene bg darkroom with Fade(1.0, 1.0, 1.0, color="#fff")
        ethan "...back again, but this time feels..."
        ethan "...different."
        ethan "I know what I need to do now."

        call set_keycard_clicked(False)
        while not keycard_clicked:
            show screen f3_keycard
            pause
        
        hide screen f3_keycard
        $ key_card3_acquired = True
        "Key Card Acquired"
        call screen objective_text(chap3_objective_go_elevator)
        show screen objective_text(chap3_objective_go_elevator, 0.98, 0.1)

    else:
        scene bg darkroom with fade
        ethan "I have the key card. I should hurry to the elevator."

    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen back_btn
        pause
    
    jump f3_p2

label present_travel:
    hide screen objective_text
    scene black with Fade(1.0, 1.0, 1.0, color="#fff")
    
    "PRESENT TRAVEL"
    "GHOST MODE"
    "BLA BLA BLA"

    $ present_travel_done = True
    jump main_room3