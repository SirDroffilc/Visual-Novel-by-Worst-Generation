init python:
    # Set default volume for all main channels
    renpy.music.set_volume(0.7, channel="music")
    renpy.music.set_volume(0.7, channel="sound")
    renpy.music.set_volume(0.7, channel="voice")
    renpy.music.set_volume(0.7, channel="movie")

#  <===== Chapter 1 Functions =====

label set_puzzle_missing_pieces_clicked(state):
    $ puzzle_missing_pieces_clicked = state
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


#  <===== Chapter 3 Functions =====

label set_start_btn_clicked(state):
    $ start_btn_clicked = state
    return

label check_answer(answer_input):
    python:
        if not isinstance(answer_input, str):
            answer_input = "" 
        answer_input = answer_input.lower().strip()
        if answer_input == "slam dunk":
            answer_correct = True
        else:
            answer_correct = False
    
    return

screen mini_game_clue(num):
    imagebutton:
        xalign 0.5
        yalign 0.5

        idle Transform(f"clues/clue_{num}.png", zoom=0.7)
    
# ===== Chapter 3 Functions =====>
