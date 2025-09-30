label chapter2:
    hide screen objective_text
    scene black with fade
    show screen chapter_title_text("Chapter 2 The Fool")
    pause 3.0
    hide screen chapter_title_text
    show screen chapter_label_screen(2) 
    
    scene bg f2p1 with fade
    stop music fadeout 1.0
    "Another floor..."
    "That key card was just for one floor above? "
    "...but I have to keep moving... even if every part of me wants to turn back."
    "I swear, this place will make me go insane."

    play sound "audio/sfx_rummaging.ogg"

    "What's that noise?"
    "It's coming from that room..."
    "Is someone there?"
    "They might be able to help me find the way out."
    "I reached out for the door knob, but..."
    "Wait... what if they're... dangerous?"
    "I have to be careful."
    stop sound
    "It stopped..."
    play music "audio/sfx_heartbeat.ogg"
    "Did they hear me?"
    play sound "audio/sfx_door_unlock.ogg"
    pause 1.0

    stop music
    stop sound
    scene bg room201_1 with fade
    show noah shocked with vpunch
    pause
    noah "ETHAN?!"
    show noah shocked at right:
        linear 0.1 xalign 0.9
    
    show frame_overlay at frame_slide_from_left
    show ethan scared at sprite_slide_from_left
    ethan "No... Noah? But you..."
    show noah laughing with Dissolve(0.1)
    
    noah "Dude! It's been forever!"
    noah "What's it been-like a year? Two?"
    show noah big_smile with Dissolve(0.1)
    noah "Man, I can't tell you how good it feels to see a familiar face in a place like this!"
    show ethan confused with Dissolve(0.1)
    ethan "Ye… Yeah."
    show noah smile with Dissolve(0.1)
    noah "What's up? You look pale."
    ethan "N-no, it's nothing. Its just… this place is… insane."
    ethan "How did you even get here?"
    noah "I honestly have no clue. I just woke up in this room. "
    noah "The last thing I remember… I was in bed, trying to sleep. My parents were fighting again-screaming at each other. Couldn't shut it out."
    show ethan default with Dissolve(0.1)
    ethan "I guess were in the same boat. I woke up one floor below this one."
    ethan "The last thing I remember is that I was going out to grab some food. Then… I saw a bright light and suddenly… I was here."
    show noah depressed with Dissolve(0.1)
    noah "...So what, you think we got kidnapped or something?"
    ethan "I don't know. But whatever this place is-it's crazy. We have to get out of here as soon as possible."
    
    hide noah with Dissolve(0.1)
    show ethan confused with Dissolve(0.1)
    ethan "...Hey, this room…"
    ethan "Don't you think it looks like Genesis? You know, the old studio we used to practice at?"
    
    show noah shocked at right with Dissolve(0.1):
        xalign 0.9
    noah "...Whoa. Now that you mention it-Yeah. Damn, dude, it really does."
    noah "This feels nostalgic, but creepy as hell at the same time."
    show ethan default with Dissolve(0.1)
    ethan "It is. This whole facility {i}is{/i} creepy."
    ethan "...Come on. Lets go check the other rooms."

    hide noah with Dissolve(0.1)
    hide ethan with Dissolve(0.1)
    hide frame_overlay with Dissolve(0.1)
    jump f2_p1

