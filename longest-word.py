import re
def LongestWord(sen): 
    regex = re.compile('[^a-zA-Z]')
    #First parameter is the replacement, second parameter is your input string
    regex.sub('', 'ab3d*E')
    #Out: 'abdE'    
    sen_list = sen.split(" ")
    max_len = 0
    for sen in sen_list:
        sen = regex.sub('', sen)
        if len(sen) > max_len:
            max_len_word = sen
            max_len = len(sen)

    return max_len_word
    
# keep this function call here  
print LongestWord(raw_input())