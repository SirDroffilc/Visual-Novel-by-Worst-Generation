label chapter1:
    scene bg hallway with fade

    show screen chapter_title_text("Chapter 1: Shadows Ahead")

    pause 3.0

    hide screen chapter_title_text
    
    show haru default at left with dissolve
    haru "The key must be in one of these rooms."
    hide haru with dissolve

    while True:
        if pieces_count == 9 and not all_pieces_obtained:
            $ all_pieces_obtained = True
            call screen objective_text(chap1_objective_go_puzzle_room)
            show screen objective_text(chap1_objective_go_puzzle_room, 0.98, 0.1)
            
        show screen hallway1_buttons
    
        pause

    jump chapter2

label room101:
    scene bg darkroom with fade
    haru "This is where I woke up."
    haru "Nothing's here—just a bed and a table with a bunch of random junk on top of it."

    if not room101_pieces_taken:
        if puzzle_evt_flag:
            haru "Found the pieces."

        elif pieces_count <= 0:
            haru "Are these puzzle pieces?"

        else:
            haru "Again? What are these pieces for?"

        menu: 
            "Take the pieces?"
            "Yes":
                haru "I'll take them."
                $ pieces_count += 3
                $ room101_pieces_taken = True
                if puzzle_evt_flag:
                    haru "I got [pieces_count] of these pieces now."
                    show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
            "No":
                haru "I'll leave them here."

    scene bg hallway with fade

    return

label room102:
    if all_pieces_obtained:
        jump puzzle_mini_game
    scene bg darkroom with fade
    show haru default at left with dissolve
    haru "This place is packed."
    haru "...it's like someone dumped an entire storage unit in here."
    haru "Where do I even start looking?"
    haru "Wait... something's written on the wall."
    haru "\"Assemble the pieces\"?"

    call screen objective_text(chap1_objective_puzzle_evt)
    $ puzzle_evt_flag = True

    show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)

    show haru angry
    haru "A jigsaw puzzle? Seriously?"
    show haru default
    haru "Ugh, but it's the only lead I've got."
    haru "...fine."

    scene bg hallway with fade
    return

label room103:
    scene bg darkroom with fade

    haru "This room looks like an office… maybe for some kind of company."
    haru "...It doesn't feel like anyone's worked here in years."
    
    if not room103_pieces_taken:
        haru "...Wait, what's that under the chair?"

        if puzzle_evt_flag:
            haru "Found them."

        elif pieces_count <= 0:
            haru "Are these puzzle pieces?"

        else:
            haru "Another set of pieces? What are these for?"

        menu: 
            "Take the pieces?"
            "Yes":
                haru "Yeah, I better take these pieces."
                $ pieces_count += 2
                $ room103_pieces_taken = True
                if puzzle_evt_flag:
                    haru "I got [pieces_count] of them now."
                    show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
            "No":
                haru "I'll leave them here."
    
    scene bg hallway with fade    
    return

label room104:
    scene bg darkroom with fade

    haru "Ugh, what's that smell?"
    haru "It's like a mix of dust, dirty laundry, and… rotten food left out for weeks."
    haru "This whole place feels like a garbage dump, not a bedroom."

    if not room104_pieces_taken:
        haru "...Wait, is that—on the bed?"

        if puzzle_evt_flag:
            haru "Oh, there they are. Figures."

        elif pieces_count <= 0:
            haru "Are these puzzle pieces?"

        else:
            haru "What's with all these puzzle pieces?"

        menu: 
            "Take the pieces?"
            "Yes":
                haru "I'll take them."
                $ pieces_count += 4
                $ room104_pieces_taken = True
                if puzzle_evt_flag:
                    haru "I got [pieces_count] of these pieces now."
                    show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
            "No":
                haru "I'll leave them here."

    
    scene bg hallway with fade
    return

label puzzle_mini_game:
    scene bg darkroom with fade

    "PUZZLE MINI GAME"
    "DRAG DRAG DROP"

    scene bg hallway with fade

    return

label mainrm1:
    scene bg darkroom with fade
    "Main Room 1"
    scene bg hallway with fade
    return