import requests
import json

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
		ask = str(input("Would you like to see the statistics for a specific location or demographic?: "))
		if ask.upper() == "YES":
			print("\n")
			print("Below is a list of locations or demographics to choose from: \n")
			var = list(COVID_Call)[1:]
			for item in var:
				print(item)
			print('\n')
			chosen = input("Please choose a location or demographic: ")
		else:
			chosen = 'All'
	else:
		chosen = 'All'

	return chosen


# what stat we want function
def stats(data, user_said, province ='All'): #this takes the whole country data, takes province we considering an d
	if user_said == "recovered":
		print(data[province]["recovered"])
	elif user_said == 'confirmed':
		print(data[province]["confirmed"])
	else:
		print(data[province]["deaths"])



def symptom_check():
	print("Talking2U: Note this checker is not a replacement for a COVID test! If you are experiencing a life-threatening emergency, call 911 NOW. Otherwise, please answer the following questions.")
	monitor =[]
	print('Talking2U: What is your age?')
	age = input(name + ': ')
	print('Talking2U: What is your gender? Male, Female or Other?')
	gender = input(name + ': ')
	print('Talking2U: Are you experiencing any of the following symptoms: new or worsening seizures, extreme difficulty breathing, bluish lips or face?')
	symptoms = input(name + ': ')
	monitor.append(symptoms)
	print('Talking2U: Are you experiencing: dehydration, difficulty speaking, or disorientation (confusion)?')
	symptoms = input(name + ': ')
	monitor.append(symptoms)
	if 'yes' or 'YES' in monitor:
		print("Talking2U: You need urgent medical help - please call 911")



#main function
def main():
	#check if valid country
	valid_country = False
	country_input = ['']
	print('Talking2U: What country would you like check out?')
	while not valid_country:
		country_input = input(name + ': ').split()
		valid_country = any(item in country_input for item in countries)
		if not valid_country:
			print('Talking2U: Please enter a valid country.')
	for item in countries:
		if item in country_input:
			country = item
			break

	data = get_data(country)
	province = num_prov(country)
	print('What would you like to see specifically? Choose either "recovered", "confirmed", or "deaths".')
	user_said = input('Enter your selection: ')
	stats(data, user_said, province)


if __name__=='__main__':
	print('===================================== Talking2U Chat Bot =====================================')
	print()
	name = input('Please enter your name: ')
	print('Talking2U: Hello, ' + name + '!')
	print('Talking2U: Would you like to see COVID-19 country statistics or check your COVID-19 symptoms?')
	enter = input(name + ': ')
	if enter == 'COVID-19 country statistics':
		main()
	else:
		symptom_check()
