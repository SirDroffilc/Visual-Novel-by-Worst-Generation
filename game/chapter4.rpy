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

    show hospital_1 with fade
    ethan "Wh-where am I?"
    hide hospital_1
    show hospital_2
    ethan "What's this? A hospital?"
    hide hospital_2
    show hospital_3 with fade
    ethan "Mo-mom?"
    hide hospital_3
    show hospital_4
    mom "Eth-"
    hide hospital_4
    show hospital_5
    "mom cries tears of joy"
    "My mom burst into tears. She quickly called Dad and Nathan, who cried at the sight of me waking up as well."
    hide hospital_5

    scene black with fade
    "Yeah, I remember now." 
    "That night, while I was out, a speeding car hit me."
    "Mom told me I'd been in a coma for a year."
    "I'd heard stories of coma patients when they woke up. Some say that they could hear the world around them while unconscious. Others claim they lived on in another place, in another world..."
    "I guess what I experienced in that strange facility was exactly that."

    show woke_up with fade
    "After waking up and recovering, I knew what I had to do."
    hide woke_up
    show fam_talk with fade
    "I talked with my family."
    "I thanked them for everything they've done for me, even when I was too blind to see it after Noah died."
    "I tried to make amends for the difficult days I'd caused them."
    "I wanted to do the things for them… that I couldn't do for Noah."
    hide fam_talk

    show noah_fam
    "I talked with Noah's family."
    "I apologized for not even paying proper respects at his funeral."
    "They told me they never wanted anything like that to ever happen again — not to anyone."
    hide noah_fam
    show noah_fam_2
    "So, I explained everything. I told them about our friendship, and gave them the recording that Noah left for us."
    hide noah_fam_2

    scene white with fade
    show screen after_some_time_text("AFTER SOME TIME...")
    pause 3.0
    hide screen yrs_later_text

    show grave_1
    "..."
    hide grave_1
    show grave_2
    "Hey…"
    show grave_2
    "…I wanted to give this to you."
    hide grave_2
    show grave_3
    "It's the manga of our favorite show, signed by the author himself."
    "One of my patients gave it to me as a gift. But I knew, right away, it belonged here. With you."
    "Noah… I became a psychiatrist."
    "I want to help people who were struggling the way you once were."
    "I couldn't be there for you back then… but I can be here for others now."
    "Back then, I thought life was empty."
    "A cracked gift box, with nothing inside."
    "I guess life really is a gift, not because it's perfect, but because it's fragile."
    "My life with you was a gift—one that I will treasure forever."
    hide grave_3
    jump ending

label ending:
    scene black with Fade(1.0, 1.0, 1.0, color="#fff")
    show screen chapter_title_text("The End.")
    pause
    $ renpy.full_restart()