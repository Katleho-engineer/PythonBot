import random




def error_response():
    random_list = [
        "Please try writing something more descriptive. Or type help to see suggestions.",
        "Oh! It appears you wrote something I don't understand yet. Type help to see what I can help you with.",
        "Do you mind trying to rephrase that? Or type help to see suggestions.",
        "I'm terribly sorry, I didn't quite catch that. Or type help to see I can do",
        "I can't answer that yet, please try asking something else. Or type help to get suggestions"
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]


def help_me():
    suggestions = """
    I am a WordBot. I can give you the following information about words:
        - Definition
        - Antonym
        - Synonym
        - Syllables
        - Part of 
        - Pronunciation
        - Use in a sentence
        - everything 

    Here are the type of request to make:
        ~ define ambient
        ~ Antonym of success
        ~ Synonym of life
        ~ Syllables of complicated
        ~ Part of wheel
        ~ pronunciation pf bombastic
        ~ Use careful in a sentence
        ~ Give me everything about lemon
     """
    return suggestions


print(help_me())