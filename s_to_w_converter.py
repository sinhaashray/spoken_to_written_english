from word2number import w2n

num_rules = {
            "zero": 0,
            "one" : 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "twenty": 20,
            "thirty": 30,
            "forty": 40,
            "fifty": 50,
            "sixty": 60,
            "seventy": 70,
            "eighty": 80,
            "ninety": 90,
            "hundred": 100
            }

curr_rules = {
    "dollars":"$",
    "dollar":"$",
    "euros":"€",
    "euro":"€",
    "rupees":"₹",
    "rupee":"₹"}

time_rules = {
            "C M": "CM",
            "P M": "PM",
            "D M": "DM",
            "A M": "AM"
            }
def convert_num(sentence):
    words = sentence.split(" ")
    new_sen2 = ""
    new_sen = ""
    parent_index = -1;
    for word in words:
        if(word in num_rules):
            if(parent_index == -1):
                parent_index = words.index(word)
            new_sen = new_sen+ word
            new_sen = new_sen+ " "
        else:
            parent_index = -1
            new_sen = new_sen[:-1]
            if(new_sen != ""):
                new_sen = w2n.word_to_num(new_sen)
            new_sen2 = new_sen2 + word + " "
            if(new_sen != ""):
                new_sen2 =new_sen2 + str(new_sen) + " "
            new_sen = ""
    new_sen2 = new_sen2 + words[-1] + " "
    if(new_sen != ""):
        new_sen = w2n.word_to_num(new_sen)
        new_sen2 =new_sen2 + str(new_sen) + " "
    new_sen2 = new_sen2[:-1]
    return new_sen2

def convert_time(sentence):
    for i in range(len(sentence)-2):
        key = sentence[i:i+3]
        if(key in time_rules):
            sentence = sentence.replace(key,time_rules[key])
    return sentence

def convert(sentence):
    sentence = convert_time(sentence)
    sentence = convert_num(sentence)
    return sentence

print("Input exit to exit\n\n\n")
while(True):
    print("input sentence :\n")
    sentence = input()
    if(sentence == "exit"):
        break;
    sentence = convert(sentence)
    print(sentence)