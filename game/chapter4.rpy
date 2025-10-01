label rooftop:
    hide screen objective_text
    play music "audio/bgm_peaceful_ambient.ogg" fadein 2.0
    scene bg white with Fade(0.5, 1.0, 0.5, color="#dfdebb")
    "Am I... on a rooftop?"
    scene bg rooftop1 with Fade(0.5, 1.0, 0.5, color="#dfdebb")
    "What's that?"
    "...A door? Out here?"
    "This... must be the end."
    scene bg rooftop4 with fade
    "But... why is it just standing there, in the middle of the rooftop?"
    "Just... a single door."
    scene bg rooftop2 with fade
    "It feels wrong... like it's waiting for me."
    "Do I even want to know what's behind it?"
    "My chest feels heavy... My hands won't stop shaking."
    "Still... I've come this far."
    scene bg rooftop3 with fade
    "There's no turning back now."
    stop music fadeout 2.0
    play sound "audio/sfx_door_unlock.ogg"
    play sound "audio/sfx_accident.ogg"
    scene bg white with Fade(1.0, 0.5, 1.0, color="#fff")
    pause 2.0

    jump epilogue

label epilogue:
    scene hospital_1 with Fade(1.0, 0.5, 1.0, color="#fff")
    ethan "Wh-where am I?"
    scene hospital_2 with Dissolve(0.3)
    ethan "What's this? A hospital?"
    scene hospital_3 with Dissolve(0.3)
    ethan "Mo-mom?"
    scene hospital_4 with Dissolve(0.3)
    mom "Ethan-"
    scene hospital_5 with Dissolve(0.3)
    play music "audio/bgm_peaceful_ambient.ogg" fadein 2.0
    "My mom burst into tears. She quickly called Dad and Nathan, who cried at the sight of me waking up as well."

    scene black with fade
    "Yeah, I remember now." 
    "That night, while I was out, a speeding car hit me."
    "Mom told me I'd been in a coma for a year."
    "I'd heard stories of coma patients when they woke up..."
    "Some say that they could hear the world around them while unconscious."
    "Others claim they lived on in another place, in another world..."
    "I guess what I experienced in that strange facility was exactly that."

    scene woke_up with Fade(1.0, 1.0, 1.0)
    "After waking up and recovering, I knew what I had to do."
    scene fam_talk with fade
    "I talked with my family."
    "I thanked them for everything they've done for me, even when I was too blind to see it after Noah died."
    "I tried to make amends for the difficult days I'd caused them."
    "I wanted to do the things for them... that I couldn't do for Noah."

    scene noah_fam with fade
    "I talked with Noah's family."
    "I apologized for not even paying proper respects at his funeral."
    "They told me they never wanted anything like that to ever happen again-not to anyone."
    show noah_fam_2 with Dissolve(0.3)
    "So, I explained everything. I told them about our friendship, and gave them the recording that Noah left for us."
    stop music fadeout 5.0  
    scene black with fade
    show screen after_some_time_text("Months later...")
    pause
    hide screen after_some_time_text with dissolve
    scene grave_1 with fade
    pause
    scene grave_2 with Dissolve(0.5)
    pause
    "Hey..."
    "...I wanted to give this to you."
    scene grave_3 with Dissolve(0.3)
    pause
    "It's the manga of our favorite show, signed by the author himself."
    "One of my colleagues gave it to me as a gift. But I knew, right away, it belonged here. With you."
    "Noah... I'm studying to become a psychiatrist now."
    "I want to help people who were struggling the way you once were."
    "I couldn't be there for you back then... but I can be here for others now."
    "Back then, I thought life was empty."
    "A cracked gift box, with nothing inside."
    "I guess life really is a gift, not because it's perfect, but because it's fragile."
    "My life with you was a gift-one that I will treasure forever."
    jump ending

label ending:
    scene black with Fade(1.0, 1.0, 1.0)
    show screen chapter_title_text("The End.")
    pause
    $ renpy.full_restart()