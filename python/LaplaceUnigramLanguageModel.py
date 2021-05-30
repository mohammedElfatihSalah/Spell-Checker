from collections import defaultdict
from LanguageModel import LanguageModel
import math

class LaplaceUnigramLanguageModel(LanguageModel):

  def __init__(self, corpus, epsilon = .001):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.vocab = defaultdict(lambda: 0)
    self.total = 0.0
    self.v = 0.0
    self.epsilon = epsilon
    self.train(corpus)
    

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    for sentence in corpus.corpus:
      for dotum in sentence.data:
        self.vocab[dotum.word] +=1
        self.total +=1
    self.v = len(self.vocab.keys())
    
      

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    score = 0.0
    for token in sentence:
        freq = self.vocab[token] + self.epsilon
        score += math.log(freq)
        score -=math.log(self.total + self.v * self.epsilon)
    return score
