import sys
import requests
import time
from colorama import init, Fore, Style as CStyle
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style as PTStyle

BASE_URL = "https://musicbrainz.org/ws/2/recording?query=tag:{genre}&fmt=json"

style = PTStyle.from_dict({
    "prompt": "ansigreen dim",
    "": "bold ansibrightgreen",
})

minn = 0
maxx = 10


def safe_request(url, headers):
    """Prevent connection reset and API throttling."""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        time.sleep(1.2)

        if response.status_code != 200:
            return None

        return response.json()

    except requests.exceptions.RequestException:
        return None


def search_by_genre(genre, twice):

    headers = {
        "User-Agent": "TrackGenerator/1.0 (flaviusepintilie@gmail.com)"
    }

    data = safe_request(
        BASE_URL.format(genre=genre),
        headers
    )

    if data is None and not twice:
        print("Network error or connection reset.")
        return

    tracks_id = data.get("recordings", [])

    if not tracks_id and not twice:
        print("No tracks found.")
        return

    verify = False

    for i, track in enumerate(tracks_id[minn:maxx], start=1):

        title = track.get("title", "Unknown title")

        artist_credit = track.get("artist-credit", [])
        artist = artist_credit[0]["name"] if artist_credit else "Unknown artist"

        verify = True

        if i < 10:
            print(
                f"{CStyle.BRIGHT}{Fore.GREEN}{i}.  "
                f"{Fore.YELLOW}{title}{CStyle.RESET_ALL} – "
                f"{CStyle.BRIGHT}{Fore.CYAN}{artist}{CStyle.RESET_ALL}"
            )

        else:
            print(
                f"{CStyle.BRIGHT}{Fore.GREEN}{i}. "
                f"{Fore.YELLOW}{title}{CStyle.RESET_ALL} – "
                f"{CStyle.BRIGHT}{Fore.CYAN}{artist}{CStyle.RESET_ALL}"
            )

    if not verify:
        if not twice:
            print(
                f"{CStyle.BRIGHT}{Fore.RED}"
                f"No or no more tracks found for genre/tag: {genre}"
                f"{CStyle.RESET_ALL}"
            )
        return False

    return True


def main():
    global minn, maxx
    run_out = False
    print(fr"""{CStyle.BRIGHT}
{Fore.MAGENTA}___________                     __       {Fore.GREEN}________                                   __
{Fore.MAGENTA}\__    ___/___________    ____ |  | __  {Fore.GREEN}/  _____/  ____   ____   ________________ _/  |_  ___________
{Fore.MAGENTA}  |    |  \_  __ \__  \ _/ ___\|  |/ / {Fore.GREEN}/   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
{Fore.MAGENTA}  |    |   |  | \// __ \\  \___|    <  {Fore.GREEN}\    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
{Fore.MAGENTA}  |____|   |__|  (____  /\___  >__|_ \  {Fore.GREEN}\______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|
{Fore.MAGENTA}                      \/     \/     \/         {Fore.GREEN}\/     \/     \/     \/           \/

          {Fore.BLUE}Feeling stuck with your own thoughts in the metro/train or whatever? Just let the music flow!{CStyle.RESET_ALL}
          """)

    if len(sys.argv) >= 2:
        genre = sys.argv[1]
        search_by_genre(genre)
        return

    print(f"{CStyle.BRIGHT}{Fore.YELLOW}Welcome to TrackGenerator. Type <help> for more information.{CStyle.RESET_ALL}")

    previous_command = None

    while True:

        command = prompt(
            [("class:prompt", ">>> ")],
            style=style
        ).strip()

        if command.lower() == 'exit':
            print("Goodbye!")
            break

        elif command.lower() == 'help':
            print(fr"""{CStyle.BRIGHT}
{Fore.YELLOW}Basic Usage: {Fore.GREEN}trackgen <genre>{CStyle.RESET_ALL}" 
- This command will be runned outside of the interactive mode, directly in the terminal. It will fetch and display tracks based on the specified genre/tag.
{CStyle.BRIGHT}{Fore.YELLOW}Example: {Fore.GREEN}trackgen rock{CStyle.RESET_ALL}")
You can also run the command without any arguments to enter the interactive mode, where you can type genres/tags and get tracks on the fly.
If you are traveling and want the feel the vibe of the country you are in, just type the name of the country as a genre/tag.
For example, if you are in Italy, just type {Fore.GREEN}italy{CStyle.RESET_ALL} and enjoy the music of the country you are in.


{CStyle.BRIGHT}{Fore.YELLOW}Type {Fore.GREEN}more{Fore.YELLOW} in the interactive mode to fetch more tracks for the last entered genre/tag.

Type {Fore.GREEN}exit{Fore.YELLOW} to exit the interactive mode.

What will happen if you enter a genre/tag that is really weird. For example, if you enter just the letter {Fore.GREEN}d{CStyle.RESET_ALL},
The API will search its database for any recordings where a user typed "d" as a tag. It will find those tracks, return the JSON data. 
They will likely be completely random songs that just happen to have that weird tag.
            """)

        elif command.lower() == 'more':

            if previous_command is None:
                print(
                    f"{CStyle.BRIGHT}{Fore.RED}No previous command found. Please enter a genre first.{CStyle.RESET_ALL}")
                continue

            minn += 10
            maxx += 10

            if not search_by_genre(previous_command, False):
                run_out = True

        else:

            if run_out:

                search_by_genre(command, True)
                minn = 0
                maxx = 10

            search_by_genre(command, False)
            previous_command = command

            run_out = False

    if __name__ == "__main__":
        main()
