import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))
# print(type(data))
user_input = (input("Enter the Word: "))
user_input = user_input.casefold()


def translate(user_input):
    
   
    close_by = get_close_matches(user_input, data.keys())
    # print(close_by)

    if user_input in data:
        return data[user_input]
    elif len(close_by) > 0:
        print(f"Did you mean {close_by [0]} instead? ")
        yn = input(" Enter Y for yes and N for no.: ")
        if yn == "Y":
            return data[close_by[0]]
        elif yn == "N":
            return "Sorry, The word that you were looking for is not in our database"
        else:
            return "Sorry, The program did not understand your query"
    else:
        return"Sorry, The word does not exist, Please double check it"


output = translate(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
