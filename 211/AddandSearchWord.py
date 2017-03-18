class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p = self.dic
        for ch in word:
            if ch not in p:
                p[ch] = {}
            p = p[ch]
        p['#'] = '#'

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        p = [self.dic]
        for ch in word:
            if ch != '.':
                p = map(lambda tr:tr[ch],filter(lambda tr:ch in tr,p))
            else:
                q = []
                for tr in p:
                    if isinstance(tr,dict):
                        q += filter(lambda x:isinstance(x,dict),tr.values())
                p = q
        return True if any(map(lambda tr:'#' in tr,p)) else False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)