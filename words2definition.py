import requests
import json

input_file = open("input.txt", "r")
data = input_file.read()
 
data_into_list = data.split("\n")

# cleans output file
open("output.txt", "w").close()

for x in range(0, len(data_into_list)):

    new_string = data_into_list[x]
    string = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + new_string

    jdata = requests.get(url=string)

    try:
        response_jdata = json.loads(jdata.text)
        with open('output.txt', 'a', encoding='utf-8') as json_file:
            try: 
                print("defining word: " + new_string + " & left over words: " + str(len(data_into_list)-x) + " words")
                output_data = response_jdata[0]['meanings'][0]['definitions'][0]['definition']
                json_file.write(new_string + ": " + str(output_data) + "\n\n")
            except KeyError:
                json_file.write(new_string + ": " + "couldn't find definition" + "\n\n")
                continue
    except: 
        print("\nerror in defining word: \"" + new_string + "\" -> is there a space in the file?\n")

    continue

input_file.close()
