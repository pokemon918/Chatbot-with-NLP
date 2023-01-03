from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# Creating ChatBot Instance
CB = ChatBot('ChatBot')
 # Training with Personal Ques & Ans
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "You're welcome.",
    "who developed you",
    "I am developed by Saikat Sheet"
    "Do you know the birthday date of Saikat"
    "Yes,9th january,2002"
]
trainer = ListTrainer(CB)
trainer.train(conversation)
# # Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(CB)
trainer_corpus.train('chatterbot.corpus.english')
