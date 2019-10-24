from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import json

class ActionAttrition(Action):
	def name(self):
		print('in self method')
		return 'action_attrition'

	def run (self, dispatcher, tracker, domain):
		print('in run method')
		mon = tracker.get_slot('month')
		print(mon)
		with open('data.txt') as json_file:
			data = json.load(json_file)
			
			for result in data['current']:
				print('Month:'+ result['Month'])
				if result['Month'].lower() == mon.lower():
					print('month Found')
					Month = result['Month']
					Opening_Balance = result['Opening_Balance']
					Employees_joined = result['Employees_joined']
					Employees_Left = result['Employees_Left']
					Closing_Balance = result['Closing_Balance']
					Attrition = result['Attrition%']
		response ="""The attrition percentage for month {} is {} %. {} employees left and {} employees joined the organization.""".format(Month, Attrition,Employees_Left,Employees_joined)
		
		print(response)
						
		dispatcher.utter_message(response)
		return [SlotSet('month',mon)]
		