import requests
import json
import time

countries = [
	'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
	'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
	'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria',
	'Burkina Faso', 'Burma', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic',
	'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica',
	"Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Diamond Princess', 'Djibouti', 'Dominica',
	'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini',
	'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada',
	'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hungary', 'Iceland', 'India',
	'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya',
	'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
	'Liechtenstein', 'Lithuania', 'Luxembourg', 'MS Zaandam', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali',
	'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
	'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
	'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
	'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
	'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
	'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
	'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan*',
	'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda',
	'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',
	'West Bank and Gaza', 'Yemen', 'Zambia', 'Zimbabwe', 'US', 'Global'
]

# To create list of countries able to be interpreted by bot
special_case = []
n = 0
for country in countries:
	splitter = countries[n].split()
	if len(splitter) == 1:
		special_case.append(countries[n])
	else:
		None
	n = n + 1

#function to get country data
def get_data(country = 'All'):
	response = requests.get("https://covid-api.mmediagroup.fr/v1/cases", params ={'country': country})
	data = json.loads(response.text)
	return data #this is the dictionary with the country info in it


#function for number of provinces
def num_prov(country):
	x = str(country)
	COV_dat = requests.get('https://covid-api.mmediagroup.fr/v1/cases', params = {'country':x})
	COVID_Call = json.loads(COV_dat.text)

	amount = len(list(COVID_Call))

	if amount > 1:
		print("\nTalking2U: Would you like to see the statistics for a specific location or demographic? Please say yes or no\n")
		ask = str(input(name + ": "))
		if ask.upper() == "YES":
			print("\nTalking2U: Please choose one of the locations or demographics below! Please spell it correctly! I'm case-sensitive hehe\n")
			var = list(COVID_Call)[1:]
			for item in var:
				print(item)
			print('\n')
			chosen = str(input(name + ": "))
		else:
			chosen = 'All'
	else:
		chosen = 'All'

	return chosen


# what stat we want function
def stats(data, country, key, province): #this takes the whole country data, takes province we considering an d
	if key == "ALL":
		if province == 'All':
			print("\n")
			print(f'''Talking2U: In {country} there are currently {data[province]["confirmed"]} cases, {data[province]["recovered"]} cases have recovered, 
	           and there have been {data[province]["deaths"]} mortalities.''')
		else:
			print("\n")
			print(f'''Talking2U: In {province} there are currently {data[province]["confirmed"]} cases, {data[province]["recovered"]} cases have recovered, 
	   and there have been {data[province]["deaths"]} mortalities.\n''')
	elif key == "RECOVERED":
		print(f'''\nTalking2U: Of the {data[province]["confirmed"]} confirmed cases, there are currently {data[province]["recovered"]} recovered cases!''')
	elif key == 'CONFIRMED':
		print(f'''\nTalking2U: As of the recent statistics, there are currently {data[province]["confirmed"]} confirmed COVID-19 cases.''')
	else:
		print(f'''\nTalking2U: As of the recent statistics, have been {data[province]["deaths"]} mortalities.''')
	print(f'''\nTalking2U: Remember to wear a mask, socially distance, and follow your local COVID-19 
	   guidelines and legislations! Stay safe and healthy {name}!''')




