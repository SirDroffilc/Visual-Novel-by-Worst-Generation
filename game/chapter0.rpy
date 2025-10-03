label splashscreen:
    scene black
    show text "A Visual Novel by" with dissolve
    pause 1.0
    hide text with dissolve
    show screen splash_screen
    pause 8.0  # duration of your video
    with fade
    hide screen splash_screen
    return

label prologue:
    scene black 
    
    play sfxloop "audio/sfx_heart_monitor.ogg" volume 0.05
    pause 0.5
    play sound "audio/voice_prologue1.ogg"
    "People talk about life as if it's a gift." 
    play sound "audio/voice_prologue2.ogg"
    "They wrap it in ribbons of meaning, tie it up with words like purpose, love, and hope."
    stop sfxloop
    play sound "audio/voice_prologue3.ogg"
    "But I can't help but see the cracks in the wrapping..."
    play sound "audio/voice_prologue4.ogg"
    "...the emptiness hiding beneath."
    play sfxloop "audio/sfx_heart_monitor_beep.ogg" volume 0.2 noloop
    pause 2.0
    scene bg room101_2 with fade
    stop sfxloop fadeout 2.0
    play music "audio/bgm_dark_quiet.ogg" fadein 2.0
    pause
    
    "…Wh-where the hell am I?"
    scene bg room101_1 with fade
    show ethan confused at right_medium with dissolve
    "This… isn't my room..."
    show ethan default with Dissolve(0.1)
    "It's empty... just a bed and a table of mess."
    show ethan smacked with Dissolve(0.1)
    "How did I get here?"
    "I can't remember..."
    show ethan default with Dissolve(0.1)
    "I better find the way out."
    
    scene black with fade
    $ renpy.movie_cutscene("videos/look_to_onlyway.webm")
    scene bg c0_onlyway
    "“The only way... is up?”"
    "This place looks like some sort of facility..."
    
    scene black
    $ renpy.movie_cutscene("videos/onlyway_to_elevator.webm")
    scene bg elevator
    "An elevator... is this working?"
    play sound "audio/sfx_elevator_locked.ogg"
    "{i}Elevator Screen: Access Denied. F1 Key Card Required.{/i}"
    "I need to find this key card."
    
    scene black
    $ renpy.movie_cutscene("videos/elevator_to_mainroom.webm")
    scene bg c0_mainroom
    "This room looks important…"
    play sound "audio/sfx_door_locked.ogg"
    pause
    "It's locked. What should I do? I need to get out of this place."
    
    jump chapter1
