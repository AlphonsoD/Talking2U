import requests
import json

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


#main function
def main():
	print('Hello! I am Talking2U, a chat bot desgined to give statstics about COVID-19 from around the world.')
	country = input('What country would you like check out? Please enter a country: ').strip().title()
	#special US case
	if country == 'Us':
		country = 'US'
	data = get_data(country)
	province = num_prov(country)
	print('What would you like to see specifically? Choose either "recovered", "confirmed", or "deaths".')
	user_said = input('Enter your selection: ')
	stats(data, user_said, province)



if __name__=='__main__':
	main()
