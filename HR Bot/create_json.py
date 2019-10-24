import json

data = {}  
data['current'] = []  
data['current'].append({  
    'Month': 'January',
    'Opening_Balance': 27,
    'Employees_joined': 3,
	'Employees_Left': 1,
	'Closing_Balance': 29,
	'Attrition%': 3.45
	
})

data['current'].append({  
    'Month': 'Feburary',
    'Opening_Balance': 29,
    'Employees_joined': 1,
	'Employees_Left': 5,
	'Closing_Balance': 25,
	'Attrition%': 20.00
	
})

data['current'].append({  
    'Month': 'March',
    'Opening_Balance': 25,
    'Employees_joined': 4,
	'Employees_Left': 2,
	'Closing_Balance': 27,
	'Attrition%': 7.41
	
})

data['current'].append({  
    'Month': 'April',
    'Opening_Balance': 27,
    'Employees_joined': 1,
	'Employees_Left': 0,
	'Closing_Balance': 28,
	'Attrition%': 0.00
	
})

data['current'].append({  
    'Month': 'May',
    'Opening_Balance': 28,
    'Employees_joined': 0,
	'Employees_Left': 6,
	'Closing_Balance': 22,
	'Attrition%': 27.27
	
})

data['current'].append({  
    'Month': 'June',
    'Opening_Balance': 22,
    'Employees_joined': 12,
	'Employees_Left': 3,
	'Closing_Balance': 31,
	'Attrition%': 9.68
	
})

data['current'].append({  
    'Month': 'July',
    'Opening_Balance': 31,
    'Employees_joined': 1,
	'Employees_Left': 2,
	'Closin_Balance': 30,
	'Attrition%': 6.67
	
})

data['current'].append({  
    'Month': 'August',
    'Opening_Balance': 30,
    'Employees_joined': 1,
	'Employees_Left': 0,
	'Closing_Balance': 31,
	'Attrition%': 0.00
	
})

data['current'].append({  
    'Month': 'September',
    'Opening_Balance': 31,
    'Employees_joined': 1,
	'Employees_Left': 2,
	'Closing_Balance': 30,
	'Attrition%': 6.67
	
})

data['current'].append({  
    'Month': 'October',
    'Opening_Balance': 30,
    'Employees_joined': 1,
	'Employees_Left': 1,
	'Closing_Balance': 30,
	'Attrition%': 3.33
	
})

data['current'].append({  
    'Month': 'November',
    'Opening_Balance': 30,
    'Employees_joined': 1,
	'Employees_Left': 1,
	'Closing_Balance': 30,
	'Attrition%': 3.33
	
})

data['current'].append({  
    'Month': 'December',
    'Opening_Balance': 30,
    'Employees_joined': 1,
	'Employees_Left': 2,
	'Closing_Balance': 29,
	'Attrition%': 6.90
	
})

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)