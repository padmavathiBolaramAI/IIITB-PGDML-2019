from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from slack import SlackInput


#nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
#agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = interpreter)

input_channel = SlackInput('xoxb-404932233751-421217573089-vjUkaN7U5XjU3bYJ21o5Ey02') #app verification token
							#'xoxb-404932233751-416120617730-o4rB5gvqUyMVQveYvcMqmyBV' # bot verification token
							#'Bsi471fJ6ftZtAerPfAS9WuJ', # slack verification token
							#True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))