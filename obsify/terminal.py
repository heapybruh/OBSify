import colorama
import cursor

colorama.init(autoreset=True, strip=True, convert=True)
cursor.hide()

class Terminal():
    def print(message):
        print(f"[ OBSify ] {message}")

    def success(message):
        print(f"[ OBSify ] {Colors.green + message + Colors.reset}")

    def error(message):
        print(f"[ OBSify ] {Colors.red + message + Colors.reset}")

    def how_to_use():
        print(f"\nHow to use?\n" +
        "1) Open OBS\n" +
        "2) Add \"Broswer\" source to your scene\n" +
        "3) Right click on the source and open \"Properties\"\n" +
        "4) Check \"Local file\"\n" +
        "5) Click \"Browse\" and select the HTML file which is in \"./html/index.html\"\n" +
        "6) Done!\n")

class Colors:
    green = colorama.Fore.GREEN
    red = colorama.Fore.RED
    reset = colorama.Fore.RESET