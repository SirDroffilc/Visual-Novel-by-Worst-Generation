label chapter2:
    hide screen objective_text
    show screen chapter_title_text("Chapter 2 The Fool")
    pause 3.0
    hide screen chapter_title_text
    show screen chapter_label_screen(2) 

    ethan "Another floor..."
    ethan "That key card was just for one floor above? "
    ethan "...but I have to keep moving... even if every part of me wants to turn back."
    ethan "I swear, this place will make me go insane."

    "rummaging sfx loop"

    ethan "What's that noise?"
    ethan "It's coming from that room..."
    ethan "Is someone there?"
    ethan "They might be able to help me find the way out."
    "I reached out for the door knob, but..."
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
    ethan "It is. This whole facility {i}is{/i} creepy."
    ethan "...Come on. Lets go check the other rooms."

    jump f2_p1

label elevator2:
    scene black with fade
    if not key_card2_acquired:
        "Access Denied. F2 Key Card Required."
        ethan "I need the key card."
    elif not objective_go_elevator2:
        ethan "I need to find Noah first."
    else:
        hide screen objective_text
        "You ran towards the elevator, desperately trying to escape the scene..."
        ethan "Please... let me out... let me out..."
        hide screen chapter_label_screen
        jump chapter3

label f2_p1:
    if not from_locked_room:
        scene bg f2p1 with fade
    
    if objective_go_elevator2 and not from_locked_room:
        ethan "The elevator..."

    $ from_locked_room = False

    if not objective_find_main_key_shown:
        ethan "We need to get out of here, but there's no exit below. Someone wrote on the walls that the only way is up."
        ethan "For that, we need to access the elevator. If this plays out like it did for me earlier, we'll need a key card to use it."
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
    if not from_locked_room:
        scene bg f2p2 with fade
    
    if objective_go_elevator2 and not from_locked_room:
        ethan "Hurry..."
    
    $ from_locked_room = False
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p2_buttons
        pause
    jump f2_p1

label f2_p3:
    if not from_locked_room:
        scene bg f2p3 with fade
    
    if objective_go_elevator2 and not from_locked_room:
        ethan "Please... Let me get out of here..."
    $ from_locked_room = False
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p3_buttons
        pause
    jump f2_p2

label f2_p4:
    if not from_locked_room:
        scene bg f2p4 with fade

    if objective_go_elevator2 and not from_locked_room:
        ethan "No... Noah..."
    $ from_locked_room = False
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p4_buttons
        pause
    jump f2_p3

label f2_p5:
    if not from_locked_room:
        scene bg f2p5 with fade
    
    if objective_go_elevator2 and not from_locked_room:
        ethan "W-why is this happening to me?"
    $ from_locked_room = False
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p5_buttons
        pause
    jump f2_p4

label f2_p6:
    if not from_locked_room:
        scene bg f2p6 with fade
    
    if objective_go_elevator2 and not from_locked_room:
        ethan "Please let me out of here..."

    $ from_locked_room = False

    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p6_buttons
        pause
    jump f2_p5

label room201: # Music Room
    if objective_go_elevator2:
        ethan "I don't have time for this..."
        $ from_locked_room = True
        window hide
        jump f2_p1
    scene bg darkroom with fade

    if objective_find_noah:
        ethan "He's not here..."
        
    else:
        ethan "It's scary how accurate this room is to the real thing."
        noah "Yeah... even the guitars, drumset, and keyboard—this place is messing with us."

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    
    hide screen back_btn
    jump f2_p1

label room202: # Clasroom
    if objective_go_elevator2:
        ethan "I don't have time for this..."
        $ from_locked_room = True
        window hide
        jump f2_p3
    
    scene bg darkroom with fade

    if objective_find_noah or main_key2_acquired or ladder_acquired:
        if objective_find_noah:
            ethan "He's not here..."
        elif main_key2_acquired:
            ethan "Nothing much to do here. We already got the key."
        elif ladder_acquired:
            ethan "We already got the ladder. Let's go back to your room."
            noah "Yeah, that's definitely tall enough."
        call set_back_btn_clicked(False)
        show screen back_btn
        while not back_btn_clicked:
            pause
        hide screen back_btn
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
            noah "There! We can use that ladder."
            ethan "That's perfect. Let's take it back to my room."
            $ ladder_acquired = True
            hide screen ladder_active
            call screen objective_text(chap2_objective_go_dorm_room)
            show screen objective_text(chap2_objective_go_dorm_room, 0.98, 0.1)
        pause
        
    hide screen back_btn
    hide screen ladder_active
    hide screen ladder_inactive
    
    jump f2_p3

label room20X: # Locked Room
    "door locked sfx"
    if objective_go_elevator2:
        ethan "I don't have time for this..."
    else:
        ethan "It's locked. I wonder what's inside..."
    $ from_locked_room = True
    window hide
    jump f2_p4

label room203: # Noah's Room
    if objective_go_elevator2:
        ethan "I don't have time for this..."
        $ from_locked_room = True
        window hide
        jump f2_p5

    if not (objective_find_noah and not noah_revelation_done):
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

    if objective_find_noah or main_key2_acquired or ladder_acquired:
        if objective_find_noah:
            jump noah_revelation

        elif main_key2_acquired:
            ethan "We already got the key. Let's go to the main room."
        
        elif ladder_acquired:
            call room203_cutscene
    
    else:  
        noah "We need to find something taller than a chair or a desk."

    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen back_btn
        pause
    
    hide screen back_btn
    jump f2_p5

