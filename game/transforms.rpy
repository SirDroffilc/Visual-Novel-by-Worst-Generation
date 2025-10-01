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

image hallway_overlay = "sprite_frame/hallway_overlay.png"
image room101_overlay = "sprite_frame/room101_overlay.png"
image room102_overlay = "sprite_frame/room102_overlay.png"
image room103_overlay = "sprite_frame/room103_overlay.png"
image room104_overlay = "sprite_frame/room104_overlay.png"

image room201_overlay = "sprite_frame/room201_overlay.png"
image room202_overlay = "sprite_frame/room202_overlay.png"
image room203_overlay = "sprite_frame/room203_overlay.png"

image room301_overlay = "sprite_frame/room301_overlay.png"
image room302_overlay = "sprite_frame/room302_overlay.png"
image room303_overlay = "sprite_frame/room303_overlay.png"

image mainroom1_overlay = "sprite_frame/mainroom1_overlay.png"
image mainroom2_overlay = "sprite_frame/mainroom2_overlay.png"
image mainroom3_overlay = "sprite_frame/mainroom3_overlay.png"



