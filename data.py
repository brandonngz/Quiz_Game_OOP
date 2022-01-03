from prettytable import PrettyTable
table = PrettyTable()


table.field_names = ["Number", "Category"]
table.add_rows(
    [
        [1, "Science: Computers"],
        [2, "Video Games"]
    ]
)
table.align = 'l'

question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The logo for Snapchat is a Bell.", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Ada Lovelace is often considered the first computer programmer.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                                       "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Windows 7 operating system has six main editions.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                                       "question": "The Windows ME operating system was released in the year 2000.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Linux was first created as an alternative to Windows XP.", "correct_answer": "False",
     "incorrect_answers": ["True"]}
]
question_games = [
    {
        "category": "Entertainment: Video Games",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The name of the main character of the video game &quot;The Legend of Zelda&quot;, is Zelda.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "The song &quot;Megalovania&quot; by Toby Fox made its third appearence in the 2015 RPG &quot;Undertale&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
     "question": "The Ace Attorney trilogy was suppose to end with &quot;Phoenix Wright: Ace Attorney &minus; Trials and Tribulations&quot; as its final game.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "&quot;Half-Life 2&quot; runs on the Source Engine.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "Pac-Man was invented by the designer Toru Iwatani while he was eating pizza.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "The PlayStation was originally a joint project between Sega and Sony that was a Sega Genesis with a disc drive.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "The 2005 video game &quot;Call of Duty 2: Big Red One&quot; is not available on PC.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
     "question": "The names of Roxas&#039;s Keyblades in Kingdom Hearts are &quot;Oathkeeper&quot; and &quot;Oblivion&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In Pok&eacute;mon, Arbok evolves into Seviper.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
     "question": "The ADAM collecters in the Bioshock series are known as Little Sisters.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "&quot;Sonic the Hedgehog 2&quot; originally was going to have a time travel system.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In Until Dawn, both characters Sam and Mike cannot be killed under any means until the final chapter of the game.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In the video game &quot;Splatoon&quot;, the playable characters were originally going to be rabbits instead of squids.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
     "question": "Minecraft wasn&rsquo;t the original name to Minecraft.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In &quot;Space Station 13&quot;,  the station has a clown aboard it.", "correct_answer": "True",
     "incorrect_answers": ["False"]}
]

choose_category = {
    1: question_data,
    2: question_games,
}
