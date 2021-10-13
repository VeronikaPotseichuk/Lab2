from abc import ABCMeta, abstractmethod
 
 
class serializer_basic():
	@abstractmethod
	def load(self, string):
		pass

	@abstractmethod
	def dump(self, obj):
		pass
