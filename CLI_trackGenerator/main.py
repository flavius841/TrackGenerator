import sys
import requests
from colorama import init, Fore, Style as CStyle


BASE_URL = "https://api.deezer.com/search"


def search_by_genre(genre):
    params = {
        "q": f'genre:"{genre}"'
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error fetching data")
        return

    data = response.json()

    tracks = data.get("data", [])

    if not tracks:
        print("No tracks found.")
        return

    for i, track in enumerate(tracks[:10], start=1):
        title = track["title"]
        artist = track["artist"]["name"]
        print(f"{i}. {title} – {artist}")


def main():

    print(fr"""{CStyle.BRIGHT} 
{Fore.MAGENTA}___________                     __       {Fore.GREEN}________                                   __                
{Fore.MAGENTA}\__    ___/___________    ____ |  | __  {Fore.GREEN}/  _____/  ____   ____   ________________ _/  |_  ___________ 
{Fore.MAGENTA}  |    |  \_  __ \__  \ _/ ___\|  |/ / {Fore.GREEN}/   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
{Fore.MAGENTA}  |    |   |  | \// __ \\  \___|    <  {Fore.GREEN}\    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
{Fore.MAGENTA}  |____|   |__|  (____  /\___  >__|_ \  {Fore.GREEN}\______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
{Fore.MAGENTA}                      \/     \/     \/         {Fore.GREEN}\/     \/     \/     \/           \/                   

          {Fore.BLUE}Feeling stuck with your own thoughts in the metro/train or whatever? Just let the music flow!{CStyle.RESET_ALL}
          """)

    if len(sys.argv) < 2:
        print("Usage: trackgen <genre>")
        sys.exit(1)

    genre = sys.argv[1]
    search_by_genre(genre)


if __name__ == "__main__":
    main()
