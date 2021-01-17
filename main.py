import requests
import json

#function to get country data
def get_data(country = 'All'):
	response = requests.get("https://covid-api.mmediagroup.fr/v1/cases", params ={'country': country})
	data = json.loads(response.text)
	return data #this is the dictionary with the country info in it


#function for number of provinces






# what stat we want function
def stats(data, user_said, province ='All'): #this takes the whole country data, takes province we considering an d
	if user_said == "recovered":
		print(data[province][recovered])
	elif user_said == 'confirmed':
		print(data[province][confirmed])
	else:
		print(data[province][deaths])


#main function
def main():
	print('Hello! I am Talking2U, a chat bot desgined to give statstics about COVID-19 from around the world.')
	country = input('What country would you like check out? Please enter a country: ').strip().title()
	data = get_data(country)
	province = num_prov(country)
	print('What would you like to see specifically? Choose either "recovered", "confirmed", or "deaths".')
	user_said = input('Enter your selection: ')
	stats(data, user_said, province)

if __name__=='__main__':
	main()
