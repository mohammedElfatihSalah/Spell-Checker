import math
from collections import defaultdict
from LanguageModel import LanguageModel

class StupidBackoffLanguageModel(LanguageModel):
  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.total =0
    self.word_counts = defaultdict(lambda: 0)
    self.bi_word_counts = defaultdict(lambda: defaultdict(lambda: 0))

    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    for sentence in corpus.corpus:
   
      for i,dotum in enumerate(sentence.data[1:]):
        self.bi_word_counts[dotum.word][sentence.data[i].word] +=1
        

   
    
    for sentence in corpus.corpus:
      for i,dotum in enumerate(sentence.data):
        self.word_counts[dotum.word] +=1
        self.total +=1


      
    
    
  def _get_logit(self, prev, word,n=2):
    if n == 0:
      return 0

    freq = 0
    if n == 2:
      freq = self.bi_word_counts[word][prev]
      if freq == 0:
        return math.log(0.4) + self._get_logit(prev, word, n-1)
      else:
        
        return math.log(freq) - math.log(self.word_counts[word])
    elif n == 1:
      freq = self.word_counts[word]
      if freq == 0:
        return math.log(0.4) + self._get_logit(prev, word, n-1)
      else:
        return math.log(freq) - math.log(self.total)

     
  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score =  0.0
    for i,token in enumerate(sentence[1:]):
      prev = sentence[i]
      word = token

      score += self._get_logit(prev, word, 2)
    return score


