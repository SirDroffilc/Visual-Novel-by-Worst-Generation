label chapter2:
    show screen chapter_title_text("Chapter 2: The Fool")
    pause 3.0
    hide screen chapter_title_text

    ethan "Another floor..."
    ethan "...but I have to keep moving... even if every part of me wants to turn back."
    ethan "I swear, this place will make me go insane."

    "rummaging sfx loop"

    ethan "What's that noise?"
    ethan "It's coming from that room..."
    ethan "Is someone there?"
    ethan "They might be able to help me find the way out."
    "You reached out for the door knob, but..."
    ethan "Wait... what if they're... dangerous?"
    ethan "I have to be careful."
    "stop rummaging sfx"
    ethan "It stopped..."
    ethan "Did they hear me?"
    "fast hearbeat sfx"
    "door opening sfx"

    scene bg darkroom with fade
    noah "ETHAN?!"
    ethan "No... Noah? But you..."
    noah "Dude! It's been forever!"
    noah "What's it been—like a year? Two?"
    noah "Man, I can't tell you how good it feels to see a familiar face in a place like this!"
    ethan "Ye… Yeah."
    noah "What's up? You look pale."
    ethan "N-no, it's nothing. Its just… this place is… insane."
    ethan "How did you even get here?"
    noah "I honestly have no clue. I just woke up in this room. "
    noah "The last thing I remember… I was in bed, trying to sleep. My parents were fighting again—screaming at each other. Couldn't shut it out."
    ethan "I guess were in the same boat. I woke up one floor below this one."
    ethan "The last thing I remember is that I was going out to grab some food. Then… I saw a bright light and suddenly… I was here."
    noah "...So what, you think we got kidnapped or something?"
    ethan "I don't know. But whatever this place is—it's crazy. We have to get out of here as soon as possible."
    
    ethan "...Hey, this room…"
    ethan "Don't you think it looks like Genesis? You know, the old studio we used to practice at?"
    noah "...Whoa. Now that you mention it—Yeah. Damn, dude, it really does."
    noah "This feels nostalgic, but creepy as hell at the same time."
    ethan "It is. This whole facility IS creepy."
    ethan "...Come on. Lets go check the other rooms."

    jump f2_p1

label f2_p1:
    scene bg f2p1 with fade

    if not objective_find_main_key_shown:
        ethan "If this plays out like it did for me earlier, we'll need a key card to use the elevator."
        ethan "But before that, we need to find the key to the main room or something. I'm guessing that's where the key card is."
        noah "Gotcha."
        call screen objective_text(chap2_objective_find_main_key)
        show screen objective_text(chap2_objective_find_main_key, 0.98, 0.1)
        $ objective_find_main_key_shown = True

    call set_back_btn_clicked(False)
    while True:
        show screen f2_p1_buttons
        pause

label f2_p2:
    scene bg f2p2 with fade
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p2_buttons
        pause
    jump f2_p1

label f2_p3:
    scene bg f2p3 with fade
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p3_buttons
        pause
    jump f2_p2

label f2_p4:
    scene bg f2p4 with fade
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p4_buttons
        pause
    jump f2_p3

label f2_p5:
    scene bg f2p5 with fade
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p5_buttons
        pause
    jump f2_p4

label room201:
    scene bg darkroom with fade

    ethan "It's scary how accurate this room is to the real thing."
    noah "Yeah... even the guitars, drumset, and keyboard—this place is messing with us."

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    
    hide screen back_btn
    jump f2_p1

label room202:
    scene bg darkroom with fade
    
    if ladder_acquired:
        ethan "We already got the ladder. Let's go back to your room."
        noah "Yeah, that's definitely tall enough."
        jump f2_p3
        
    if not find_tall_evt_flag:
        show screen ladder_inactive
        ethan "…This time, it's our old classroom. Back in high school."
        noah "There's no way this is a coincidence. This place… it's like it's digging into our memories on purpose."
        noah "It {i}wants{i} to mess with us."

    else:
        show screen ladder_active
        ethan "These school chairs won't help us much. We need something taller."

    call set_back_btn_clicked(False)
    call set_ladder_clicked(False)
    
    while not back_btn_clicked and not ladder_acquired:
        show screen back_btn
        if not ladder_acquired and ladder_clicked and find_tall_evt_flag:
            noah "Oh, there's a ladder."
            ethan "That's totally perfect. Let's take it back to my room."
            $ ladder_acquired = True
            call screen objective_text(chap2_objective_go_dorm_room)
            show screen objective_text(chap2_objective_go_dorm_room, 0.98, 0.1)
        pause
        
    hide screen back_btn
    hide screen ladder_active
    hide screen ladder_inactive
    
    jump f2_p3

label room20X:
    "door locked sfx"
    ethan "It's locked. I wonder what's inside..."
    noah "Let's just go."
    window hide
    return

label room203:
    scene bg darkroom with fade
    if not find_tall_evt_flag:
        noah "Dude! This is…"
        ethan "Your dorm room."
        noah "No way… This is insane. Why does this place look exactly like my dorm? Down to the mess on the desk, even?"
        ethan "I told you—this place is crazy. Logic doesn't belong here."
        ethan "...I've only been in your dorm once, but it stuck with me so much that I still remember exactly what it looks like. "

        noah "Wait… look up. Hey, is that the key you were talking about?"
        noah "It's just hanging over there on the ceiling."
        ethan "Yeah, I think that's it."
        ethan "Tch, too high though. We need something tall to stand on."

        noah "This desk won't do it for sure, even the chair. We need something taller."
        noah "Hmm... there's nothing useful here. Let's check the other rooms. There's gotta be something." 

        call screen objective_text(chap2_objective_find_tall)
        show screen objective_text(chap2_objective_find_tall, 0.98, 0.1)
        $ find_tall_evt_flag = True

    if ladder_acquired:
        jump room203_cutscene
        
    noah "We still need to find something taller than a chair or a desk."

    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen back_btn
        pause
    
    hide screen back_btn
    jump f2_p5

label room203_cutscene:
    "GETTING THE MAIN KEY USING THE LADDER CUTSCENE"
    jump f2_p5