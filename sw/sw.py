'''
Basic example of all subtrings available from a single string
'''

def get_all_substrings(word: str) -> list[str]:
    l = 0
    r = 1 # so it goes from [0:1]
    initial_position = r
    final = []
    
    while not (l == 0 and r == len(word) + 1): 
        # print(f"{word[l:r]}")
        final.append(word[l:r])
        
        l+= 1
        r+=1
        
        
        if r > len(word): # if you get to the end of the word, expand the window
            initial_position += 1
            r = initial_position
            l = 0
    return final 

if __name__ == "__main__":
    example = "example"
    example_substrings = get_all_substrings(example)