label chapter3:
    stop music fadeout 2.0
    hide screen objective_text
    scene black with fade
    
    show screen chapter_title_text("Chapter 3 Turning Point")
    pause 3.0
    hide screen chapter_title_text
    show screen chapter_label_screen(3) 
    
    $ renpy.movie_cutscene("videos/run_to_mainroom.webm")
    scene bg mainroom3_close
    play music "audio/bgm_horror_atmosphere.ogg"
    play sfxloop "audio/sfx_door_banging.ogg"
    "Please... open! {size=+10}OPEN!{/size}"
    "Come on, come on... why won't you open?!"
    stop sfxloop
    scene bg mainroom3_close with vpunch
    play sound "audio/sfx_door_slam.ogg"
    "{size=+30}FUCK!{/size}"
    "Haaa... haaa..."
    "Calm down... it's no good. I'll have to find the key again."

    jump f3_p1

label elevator3:
    scene bg elevator with fade

    if not key_card3_acquired:
        play sound "audio/sfx_elevator_locked.ogg"
        "{i}Access Denied. F2 Key Card Required.{/i}"
        ethan "Figures."
        jump f3_p1

    else:
        play sound "audio/sfx_elevator_unlock.ogg"
        ethan "What's next?"
        hide screen objective_text
        hide screen chapter_label_screen
        jump rooftop

label f3_p1:
    scene bg f3p1 with fade

    if not objective_find_main_key3_flag:
        call screen objective_text(chap3_objective_find_main_key)
        show screen objective_text(chap3_objective_find_main_key, 0.93, 0.07)
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
    scene bg room301 with fade

    if not key_card3_acquired:
        "Ugh, dust everywhere... just boxes stacked on top of each other."
        if not main_key3_acquired:
            "Nothing useful... maybe I should check the other rooms."
    else:
        "I should get out of here."

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    hide screen_back_btn
    jump f3_p1

label room302: # Living Room
    scene bg room302 with fade
    if not key_card3_acquired:
        "This looks... familiar, like someone actually lived here."
        "A sofa... a TV that doesn't work anymore... broken remote on the floor."
        if not main_key3_acquired:
            "...but no key."
    else:
        "I should get out of here."

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    hide screen_back_btn
    jump f3_p1

label room303: # Game Room
    scene bg room303 with fade

    if not key_card3_acquired:
        if not guessing_game_won:
            if not tried_guessing:
                "An arcade machine?"
                "I'm tired of this..."
            else:
                "Let's try this again..."
            jump guessing_mini_game
        elif not main_key3_acquired:
            "What are all these games for?"
            "What's this place?"
            "Please... let me out..."
            play sound "audio/sfx_object_dropped.ogg"
            pause
            show screen main_key(filepath="keys/key3.png", x=0.2, y=0.4, zoom_size=1.0, clickable=False) with dissolve
            "...the key."
            show screen main_key(filepath="keys/key3.png", x=0.2, y=0.4, zoom_size=1.0, clickable=True)
            call set_main_key_clicked(False)
            while not main_key_clicked:
                "{i}Take the Main Key.{/i}"
            "{i}Main Key Acquired.{/i}"
            $ main_key3_acquired = True

            call screen objective_text(chap3_objective_go_main_room, 0.5, 0.4)
            show screen objective_text(chap3_objective_go_main_room, 0.93, 0.07)
            
        else:
            "I already got the key from this stupid machine."
        
    else:
        "I should get out of here."
    
    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    hide screen_back_btn
    jump f3_p2

label guessing_mini_game:
    hide screen objective_text
    scene bg guessing with fade
    play music "audio/retro_bgm.ogg"
    if not tried_guessing:
        ethan "\"Guessing Game\"?"
    else:
        ethan "I'm gettin' it right this time..."
    scene bg guessing_instructions
    pause
    if not tried_guessing:
        ethan "Five tries..."
        scene bg guessing_instructions with vpunch
        ethan "WHY DO I HAVE TO DO THIS?!"
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
            play sound "audio/bgm_slamdunk_op_cut.ogg" volume 0.4 fadein 1.0

        show screen mini_game_clue(clue_number)

        $ answer = ""
        while not isinstance(answer, str) or answer.strip() == "":
            $ answer = renpy.input("Answer: ")
            if not isinstance(answer, str):
                $ answer = ""   # Force back to empty so it loops again

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
        pause
        show room303_overlay at frame_slide_from_left
        show ethan scared at sprite_slide_from_left
        ethan "That..."
        ethan "That... was our..."
        show ethan terrified with vpunch
        ethan "DON'T FUCK WITH ME!"
        show ethan terrified with vpunch
        ethan "WHO'S BEHIND THIS?!"
        show ethan terrified with vpunch
        ethan "WHY ARE YOU DOING THIS?!"
        show ethan crying_heavy with Dissolve(0.2)
        ethan "...I"
        ethan "...I-I just want to get out of here."
        play music "audio/bgm_ambient_horror.ogg"
        hide ethan with Dissolve(0.5)
        hide room303_overlay with Dissolve(0.5)
        $ guessing_game_won = True
    else:
        "..."
        play sound "audio/retro_lose.ogg"
        scene bg guessing_lost
        pause
        ethan "What's the answer?"
        ethan "Are there any more clues?"
        ethan "Maybe in the other rooms..."
        show screen objective_text(chap3_objective_find_main_key, 0.93, 0.07)
        jump f3_p2

    stop sound
    play sound "audio/retro_game_over.ogg"
    scene bg guessing_gameover
    pause
    jump room303

label main_room3:
    if not main_key3_acquired:
        $ from_locked_room = True
        play sound "audio/sfx_door_locked.ogg"
        ethan "It's locked. I better search the other rooms for the key."
        jump f3_p2
    
    if not present_travel_done:
        play sound "audio/sfx_door_unlock.ogg"
        scene black with fade
        pause 0.5
        scene bg mainroom3 with fade
        show screen keycard(filepath="keys/keycard3.png", x=0.5, y=0.4, zoom_size=0.05, clickable=False)
        call set_keycard_clicked(False)
        pause
        "A hospital bed..."
        "What is this place really for?"
        "The key card..."
        "Please... don't be another nightmare."
        show screen keycard(filepath="keys/keycard3.png", x=0.5, y=0.4, zoom_size=0.05, clickable=True)
        while not keycard_clicked:
            "{i}Take the Key Card{/i}"
        
        hide screen keycard
        hide screen objective_text
        jump present_travel

    elif not key_card3_acquired:
        scene bg mainroom3 with Fade(0.5, 1.0, 0.5, color="#fff")
        ethan "...back again, but this time feels..."
        ethan "...different."
        ethan "I know what I need to do now."

        $ key_card3_acquired = True
        "{i}Key Card Acquired{/i}"
        call screen objective_text(chap3_objective_go_elevator)
        show screen objective_text(chap3_objective_go_elevator, 0.93, 0.07)

    else:
        scene bg mainroom3 with fade
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