label elevator2:
    scene bg elevator with fade
    if not key_card2_acquired:
        play sound "audio/sfx_elevator_locked.ogg"
        "{i}Access Denied. F2 Key Card Required.{/i}"
        ethan "I need the key card."
    elif not objective_go_elevator2:
        ethan "I need to find Noah first."
    else:
        hide screen objective_text
        "You ran towards the elevator, desperately trying to escape the scene..."
        play sound "audio/sfx_elevator_unlock.ogg"
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
        show frame_overlay at frame_slide_from_left
        show ethan default at sprite_slide_from_left
        
        ethan "We need to get out of here, but there's no exit below. Someone wrote on the walls that the only way is up."
        ethan "For that, we need to access the elevator. If this plays out like it did for me earlier, we'll need a key card to use it."
        ethan "But before that, we need to find the key to the main room or something. I'm guessing that's where the key card is."
        show noah big_smile_thumbs_up at right with Dissolve(0.1):
            xalign 0.9
        noah "Gotcha."

        hide noah with Dissolve(0.1)
        hide ethan with Dissolve(0.1)
        hide frame_overlay with Dissolve(0.1)
        play music "audio/bgm_dark_quiet.ogg" fadein 1.0
        call screen objective_text(chap2_objective_find_main_key)
        show screen objective_text(chap2_objective_find_main_key, 0.93, 0.07)
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
    if not ladder_acquired:
        scene bg room201_1 with fade
    else:
        scene bg room201_3 with fade

    if objective_find_noah:
        ethan "He's not here..."
    
    elif main_key2_acquired:
        ethan "Nothing much to do here. We already got the key."
    
    elif ladder_acquired:
        ethan "We already got the ladder. Let's go back to your room."
        noah "Yeah, that's definitely tall enough."

    elif not find_tall_evt_flag:
        ethan "It's scary how accurate this room is to the real thing."
        noah "Yeah... even the guitars, drumset, and keyboard-this place is messing with us."
    
    else:
        ethan "Something tall..."
        call set_ladder_clicked(False)
        call set_back_btn_clicked(False)
        show screen back_btn
        show screen ladder_layer
        while not back_btn_clicked:
            if ladder_clicked and find_tall_evt_flag and not ladder_acquired: 
                show noah big_smile at right with Dissolve(0.2):
                    xalign 0.9
                noah "There! We can use that ladder."
                show frame_overlay at frame_slide_from_left
                show ethan confused at sprite_slide_from_left
                ethan "That ladder..."
                show noah default with Dissolve(0.1)
                noah "What's up?"
                ethan "Nothing..."
                show noah big_smile_thumbs_up with Dissolve(0.1)
                noah "Let's go get that key!"
                ethan "Yeah..."
                hide noah with Dissolve(0.1)
                hide ethan with Dissolve(0.1)
                hide frame_overlay with Dissolve(0.1)
                $ ladder_acquired = True
                hide screen ladder_layer
                scene bg room201_3
                call screen objective_text(chap2_objective_go_dorm_room)
                show screen objective_text(chap2_objective_go_dorm_room, 0.93, 0.07)
            pause
        hide screen back_btn
        hide screen ladder_layer
        jump f2_p1
            
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

    scene bg room202 with fade

    if objective_find_noah:
        "He's not here..."
    
    elif main_key2_acquired:
        "Nothing much to do here. We already got the key."
    
    elif ladder_acquired:
        "We should go get the key."

    elif find_tall_evt_flag:
        "These school chairs won't help us much. We need something taller."
    
    else:
        ethan "…This time, it's our old classroom. Back in high school."
        ethan "There's no way this is a coincidence. This place… it's like it's digging into our memories on purpose."
        ethan "It {i}wants{i} to mess with us."

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    
    hide screen back_btn
    jump f2_p3

