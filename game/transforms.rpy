transform chapter_fade:
    alpha 0.0 # start invisible
    linear 1.0 alpha 1.0   # fade in
    pause 1.0
    linear 1.0 alpha 0.0   # fade out

transform left_small:
    xalign -0.05
    yalign 1.0
    zoom 0.7

transform right_medium:
    xalign 1.0
    yalign 1.0
    zoom 0.8

transform sprite_slide_from_left:
    xalign -0.5
    yalign 1.0
    zoom 0.7
    linear 0.1 xalign -0.05

transform frame_slide_from_left:
    xalign -1.0
    yalign -0.4
    zoom 1.3
    linear 0.1 xalign -0.7

transform exit_left_fast:
    linear 1.0 xalign -1.5   # slide off left in 0.1s

image frame_overlay = "sprite_frame/small_frame.png"