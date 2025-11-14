from random import choice

capital = "Topeka"

bird = "Western Meadowlark"
flower = "Sunflower"

song = "Home on the range"

def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas city",
         "A considerable portion of kansas city is actually in Missouri",
         "Most kansans are annoyed by Wizard of Oz references to people outside of kansas"
    ]


    index = choice("0123")
    print(funfacts[int(index)])

