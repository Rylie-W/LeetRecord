class StreamChecker:

    def __init__(self, words):
        self.words=set(words)
        self.pre=""

    def query(self, letter: str) -> bool:
        self.pre+=letter
        if letter in self.words:
            return True
        return self.__isSuffix()

    def __isSuffix(self):
        for word in self.words:
            if word == self.pre[-len(word):]:
                return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)