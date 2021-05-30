from abc import ABC, abstractmethod
class LanguageModel:
  @abstractmethod
  def train(self, corpus):
    pass
  @abstractmethod
  def score(self, sentence):
    pass