label room20X: # Locked Room
    play sound "audio/sfx_door_locked.ogg"
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
        scene bg room203_1 with fade

    if not find_tall_evt_flag:
        show noah shocked at right with vpunch:
            xalign 0.9
        noah "Dude! This is…"
        show frame_overlay at frame_slide_from_left
        show ethan confused at sprite_slide_from_left
        ethan "Your dorm room."
        noah "No way… This is insane. Why does this place look exactly like my dorm? Down to the mess on the desk, even?"
        ethan "I told you-this place is crazy. Logic doesn't belong here."
        show ethan default with Dissolve(0.1)
        ethan "...I've only been in your dorm once, but it stuck with me so much that I still remember exactly what it looks like. "

        show noah smile with Dissolve(0.1)
        noah "Wait… look up. Hey, is that the key you were talking about?"
        noah "It's just hanging over there on the ceiling."
        ethan "Yeah, I think that's it."
        show ethan confused with Dissolve(0.1)
        ethan "Tch, too high though. We need something tall to stand on."
        noah "This desk won't do it for sure, even the chair. We need something taller."
        noah "Hmm... there's nothing useful here. Let's check the other rooms. There's gotta be something." 

        hide noah with Dissolve(0.1)
        hide ethan with Dissolve(0.1)
        hide frame_overlay with Dissolve(0.1)
        call screen objective_text(chap2_objective_find_tall)
        show screen objective_text(chap2_objective_find_tall, 0.93, 0.07)
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
    scene bg room203_2 with fade
    ethan "Can you reach it?"
    noah "Yeah, leave it to me!"
    scene bg ladder_scene1 with fade
    pause
    scene bg ladder_scene2 with fade
    noah "Aahh..."
    noah "Aahh... yes!"
    noah "Got it! Let's move on."
    ethan "Ye... yeah, let's go."
    scene bg room203_3 with fade 
    call screen objective_text(chap2_objective_go_main_room)
    show screen objective_text(chap2_objective_go_main_room, 0.93, 0.07)
    $ main_key2_acquired = True
    return

label noah_revelation:
    hide screen objective_text
    stop music
    scene black with fade
    ethan "Noah? Are you there?"
    play sound "audio/sfx_door_unlock.ogg"
    pause 2.0
    play sound "audio/sfx_horror_sting.ogg"
    pause 0.3
    scene bg room203_4 with vpunch
    pause
    
    "(voice acting NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO"

    play music "audio/bgm_sad_horror.ogg"
    "I… I knew it."
    "I knew this place wasn't kind enough to just let me relive our high school memories."
    "The moment I saw him on this floor… I knew."
    "I knew I wasn't allowed to be happy. Not after everything I've done."
    "Noah... took his life a year ago."
    "He never told me the full story-only that things at home were falling apart."
    "His parents were fighting. The house itself felt like it was crumbling."
    "And he was stuck in the middle."

    "He left their house… and started staying in a dormitory. "
    "He stopped going to school…"
    "I thought it was just another rough patch… something he'd laugh off the next day."
    "...But he didn't."
    "After a week, I tried to visit him at his place..."
    "...then I saw... {b}this{/b}."

    "I should've noticed."
    "The way he forced his smile."
    "The way his eyes always looked tired, even when he swore he was fine."
    "I should've asked. I should've stayed. I should've done something."
    "...But I didn't."
    "I was too busy. Too wrapped up in my own world. Too blind to see he was drowning."
    "And now-he's gone."

    "He needed me, and I WASN'T THERE!"
    "DON'T TELL ME IT WASN'T MY FAULT-"
    "BECAUSE IT IS!"
    "DON'T TELL ME THERE WAS NOTHING I COULD'VE DONE-"
    "BECAUSE THERE WAS!"
    "I WAS THE CLOSEST PERSON TO HIM!"
    "I SHOULD'VE SAVED HIM!"
    "I'M THE ONE TO BLAME!"
    stop music fadeout 8.0
    ""
    "I... I didn't even go to his funeral..."
    "...couldn't even talk to his family."
    "I had no right."
    "I... I didn't do anything for him."

    play music "audio/bgm_ambient_horror.ogg" fadein 2.0

    $ noah_revelation_done = True
    call screen objective_text(chap2_objective_go_elevator)
    show screen objective_text(chap2_objective_go_elevator, 0.93, 0.07)
    $ objective_go_elevator2 = True
    jump f2_p5

