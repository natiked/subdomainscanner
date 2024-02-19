import requests

cities = open('city.txt','r')
countries = open('countries.txt','r')
city_line = cities.readlines()
country_line = countries.readlines()
base_link = input("What is the base link: ")
valid = 0

for line in city_line:
    city = line.replace('\n','')
    try:
        request_reply = requests.get('http://' + city + '.'+ base_link)
        print('[+]Valid: ' + line)
        valid = valid + 1       
    except:
        #print('[-]Invalid: ' + line)
        pass

print('[?] Checking Country')
for line in country_line:
    country = line.replace('\n','')
    try:
        request_reply = requests.get('http://' + country + '.'+ base_link)
        print('[+]Valid: ' + country)
        valid = valid + 1       
    except:
        #print('[-]Invalid: ' + line)
        pass

        

        

       
       

        
        
        
    

