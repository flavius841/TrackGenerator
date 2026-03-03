import sys
import requests
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


def search_by_genre(genre):

    response = requests.get(BASE_URL.format(genre=genre))
    verify = False

    if response.status_code != 200:
        print("Error fetching data")
        return

    data = response.json()

    tracks_id = data.get("recordings", [])

    if not tracks_id:
        print("No tracks found.")
        return

    for i, track in enumerate(tracks_id[minn:maxx], start=1):
        title = track["title"]
        artist = track["artist-credit"][0]["name"]
        verify = True

        if i < 10:
            print(f"{CStyle.BRIGHT}{Fore.GREEN}{i}.  {Fore.YELLOW}{title}{CStyle.RESET_ALL} – {CStyle.BRIGHT}{Fore.CYAN}{artist}{CStyle.RESET_ALL}")

        else:
            print(f"{CStyle.BRIGHT}{Fore.GREEN}{i}. {Fore.YELLOW}{title}{CStyle.RESET_ALL} – {CStyle.BRIGHT}{Fore.CYAN}{artist}{CStyle.RESET_ALL}")

    if not verify:
        print(
            f"{CStyle.BRIGHT}{Fore.RED}No or no more tracks found for genre/tag: {genre}{CStyle.RESET_ALL}")


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
            command = prompt(
                [("class:prompt", ">>> ")],
                style=style,
                # completer=command_completer,
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
                if 'previous_command' not in locals():
                    print(
                        f"{CStyle.BRIGHT}{Fore.RED}No previous command found. Please enter a genre first.{CStyle.RESET_ALL}")
                    continue
                global minn, maxx
                minn += 10
                maxx += 10
                search_by_genre(previous_command)

            else:
                search_by_genre(command)
                previous_command = command

    genre = sys.argv[1]
    search_by_genre(genre)


if __name__ == "__main__":
    main()
