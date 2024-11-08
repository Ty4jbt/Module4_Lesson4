# Task 1
# Analyze the code and refactor it to make it more readable and maintainable.

# Weather Forecast Application Script

# WeatherDataFetcher class fetches weather data for a given city.
class WeatherDataFetcher:
    # Initialize weather data for three cities
    def __init__(self):

        # Weather data for three cities
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    # Fetch weather data for a given city
    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})

# WeatherDataParser class parses weather data and returns a formatted weather report.
class WeatherDataParser:

    # Parse weather data and return a formatted weather report
    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    # Get detailed forecast for the weather data / acts as a placeholder for future functionality
    def get_detailed_forecast(self, data):
        return self.parse_weather_data(data)

# UserInterface class interacts with the user to get the city and display the weather forecast.
class UserInterface:
    def __init__(self, fetcher, parser):
        self.fetcher = fetcher
        self.parser = parser

    # Display weather forecast for a given city    
    def display_weather(self, city):
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse_weather_data(data)
            print(weather_report)

    # Run the user interface until the user decides to exit
    def run(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break

            # Get weather forecast based on user input
            data = self.fetcher.fetch_weather_data(city)
            if not data:
                print(f"Weather data not available for {city}")
                continue
            
            # Ask user if they want a detailed forecast / returns the same forecast for now
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.parser.get_detailed_forecast(data)
            else:
                forecast = self.parser.parse_weather_data(data)

            print(forecast)

# Main function to run the weather forecast application
def main():
    fetcher = WeatherDataFetcher()
    parser = WeatherDataParser()
    ui = UserInterface(fetcher, parser)
    ui.run()

if __name__ == "__main__":
    main()