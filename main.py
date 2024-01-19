import json
import re
import error
import api


# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("logic.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:

        answer = response_data[response_index]["bot_response"]

        if answer == 'placeholder':
            response_type = response_data[response_index]["response_type"]
            answer = placeholder(user_input, response_type)

        else:
            answer = response_data[response_index]["bot_response"]

        return answer

    return error.error_response()


# function finds the last word in a sentence
def lastWord(string):

    lis = list(string.split(" "))

    length = len(lis)

    return lis[length - 1]


# function finds the word that comes after use
def useWOrd(sentence):
    lis = list(sentence.split(" "))

    for i in range(len(lis)):
        if lis[i] == 'use':
            return lis[i + 1]


# function gives an appropriate response for any logic that has "placeholder" as a response.
def placeholder(question, response_type):

    if response_type == 'definition':
        confirm = 'no'
        answer = lastWord(question)

        while confirm != 'yes':

            confirm = input(f"Bot: Do you want the definition of '{answer}'? [yes/no]\nYou: ").lower()

            while (confirm != 'no') and (confirm != 'yes'):
                confirm = input(f"Bot: Please type yes or no. Do you want the definition of '{answer}'?\nYou: ")

            if confirm == 'yes':
                break

            else:
                question = input(f"Bot: Type a word that you want the definition of.\nYou: ").lower()
                answer = lastWord(question)

        define = api.wordAPI_define(answer)
        return define

    if response_type == 'partOF':
        confirm = 'no'
        answer = lastWord(question)

        while confirm != 'yes':

            confirm = input(f"Bot: Do you want to know what '{answer}' forms part of? [yes/no]\nYou: ").lower()

            while (confirm != 'no') and (confirm != 'yes'):
                confirm = input(f"Bot: Please type yes or no. Do you want to know what '{answer}' forms part of?\nYou: ")

            if confirm == 'yes':
                break

            else:
                question = input(f"Bot: Type a word that you want. \nYou: ").lower()
                answer = lastWord(question)

        part_of = api.wordAPI_partOf(answer)
        return part_of

    if response_type == 'antonym':
        confirm = 'no'
        answer = lastWord(question)

        while confirm != 'yes':

            confirm = input(f"Bot: Do you want to know the antonym of '{answer}'? [yes/no]\nYou: ").lower()

            while (confirm != 'no') and (confirm != 'yes'):
                confirm = input(f"Bot: Please type yes or no. Do you want to know the antonym of '{answer}'?\nYou: ")

            if confirm == 'yes':
                break

            else:
                question = input(f"Bot: Type a word that you want the antonym of. \nYou: ").lower()
                answer = lastWord(question)

        antonym = api.wordAPI_antonyms(answer)
        return antonym

    if response_type == 'synonyms':
        confirm = 'no'
        answer = lastWord(question)

        while confirm != 'yes':

            confirm = input(f"Bot: Do you want to know the synonyms of '{answer}'? [yes/no]\nYou: ").lower()

            while (confirm != 'no') and (confirm != 'yes'):
                confirm = input(f"Bot: Please type yes or no. Do you want to know the synonyms of '{answer}'?\nYou: ")

            if confirm == 'yes':
                break

            else:
                question = input(f"Bot: Type a word that you want the synonyms of. \nYou: ").lower()
                answer = lastWord(question)

        synonyms = api.wordAPI_synonyms(answer)
        return synonyms

    if response_type == 'syllables':
        confirm = 'no'
        answer = lastWord(question)

        while confirm != 'yes':

            confirm = input(f"Bot: Do you want to know the syllables of '{answer}'? [yes/no]\nYou: ").lower()

            while (confirm != 'no') and (confirm != 'yes'):
                confirm = input(f"Bot: Please type yes or no. Do you want to know the syllables of '{answer}'?\nYou: ")

            if confirm == 'yes':
                break

            else:
                question = input(f"Bot: Type a word that you want the syllables of. \nYou: ").lower()
                answer = lastWord(question)

        syllables = api.wordAPI_syllables(answer)
        return syllables

    if response_type == 'pronunciation':
        confirm = 'no'
        answer = lastWord(question)

        while confirm != 'yes':

            confirm = input(f"Bot: Do you want to know the pronunciation of '{answer}'? [yes/no]\nYou: ").lower()

            while (confirm != 'no') and (confirm != 'yes'):
                confirm = input(f"Bot: Please type yes or no. Do you want to know the pronunciation of '{answer}'?"
                                f"\nYou: ")

            if confirm == 'yes':
                break

            else:
                question = input(f"Bot: Type a word that you want the pronunciation of. \nYou: ").lower()
                answer = lastWord(question)

        pronunciation = api.wordAPI_pronunciation(answer)
        return pronunciation

    if response_type == 'example':
        confirm = 'no'
        answer = useWOrd(question)

        while confirm != 'yes':

            confirm = input(f"Bot: Do you want to see '{answer}' used in a sentence? [yes/no]\nYou: ").lower()

            while (confirm != 'no') and (confirm != 'yes'):
                confirm = input(f"Bot: Please type yes or no. Do you want to see '{answer}' used in a sentence?\nYou: ")

            if confirm == 'yes':
                break

            else:
                question = input(f"Bot: Type a word that you want to see used in a sentence. \nYou: ").lower()
                answer = lastWord(question)

        example = api.wordAPI_examples(answer)
        return example

    if response_type == 'everything':
        confirm = 'no'
        answer = lastWord(question)

        while confirm != 'yes':

            confirm = input(f"Bot: Do you want to see everything about '{answer}'? [yes/no]\nYou: ").lower()

            while (confirm != 'no') and (confirm != 'yes'):
                confirm = input(f"Bot: Please type yes or no. Do you want to see everything about '{answer}'?\nYou: ")

            if confirm == 'yes':
                break

            else:
                question = input(f"Bot: Type a word that you want to see everything about. \nYou: ").lower()
                answer = lastWord(question)

        everything = api.wordAPI_everything(answer)
        return everything

    if response_type == 'help':

        answer = error.help_me()
        return answer


while True:
    user_input = input("You: ")

    if user_input == 'stop now':
        break

    print("Bot:", get_response(user_input))