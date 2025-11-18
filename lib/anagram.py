# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)
        pass


    def match(self, word_list):
        matches = []
        for candidate in word_list:
            lower_candidate = candidate.lower()

            if lower_candidate == self.word:
                continue

            if sorted(lower_candidate) == self.sorted_word:
                matches.append(candidate)
        
        return matches
       
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
