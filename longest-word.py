import re
def LongestWord(sen): 
    # defining valid characters
    regex = re.compile('[^a-zA-Z]')

    # parsing input to list
    sen_list = sen.split(" ")

    # initiating comparison loop
    max_len = 0
    for sen in sen_list:
        # using re.sub to remove unvalid chracters from string
        sen = regex.sub('', sen)
        if len(sen) > max_len:
            max_len_word = sen
            max_len = len(max_len_word)

    return max_len_word
    
# function call
print LongestWord(input())