import requests
import json

#function to get country data




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
		else
			chosen = 'All'
	else:
		chosen = 'All'

	return chosen






# what stat we want function




#main function



# if __name__=='__main__'
#main()