label room203_cutscene:
    hide screen objective_text
    "GETTING THE MAIN KEY USING THE LADDER CUTSCENE"

    noah "Got it! Let's move on."
    ethan "Ye... yeah, let's go."
    call screen objective_text(chap2_objective_go_main_room)
    show screen objective_text(chap2_objective_go_main_room, 0.98, 0.1)
    $ main_key2_acquired = True
    return

label noah_revelation:
    hide screen objective_text
    scene black with fade
    ethan "Noah? Are you there?"
    "(cutscene)"
    "(door opening sfx)"
    "(background Best Friend hanged on the ceiling, dead)"
    "(horror shock sfx)"
    "(voice acting NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO"
    "(end cutscene)"

    ethan "I… I knew it."
    ethan "I knew this place wasn't kind enough to just let me relive our high school memories."
    ethan "The moment I saw him on this floor… I knew."
    "(quick flashback to \"Noah? But you…\" line)"
    ethan "I knew I wasn't allowed to be happy. Not after everything I've done."
    ethan "Noah... took his life a year ago."
    ethan "He never told me the full story—only that things at home were falling apart."
    ethan "His parents were fighting. The house itself felt like it was crumbling."
    ethan "And he was stuck in the middle."

    ethan "He left their house… and started staying in a dormitory. "
    ethan "He stopped going to school…"
    ethan "I thought it was just another rough patch… something he'd laugh off the next day."
    ethan "...But he didn't."
    ethan "After a week, I tried to visit him at his place..."
    ethan "...then I saw... {b}this{/b}."

    ethan "I should've noticed."
    ethan "The way he forced his smile."
    ethan "The way his eyes always looked tired, even when he swore he was fine."
    ethan "I should've asked. I should've stayed. I should've done something."
    ethan "...But I didn't."
    ethan "I was too busy. Too wrapped up in my own world. Too blind to see he was drowning."
    ethan "And now—he's gone."

    "(lines with voice acting), angry at self"
    ethan "He needed me, and I WASN'T THERE!"
    ethan "DON'T TELL ME IT WASN'T MY FAULT—"
    ethan "BECAUSE IT IS!"
    ethan "DON'T TELL ME THERE WAS NOTHING I COULD'VE DONE—"
    ethan "BECAUSE THERE WAS!"
    ethan "I WAS THE CLOSEST PERSON TO HIM!"
    ethan "I SHOULD'VE SAVED HIM!"
    ethan "I'M THE ONE TO BLAME!"
    "(pause, anger breaking down into grief)"
    ethan "I... I didn't even go to his funeral..."
    ethan "...couldn't even talk to his family."
    ethan "I had no right."
    ethan "I... I didn't do anything for him."

    $ noah_revelation_done = True
    call screen objective_text(chap2_objective_go_elevator)
    show screen objective_text(chap2_objective_go_elevator, 0.98, 0.1)
    $ objective_go_elevator2 = True
    jump f2_p5

label main_room2:
    if objective_go_elevator2:
        ethan "I don't have time for this..."
        $ from_locked_room = True
        window hide
        jump f2_p6
    if not main_key2_acquired:
        "door locked sfx"
        $ from_locked_room = True
        noah "You're right—it's locked."
        ethan "Yeah, this is the main room. There's one just like this before."
        ethan "We need the key."
        window hide
        jump f2_p6

    if not past_travel_done:
        hide screen objective_text
        scene black with fade
        "door unlocking sfx"
        ethan "I'll go first."
        "I slowly entered the main room..."
        "SLAM!"
        "The door crashed shut behind me, echoing through the room."
        scene bg f2p6 with fade
        noah "Ethan! Are you good?"
        ethan "Yeah, I'm fine!"
        ethan "...but the door's stuck."
        noah "That's fine. Can you see the key card?"
        ethan "Yeah, it's here!"
        noah "Just grab the card. I'll find a way to open the door."

        scene bg darkroom with fade
        ethan "I see it… the key card."
        ethan "But… am I really going to go through that nightmare again?"
        ethan "I-I'm scared. But if we ever want to get out of here…"

        show screen f2_keycard
        call set_keycard_clicked(False)
        while not keycard_clicked:
            "Take the Key Card"
        
        hide screen f2_keycard
        hide screen objective_text
        jump past_travel

    else: # past travel done
        if not objective_find_noah:
            scene bg darkroom with Fade(1.0, 1.0, 1.0, color="#fff")
            ethan "I-I'm... back?"  
            ethan "That's it? It's over?"  
            ethan "Hah... maybe it wasn't as bad as I thought."
            ethan "I got the key card for the elevator."
            "Key Card Acquired."
            $ key_card2_acquired = True
            ethan "I need to find Noah. He's probably worried sick."  
            "My eyes fall on the door—left wide open."
            ethan "Wait... the door's wide open."  
            ethan "Did he manage to unlock it while I was out?"  
            ethan "But... where did he go?"  

            call screen objective_text(chap2_objective_find_noah)
            show screen objective_text(chap2_objective_find_noah, 0.98, 0.1)
            $ objective_find_noah = True

        else:
            scene bg darkroom with fade
            ethan "I need to find Noah."

        jump f2_p6

label past_travel:
    ethan "P-please... don't make me see {i}that{/i} again—"

    scene black with Fade(1.0, 1.0, 1.0, color="#fff")
    
    "TIME TRAVEL PAST"
    "BONDING WITH NOAH"
    "BLA BLA BLA"

    $ past_travel_done = True
    jump main_room2