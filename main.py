import requests
import json

#function to get country data




#function for number of provinces






# what stat we want function




#main function
def main():
	print('Hello! I am Talking2U, a chat bot desgined to give statstics about COVID-19 from around the world.')
	country = input('What country would you like check out? Please enter a country: ').strip().title()
	data = get_data(country)
	province = num_prov(country)
	print('What would you like to see specifically? Choose either "recovered", "confirmed", or "deaths".')
	user_said = input('Enter your selection: ')
	stats(data, user_said, province = 'All')

if __name__=='__main__':
	main()



