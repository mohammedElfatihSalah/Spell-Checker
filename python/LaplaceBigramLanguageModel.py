from collections import defaultdict
import math
from LanguageModel import LanguageModel

class LaplaceBigramLanguageModel(LanguageModel):

  def __init__(self, corpus, epsilon=7):
    """Initialize your data structures in the constructor."""
    # TODO your code here'
    self.v = 0
    self.total=0
    self.epsilon=epsilon
    self.vocab = defaultdict(lambda:defaultdict(lambda:0))
    self.word_counts= defaultdict(lambda:0)
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    
    for sentence in corpus.corpus:
      for i,dotum in enumerate(sentence.data[1:]):
        self.vocab[dotum.word][sentence.data[i].word] +=1
        self.word_counts[sentence.data[i].word] +=1
        self.total +=1
    self.v = len(self.vocab.keys())
    
  
  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    score =  0.0
    for i,token in enumerate(sentence[1:]):
      prev = sentence[i]
      current = token
      freq = self.vocab[current][prev] + self.epsilon

      score += math.log(freq)
      score -= math.log(self.word_counts[prev] + self.epsilon * self.v)
    return score 
