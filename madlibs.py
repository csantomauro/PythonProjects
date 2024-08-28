director = "Bong Joon-Ho"

# print("The best director is " + director)
# print("The best director is {}".format(director))
# print(f"The best director is {director}")

choice = int(input("Please pick a number between 1 and 3"))

madlib = ""
print (choice)

if choice == 1:
    one = input("Adjective: ")
    two = input("Noun (plural):")
    three = input("Verb (past tense):")
    four = input("Adjective:")
    five = input("Noun:")
    six = input("Verb (present tense):")
    seven = input("Noun:")
    eight = input("Adjective:")
    nine = input("Verb (past tense):")
    ten = input("Adjective:")

    madlib = f"It was a {one} day at the beach. The sun was shining, and the {two} were sparkling in the water. \
    I {three} into the ocean and felt the {four} waves crash against me. I brought my {five} along, hoping to {six} it in \
    the sand. Suddenly, a {seven} floated by, and everyone around me started laughing. It was a {eight} sight, and I \
    couldn't believe my eyes! As the day came to an end, we {nine} our towels and headed home, feeling {ten} and happy."
elif choice == 2:
    one = input("Adjective: ")
    two = input("Noun:")
    three = input("Verb (past tense):")
    four = input("Adjective:")
    five = input("Noun:")
    six = input("Verb (present tense):")
    seven = input("Noun:")
    eight = input("Adverb:")
    nine = input("Verb:")
    ten = input("Adjective:")

    madlib = f"The old mansion on the hill was known to be {one}. No one dared to enter its creaky doors, except for one \
    brave {two} who {three} there one night. The air inside was {four}, and the only sound was the ticking of an old {five}. As the \
    brave soul {six} through the dark hallways, a shadowy {seven} appeared out of nowhere. {eight}, they tried to {nine}, but the doors \
      were locked. The mansion's mystery was never solved, and it remains a {ten} tale told to this day."
else:
    one = input("Noun: ")
    two = input("Adjective:")
    three = input("Verb (past tense):")
    four = input("Adjective:")
    five = input("Noun:")
    six = input("Verb:")
    seven = input("Adverb:")
    eight = input("Noun:")
    nine = input("Adjective:")
    ten = input("Verb (past tense):")

    madlib = f"In the lab, the mad scientist was working on their latest {one}. They combined a {two} chemical with some strange \
      {three} substances. The mixture turned a {four} color and began to bubble like a {five}! The scientist decided to {six} the \
      concoction, but things quickly got out of hand. {seven}, the mixture exploded, covering the entire lab in {eight}. The {nine} \
     result was nothing like what they expected, and the scientist {ten} away from the experiment, vowing to be more careful next time."

print (madlib)