def symptom_check(): #If you can, pls check this to check the formatting <3
	print("\nTalking2U: Alright, let me fetch my assessment tool!")
	time.sleep(0.5)
	print("\nTalking2U: ...")
	time.sleep(1.5)
	print("""\nTalking2U: Here it is! The following questionnaire will help you determine if you require 
further assessment for COVID-19 per the Government of Canada Self-Assessment Tool""")
	time.sleep(1)
	print("""\nTalking2U: Please note this checker is not a replacement for a COVID test!
	   If you are experiencing a life-threatening emergency, call 911 NOW. 
	   Otherwise, please answer the following questions.""")
	time.sleep(3)
	print("""\nTalking2U: Are you experiencing any of the following symptoms:

	   - severe difficulty breathing
	   - severe chest pain
	   - extreme difficulty waking up
	   - confusion
	   - loss of consciousness

	   Please answer yes or no\n""")
	symptoms = str(input(name + ': ')).upper()
	symp_list = symptoms.split(" ")
	time.sleep(0.5)
	if 'YES' in symp_list:
		print("""\nTalking2U: You need urgent medical help - please call 911 or go to
           your nearest emergency department. These symptoms require immediate attention, 
           according to the Government of Canada Self-Assessment Tool""")
	else:
		print("""\nTalking2U: Are you experiencing any of the following symptoms?
	   - a new or worsening cough
	   - headache
	   - new loss of smell or taste
	   - shortness of breath or difficulty breathing
	   - feeling very unwell
	   - chills
	   - fatigue or weakness
	   - muscle or body aches
	   - gastrointestinal symptoms (i.e. abdominal pain, vomiting, diarrhea)
	   - temperature equal to or over 38°C
	   - feeling feverish

	   Please answer yes or no\n""")
		symptoms = str(input(name + ': ')).upper()
		symp_list = symptoms.split()
		time.sleep(0.5)
		if 'YES' in symp_list:
			print("""\nTalking2U: Please self-isolate. The Public Health Agency of Canada asks
	   anyone with the above symptoms to please self-isolate as a precaution""")
			time.sleep(0.5)
			print("\nTalking2U: ...")
			time.sleep(2.5)
			print("""\nTalking2U: To determine your next steps, please utilize the COVID-19 Self-Assessment tool on
	   the Government of Canada website.""")
		else:
			print(f'''\nTalking2U: You have no need to worry! Remember to wear a mask, socially distance,
         and follow your local COVID-19 guidelines and legislations! Stay safe and healthy {name}!''')



#main function
def main():
	#check if valid country
	valid_country = False
	country_input = ['']
	print('\nTalking2U: What country would you like check out? Please choose from the list below!')
	print('\nTalking2U: If you want to check out the global statistics instead, ask for global!\n')
	#https://www.geeksforgeeks.org/python-printing-list-vertically/
	nice_way = [special_case[0:53],special_case[53:106],special_case[106:157]]
	for i in range(51): 
	    for x in nice_way: 
	        print(x[i], end = '  ||  ') 
	    print()
	print(' ')
	time.sleep(1)
	while not valid_country:
		country_input = input(name + ': ').split()
		country_input = [x.title() for x in country_input]
		us_variation = ['US', 'Us', 'uS','us']
		for i in us_variation:
			if i in country_input:
				country_input = ['US']
		valid_country = any(item in country_input for item in countries)
		if not valid_country:
			print("\nTalking2U: Sorry, I didn't quite understand that. Did you choose a country from the list?\n")

	for item in countries:
		if item in country_input:
			country = item.title()
			if country == 'Us':
				country ='US'
			break

	data = get_data(country)
	province = num_prov(country)

	print('\nTalking2U: What would you like to see specifically? The number of confirmed or recovered cases, deaths, or all of the statistics?\n')
	user_said = str(input(name + ': ')).lower()

	beta = True #for loop to allow for less case-sensitivity
	said = list(user_said.split(" "))
	all_words = ['all', 'everything']
	recovered_words = ['recovered','survived','survivors']
	confirmed_words = ['confirmed']
	death_words = ['deaths','mortalities','fatalities','died','dead']
	while beta:
		for wurd in said:
			if wurd in all_words:
				key = 'ALL'
				beta = False
				break
			elif wurd in recovered_words:
				key = 'RECOVERED'
				beta = False
				break
			elif wurd in confirmed_words:
				key = 'CONFIRMED'
				beta = False
				break
			elif wurd in death_words:
				key = 'DEATHS'
				beta = False
				break
		else:
			print("Talking2U: I apologize but I don't think I quite understood that. Please say that again")

	stats(data, country, key, province) #changed user_said to key to accommodate less case-sensitivity (see above)

def get_name():
	name = input('Please enter your name: ')
	name = name.title()
	print('\nTalking2U: Hello, ' + name + '!')
	return name



if __name__=='__main__':
	print('===================================== Talking2U Chat Bot =====================================')
	print()
	#name = input('Please enter your name: ')
	#name = name.title()
	#print('\nTalking2U: Hello, ' + name + '!')
	name = get_name()
	alpha = True
	while alpha:
		print('\nTalking2U: Would you like to see COVID-19 country statistics or check your COVID-19 symptoms?\n')
		enter = str(input(name + ': ')).lower()
		words = list(enter.split(" "))
		keywords = ['stats','statistics', 'country', 'stat']
		symptom_words = ['symptoms', 'signs', 'symptom', "indicator"]
		for word in words:
			if word in keywords:
				main()
				alpha = False
				break
			elif word in symptom_words:
				symptom_check()
				alpha = False
				break
		else:
			print("\nTalking2U: Hmm...I didn't quite get that.")
