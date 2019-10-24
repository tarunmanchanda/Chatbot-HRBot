from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter

def train_nlu(data, config_file, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(config_file))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'attritionnlu')

def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/attritionnlu')
	print(interpreter.parse(u"I was wondering what was the attrition percentage in July?"))



if __name__ == '__main__':
	train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
	run_nlu()