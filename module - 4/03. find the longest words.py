def longest_woed(filename):
    with open(filename,'r') as infilit:
        words = infilit.read().split()
    
    max_len = len (max(words, key=len))
    return[word for word in words if len(word)==max_len]

print(longest_woed('student.txt'))