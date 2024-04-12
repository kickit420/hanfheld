import requests

def find_strain(strain_name):
    strain_formatted = strain_name.replace(" ", "%20")
    request_url = "https://de.seedfinder.eu/api/json/search.json?q=" + strain_formatted

    headers = {
        "Authorization": "b10854879ea0334e9c08ecd7cc1f3bab"
    }

    response = requests.get(request_url, headers=headers)

    # Überprüfe, ob die Anfrage erfolgreich war
    if response.status_code == 200:
        # Gibt die Daten als JSON zurück
        print(response.json())
        return response.json()
    else:
        # Gibt Fehlermeldung aus, wenn die Anfrage nicht erfolgreich war
        return f"Error: {response.status_code} - {response.text}"


def main():
    find_strain("Lemon Haze")


if __name__ == "__main__":
    main()
