label rooftop:
    scene black with fade
    ethan "is this... a rooftop?"
    ethan "What's that?"
    ethan "...A door? Out here?"
    ethan "This... must be the end."

    "You reached out for the door and slowly opened it."

    "car horn sfx, crash sfx"
    "hospital beep beep sfx"
    "silence"

    jump epilogue

label epilogue:
    scene black with Fade(1.0, 1.0, 1.0, color="#fff")
    show screen chapter_title_text("Epilogue")
    pause 3.0
    hide screen chapter_title_text

    ethan "Wh-where am I?"
    ethan "What's this? A hospital?"
    ethan "Mo-mom?"
    
    mom "Eth-"

    "mom crying tears of joy"

    ethan "{i}My mom burst into tears. She quickly called Dad and Nathan, who cried at the sight of me waking up as well.{/i}"
    ethan "{i}Yeah, I remember now.{/i}" 
    ethan "{i}That night, while I was out, a speeding car hit me.{/i}"
    ethan "{i}Mom told me I'd been in a coma for a year.{/i}"
    ethan "{i}I'd heard stories of coma patients when they woke up—some say that they could hear the world around them while unconscious; others claim they lived on in another place, in another world...{/i}"
    ethan "{i}I guess what I experienced in that strange facility was exactly that.{/i}"

    ethan "{i}After waking up and recovering, I knew what I had to do.{/i}"
    ethan "{i}I talked with my family.{/i}"
    ethan "{i}I thanked them for everything they've done for me, even when I was too blind to see it after Noah died.{/i}"
    ethan "{i}I tried to make amends for the difficult days I'd caused them.{/i}"
    ethan "{i}I wanted to do the things for them… that I couldn't do for Noah.{/i}"

    ethan "{i}I talked with his family.{/i}"
    ethan "{i}I apologized for not even paying proper respects at Noah's funeral.{/i}"
    ethan "{i}They told me they never wanted anything like that to ever happen again — not to anyone.{/i}"
    ethan "{i}So, I explained everything. I told them about our friendship, and gave them the recording that Noah left for us.{/i}"

    scene black with fade
    ethan "Hey…"
    ethan "…I wanted to give this to you."
    ethan "It's the manga of our favorite show — signed by the author himself."
    ethan "One of my patients gave it to me as a gift. But I knew, right away, it belonged here. With you."
    ethan "Noah… I became a psychiatrist."
    ethan "I wanted to help people who were struggling the way you once were."
    ethan "I couldn't be there for you back then… but I can be here for others now."
    ethan "Back then, I thought life was empty."
    ethan "A cracked gift box, with nothing inside."
    ethan "I guess life really is a gift—not because it's perfect, but because it's fragile."
    ethan "My life with you was a gift—one that I will treasure forever."

    jump ending

label ending:
    scene black with Fade(1.0, 1.0, 1.0, color="#fff")
    show screen chapter_title_text("The End.")
    pause
    $ renpy.full_restart()