label main_room2:
    if objective_go_elevator2:
        ethan "I don't have time for this..."
        $ from_locked_room = True
        window hide
        jump f2_p6
    if not main_key2_acquired:
        play sound "audio/sfx_door_locked.ogg"
        $ from_locked_room = True
        noah "You're right-it's locked."
        ethan "Yeah, this is the main room. There's one just like this before."
        ethan "We need the key."
        window hide
        jump f2_p6

    if not past_travel_done:
        hide screen objective_text
        stop music fadeout 2.0
        scene black with fade
        play sound "audio/sfx_door_unlock.ogg"
        ethan "I'll go first."
        stop sound
        "I slowly entered the main room..."
        play sound "audio/sfx_door_slam.ogg"
        "SLAM!"
        "The door crashed shut behind me, echoing through the room."
        stop sound
        scene bg f2p6 with fade
        show noah scared at left with Dissolve(0.1)
        noah "Ethan! Are you good?"
        ethan "{i}Yeah, I'm fine!{/i}"
        ethan "{i}...but the door's stuck.{/i}"
        noah "That's fine. Can you see the key card?"
        ethan "{i}Yeah, it's here!{/i}"
        noah "Just grab the card. I'll find a way to open the door."
        hide noah with Dissolve(0.1)

        scene bg mainroom2 with fade
        show screen keycard(filepath="keys/keycard2.png", x=0.5, y=0.5, zoom_size=0.1, clickable=False)
        play music "audio/bgm_ambient_horror.ogg"
        ethan "Everything's... upside down... but this table..."
        ethan "The key card."
        ethan "Am I really going to go through that nightmare again?"
        ethan "I-I'm scared. But if we ever want to get out of here…"
        call set_keycard_clicked(False)
        show screen keycard(filepath="keys/keycard2.png", x=0.5, y=0.5, zoom_size=0.1, clickable=True) 
        while not keycard_clicked:
            "{i}Take the Key Card{/i}"
        
        stop music fadeout 2.0
        hide screen keycard
        hide screen objective_text
        jump past_travel

    else: # past travel done
        if not objective_find_noah:
            scene bg mainroom2_1 with Fade(0.5, 1.0, 0.5, color="#fff")
            "I-I'm... back?"  
            "That's it? It's over?"  
            "Hah... maybe it wasn't as bad as I thought."
            "I got the key card for the elevator."
            "{i}Key Card Acquired.{/i}"
            $ key_card2_acquired = True
            "I need to find Noah. He's probably worried sick."  
            "My eyes fall on the door-left wide open."
            "Wait... the door's wide open."  
            "Did he manage to unlock it while I was out?"  
            "But... where did he go?"  

            play music "audio/bgm_ambient_horror.ogg"
            call screen objective_text(chap2_objective_find_noah, 0.5, 0.3)
            show screen objective_text(chap2_objective_find_noah, 0.93, 0.07)
            $ objective_find_noah = True

        else:
            scene bg darkroom with fade
            ethan "I need to find Noah."

        jump f2_p6

label past_travel:
    "P-please... don't make me see {i}that{/i} again..."
    play sound "audio/sfx_transition.ogg"
    scene bg white with Fade(0.5, 1.0, 0.5, color="#fff")
    "Ah, too bright..."
    play sfxloop "audio/sfx_running.ogg" loop
    scene bg run with Fade(0.5, 1.0, 0.5, color="#fff")
    "Where am I?"
    scene bg ethan_running2 with Dissolve(0.5)
    ethan "Am I outside?"

    scene bg ethannoah_running with Dissolve(0.5)
    noah "DUDE, STOP DAYDREAMING! WE'RE RUNNING LATE"
    ethan "What?!"
    scene bg ethannoah_running2 with Dissolve(0.5)
    ethan "Noah, I thought you couldn't enter the room... Thank God you're here!"
    noah "Uhh, room? What are you talking about? Dude, are you still asleep?"
   
    scene bg run with Dissolve(0.2)
    $ renpy.music.set_volume(0.2, delay=0.0, channel='sfxloop')
    play sound "audio/sfx_slap.ogg"
    show ethan run2_unif at left with hpunch
    "{size=+10}*SMACK!*{/size}"
    ethan "Ouch!"
    "{i}A dull thud of pain spread across my back...{/i}"
    show noah laughing_unif at right with Dissolve(0.2)
    noah "HAHAHA! Did that wake you up?"
    ethan "..."
    show ethan default_unif at left with Dissolve(0.1)
    $ renpy.music.set_volume(0.05, delay=0.0, channel='sfxloop')
    "{i}Wait...{/i}"
    "{i}No, he's not the one I was just with in the facility.{/i}"
    "{i}...{/i}"
    "{i}...I got transported to another time again...{/i}"
    "{i}I guess... he's the Noah of this time.{/i}"
    "{i}I'm back in our high school days.{/i}"

    $ renpy.music.set_volume(0.4, delay=0.0, channel='sfxloop')
    show noah run1_unif at right with Dissolve(0.1)
    noah "JUST FIVE MORE MINUTES! DUDE, HURRY UP!"

    stop sfxloop fadeout 2.0
    jump classroom

