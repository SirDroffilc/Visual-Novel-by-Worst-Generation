label rooftop:
    hide screen objective_text
    scene black with fade
    ethan "Am I... on a rooftop?"
    ethan "What's that?"
    ethan "...A door? Out here?"
    ethan "This... must be the end."

    "I slowly walked towards the door and carefully opened it."
    scene white with Fade(1.0, 1.0, 1.0, color="#fff")

    "car horn sfx, crash sfx"
    "hospital beep beep sfx"
    "silence"

    jump epilogue

label epilogue:
    
    show screen chapter_title_text("Epilogue")
    pause 3.0
    hide screen chapter_title_text

    ethan "Wh-where am I?"
    ethan "What's this? A hospital?"
    ethan "Mo-mom?"
    
    mom "Eth-"

    "mom crying tears of joy"

    "My mom burst into tears. She quickly called Dad and Nathan, who cried at the sight of me waking up as well."
    "Yeah, I remember now." 
    "That night, while I was out, a speeding car hit me."
    "Mom told me I'd been in a coma for a year."
    "I'd heard stories of coma patients when they woke up—some say that they could hear the world around them while unconscious; others claim they lived on in another place, in another world..."
    "I guess what I experienced in that strange facility was exactly that."

    "After waking up and recovering, I knew what I had to do."
    "I talked with my family."
    "I thanked them for everything they've done for me, even when I was too blind to see it after Noah died."
    "I tried to make amends for the difficult days I'd caused them."
    "I wanted to do the things for them… that I couldn't do for Noah."

    "I talked with his family."
    "I apologized for not even paying proper respects at Noah's funeral."
    "They told me they never wanted anything like that to ever happen again — not to anyone."
    "So, I explained everything. I told them about our friendship, and gave them the recording that Noah left for us."

    scene black with fade
    "Hey…"
    "…I wanted to give this to you."
    "It's the manga of our favorite show — signed by the author himself."
    "One of my patients gave it to me as a gift. But I knew, right away, it belonged here. With you."
    "Noah… I became a psychiatrist."
    "I wanted to help people who were struggling the way you once were."
    "I couldn't be there for you back then… but I can be here for others now."
    "Back then, I thought life was empty."
    "A cracked gift box, with nothing inside."
    "I guess life really is a gift—not because it's perfect, but because it's fragile."
    "My life with you was a gift—one that I will treasure forever."

    jump ending

label ending:
    scene black with Fade(1.0, 1.0, 1.0, color="#fff")
    show screen chapter_title_text("The End.")
    pause
    $ renpy.full_restart()