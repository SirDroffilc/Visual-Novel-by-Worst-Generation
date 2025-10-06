init python:
    
    renpy.music.register_channel(
        "sfxloop",                # channel name
        "music",                  # copy functionality of the music channel
        True                      # this makes it a 'file' channel, not just sound
    )
    # Set default volume for all main channels
    renpy.music.set_volume(0.8, channel="music")
    renpy.music.set_volume(1.5, channel="sound")
    renpy.music.set_volume(1.2, channel="sfxloop")
    renpy.music.set_volume(0.8, channel="voice")
    renpy.music.set_volume(0.8, channel="movie")

    placed = {
        "piece_1": False,
        "piece_2": False,
        "piece_3": False,
        "piece_4": False,
        "piece_5": False,
        "piece_6": False,
        "piece_7": False,
        "piece_8": False,
        "piece_9": False
    }

    def set_placed_false():
        for piece in placed:
            placed[piece] = False

    correct_slots = {
        "piece_1": "1",
        "piece_2": "2",
        "piece_3": "3",
        "piece_4": "A",
        "piece_5": "B",
        "piece_6": "C",
        "piece_7": "D",
        "piece_8": "E",
        "piece_9": "F"
    }

    # Callback when a piece is dropped
    def drag_placed(drags, drop):
        piece = drags[0].drag_name
        snap_x = drags[0].x
        snap_y = drags[0].y 
        is_correctly_placed = False

        if drop:
            spot = drop.drag_name
            if correct_slots.get(piece) == spot:
                snap_x = drop.x
                snap_y = drop.y 
                is_correctly_placed = True

        drags[0].snap(snap_x, snap_y)

        placed[piece] = is_correctly_placed

        if is_correctly_placed:
            drags[0].draggable = False

        if all(placed.values()):
            return "win"

        return

#  <===== Chapter 1 Functions =====

label set_puzzle_missing_pieces_clicked(state):
    $ puzzle_missing_pieces_clicked = state
    return

label set_back_btn_clicked(state):
    $ back_btn_clicked = state
    return    

label set_main_key_clicked(state):
    $ main_key_clicked = state
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
