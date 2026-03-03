import sys
import requests
from colorama import init, Fore, Style as CStyle


BASE_URL = "https://musicbrainz.org/ws/2/recording?query=tag:{genre}&fmt=json"


def search_by_genre(genre):

    response = requests.get(BASE_URL.format(genre=genre))

    if response.status_code != 200:
        print("Error fetching data")
        return

    data = response.json()

    tracks_id = data.get("recordings", [])

    if not tracks_id:
        print("No tracks found.")
        return

    for i, track in enumerate(tracks_id[:10], start=1):
        title = track["title"]
        artist = track["artist-credit"][0]["name"]

        if i < 10:
            print(f"{CStyle.BRIGHT}{Fore.GREEN}{i}.  {Fore.YELLOW}{title}{CStyle.RESET_ALL} – {CStyle.BRIGHT}{Fore.CYAN}{artist}{CStyle.RESET_ALL}")

        else:
            print(f"{CStyle.BRIGHT}{Fore.GREEN}{i}. {Fore.YELLOW}{title}{CStyle.RESET_ALL} – {CStyle.BRIGHT}{Fore.CYAN}{artist}{CStyle.RESET_ALL}")


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
        print(f"{CStyle.BRIGHT}{Fore.YELLOW}Welcome to {Fore.GREEN}TrackGenerator{Fore.YELLOW}. Type <help> for more information.{CStyle.RESET_ALL}")
        while True:
            command = input(">> ")
            if command.lower() == 'exit':
                print("Goodbye!")
                break
            search_by_genre(command)

    genre = sys.argv[1]
    search_by_genre(genre)


if __name__ == "__main__":
    main()
