label chapter3:
    hide screen objective_text
    show screen chapter_title_text("Chapter 3: Turning Point")
    pause 3.0
    hide screen chapter_title_text

    "go straight toward main room animation"
    "banging sfx"
    ethan "Please... open! OPEN!"
    ethan "Come on, come on... why won't you open?!"
    ethan "FUCK!"
    ethan "Haaa... haaa..."
    ethan "Calm down... it's no good. I'll have to find the key again."

    jump f3_p1

label elevator3:
    scene bg darkroom with fade

    "elevator 3"
    jump f3_p1

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
    scene bg f3p2 with fade

    while True:
        show screen f3_p2_buttons
        pause
        
label room301: # Storage Room
    scene bg darkroom with fade

    ethan "Ugh, dust everywhere... just boxes stacked on top of each other."
    ethan "Nothing useful… maybe I should check the other rooms."

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    hide screen_back_btn
    jump f3_p1

label room302: # Living Room
    scene bg darkroom with fade
    ethan "This looks... familiar, like someone actually lived here."
    ethan "A sofa... a TV that doesn't work anymore... broken remote on the floor."
    ethan "...but no key."

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    hide screen_back_btn
    jump f3_p1

label room303: # Game Room
    scene bg darkroom with fade
    "GAME ROOM"

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    hide screen_back_btn
    jump f3_p2

label main_room3:
    scene bg darkroom with fade

    "MAIN ROOM"
    jump f3_p2