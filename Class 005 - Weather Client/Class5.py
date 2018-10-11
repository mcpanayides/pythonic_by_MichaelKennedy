import requests
import bs4

def main():
    print_the_header()
    zipcode = input('What zipcode do you want the weather for: ')
    html = get_data(zipcode)
    get_weather_from_html(html)
    #display for the forecast 


def print_the_header():
    print('=========================')
    print('=  Weather Application  =')
    print('=========================')
    print()
        

def get_data(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html): 
    soup = bs4.BeautifulSoup(html, 'html.parser')
  #  location = soup.find(div_='region-content-header').find('h1').get_text()
    weatherCondition = soup.find(id='curCond').find(class_='wu-value').get_text()
    weatherTemp = soup.find(id='curTemp').find(class_='wu-value').get_text()
    weatherScalar = soup.find(id='curTemp').find(class_='wu-label').get_text()    
    print(weatherCondition, weatherTemp,  weatherScalar)

    #,  weatherCondition, weatherTemp,  weatherScalar
   



if __name__ == '__main__':
    main() 