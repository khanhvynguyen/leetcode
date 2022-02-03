# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/ 

from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        new_sentences = []
        for sentence in sentences:
            new_sentences.append( sentence.split(" ") )
        sorted_sentences = sorted(new_sentences, key=len)
        longest_sentence = sorted_sentences[-1]
        return len(longest_sentence)


sentences = ["please wait", "continue to fight", "continue to win"]
print(Solution().mostWordsFound(sentences))
