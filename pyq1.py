import requests
import csv

# Replace with your OMDb API key
API_KEY = 'your_api_key_here'
API_URL = 'http://www.omdbapi.com/'

def get_movie_titles():
    """
    Takes input from the user and returns a list of movie/series titles.
    """
    user_input = input("Enter movie/series titles (comma-separated): ")
    titles = [title.strip() for title in user_input.split(",") if title.strip()]
    return titles

def fetch_movie_data(title):
    """
    Calls OMDb API and returns data for a given title.
    """
    params = {
        't': title,
        'apikey': "306c1553"
    }
    try:
        response = requests.get(API_URL, params=params)
        data = response.json()

        if data.get('Response') == 'False':
            print(f"❌ Could not fetch data for: {title}")
            return None

        print(f"✅ {data['Title']} ({data['Year']})")

        return {
            'Title': data.get('Title'),
            'Year': data.get('Year'),
            'Genre': data.get('Genre'),
            'Director': data.get('Director'),
            'IMDB Rating': data.get('imdbRating'),
            'Language': data.get('Language'),
            'Country': data.get('Country')
        }

    except Exception as e:
        print(f"Error fetching data for {title}: {e}")
        return None

def save_to_csv(data_list, filename='movie_data.csv'):
    if not data_list:
        print("⚠️ No valid movie data to save.")
        return

    keys = data_list[0].keys()
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data_list)
    print(f"\n📁 Movie data saved to {filename}")

def main():
    titles = get_movie_titles()
    all_movie_data = []

    for title in titles:
        data = fetch_movie_data(title)
        if data:
            all_movie_data.append(data)

    save_to_csv(all_movie_data)

if __name__ == '__main__':
    main()
