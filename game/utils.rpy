init python:
    # Set default volume for all main channels
    renpy.music.set_volume(0.7, channel="music")
    renpy.music.set_volume(0.7, channel="sound")
    renpy.music.set_volume(0.7, channel="voice")
    renpy.music.set_volume(0.7, channel="movie")


#  <===== Chapter 1 Functions =====

label set_puzzle_pieces_clicked(state):
    $ puzzle_pieces_clicked = state
    return

label set_back_btn_clicked(state):
    $ back_btn_clicked = state
    return    

label set_keycard_clicked(state):
    $ keycard_clicked = state
    return

# ===== Chapter 1 Functions =====>


#  <===== Chapter 2 Functions =====

label set_ladder_clicked(state):
    $ ladder_clicked = state
    return

# ===== Chapter 2 Functions =====>
