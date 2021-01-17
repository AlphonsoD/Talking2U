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





# if __name__=='__main__'
#main()



