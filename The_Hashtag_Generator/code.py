# code
'''python'''

def generate_hashtag(s):
    x=s.isspace()
    if s == '' or s == '#' or len(s) >= 140:
        result = False
    elif x:
        result = False
    else:
        result = '#'+str(s.title().replace(' ', ''))
    return result
