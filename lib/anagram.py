# your code goes here!
class Anagram:
    def __init__ (self, word):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))
    def match(self, words):
        matches = []
        for word in words:
            if word.lower() != self.word and ''.join(sorted(word.lower())) == self.sorted_word:
                matches.append(word)
        return matches
    