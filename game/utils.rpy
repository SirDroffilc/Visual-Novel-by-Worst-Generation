init python:
    # Set default volume for all main channels
    renpy.music.set_volume(0.8, channel="music")
    renpy.music.set_volume(0.8, channel="sound")
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

    # Callback when a piece is dropped
    def drag_placed(drags, drop):
        if not drop:
            return

        piece = drags[0].drag_name
        spot = drop.drag_name

        # Example rule: match piece name to a spot
        # piece_2 → Left Circle, piece_3 → Right Circle, piece_4 → Middle Circle
        if piece == "piece_1" and spot == "1":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_2" and spot == "2":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_3" and spot == "3":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_4" and spot == "A":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_5" and spot == "B":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_6" and spot == "C":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_7" and spot == "D":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_8" and spot == "E":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_9" and spot == "F":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        else:
            # Wrong spot → send back where it was
            drags[0].snap(drags[0].x, drags[0].y)

        # Check win condition
        if all(placed.values()):
            return "win"


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
