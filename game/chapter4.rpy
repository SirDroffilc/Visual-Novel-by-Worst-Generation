label epilogue:
    show screen chapter_title_text("Epilogue")
    pause 3.0
    hide screen chapter_title_text
    jump ending

label ending:
    scene black with fade
    "The End."
    $ renpy.full_restart()