label start:
    # This label should only be called when "Start Game" is clicked from main menu
    scene black with fade
    show screen warning_screen("Content Warning \n\nThis game contains themes of mental health issues,a dark setting, and jumpscares.\n\nPlayer discretion is advised.") with dissolve
    pause 3.0
    hide screen warning_screen with dissolve

    jump prologue
    
    return