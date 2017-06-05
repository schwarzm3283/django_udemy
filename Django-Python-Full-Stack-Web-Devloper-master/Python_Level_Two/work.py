import re

def multi_re_rind(patterns,phrase):
    for pat in patterns:
        print("Searching for patterns {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'

test_patterns = [r'\W+']

multi_re_rind(test_patterns,test_phrase)