label classroom:
    play music "audio/bgm_country_music.ogg"
    scene bg classroom2 with fade
    pause 2.0
    scene bg classroom1 with fade
    show ethan observing_unif at center with dissolve
    show ethan observing_unif at left with move
    ethan "We just attended the lecture for the first period. Nothing strange has happened yet." 
    show ethan default_unif with Dissolve(0.1)
    show noah bored_unif at right with Dissolve(0.1)
    noah "Ughh, that was boring. Why do we gotta learn about a bunch of dead guys?"
    noah "They're not coming back anyway..."
    show ethan talking_unif with Dissolve(0.1)
    ethan "Maybe, but it's still important."
    show noah talking_unif with Dissolve(0.1)
    ethan "The world is messed up-or not messed up-because of what they all did back then."
    noah "Yeah, but it's boring right?"
    show noah leftlook_unif with Dissolve(0.1)
    ethan "..."
    ethan "Yeah, it is."
    show ethan laughing_unif with Dissolve(0.1)
    show noah laughing_unif with Dissolve(0.1)
    ethan "HAHAHA."

    hide ethan with Dissolve(0.1)
    hide noah with Dissolve(0.1)
    scene black with fade
    jump music_clubroom

label music_clubroom:
    scene bg after_school with fade
    "After class, we just lazed around and went to a music studio near our school." 
    stop music fadeout 3.0
    $ renpy.music.set_volume(0.5, delay=0.0, channel='sfxloop')
    play sfxloop "audio/bgm_slamdunk_op_cut.ogg" fadein 2.0
    scene bg music_studio with fade 
    "The place has great equipment and it was cheap-perfect for our broke selves."
    "I play the guitar. Noah's our vocalist."
    "We absolutely loved to play the opening song of our favorite show."
    "It's a sports anime that we watch on TV. We always talk about how hilarious that show is."
    "Noah goes absolutely crazy at the mic singing its theme song."
    stop sfxloop fadeout 3.0
    
    play music "audio/bgm_country_music.ogg" fadein 3.0
    
    scene bg play_arc2 with fade
    "After that, we went to the arcade..."
    "This guy really sucks at video games, and often rages when he loses."
    "But, yeah... he's really fun to play with."
    $ renpy.music.set_volume(0.8, delay=0.0, channel='sfxloop')
    scene bg house with fade
    "Then, we went to his house to play this murder mystery visual novel about a group of extraordinary high school kids killing each other."
    scene bg play with Dissolve(0.5)
    noah "Whaaaat???"
    scene bg house with Dissolve(0.5)
    show vn_closeup at center with Dissolve(0.4)
    "I really liked this VN series"
    hide vn_closeup with Dissolve(0.5)
    
    "This was our usual routine."
    "Go to school, hang out with our band, ..."
    "...play at the arcade or at the basketball court, then play some more at his house."
    scene black with fade
    "I missed this" 
    stop music fadeout 3.0
    show ethan default_unif at center with dissolve
    pause
    show ethan dismayed2_unif with Dissolve(0.1)
    pause
    "But..."
    show ethan dismayed_unif with Dissolve(0.1)
    pause
    show ethan closeup_unif with Dissolve(0.1)
    "Am I allowed to have this much fun?"
    pause
    $ past_travel_done = True
    play sound "audio/sfx_transition.ogg"
    jump main_room2