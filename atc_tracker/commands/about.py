from colorama import init, Fore, Back

init(autoreset=True)

def about():
    print(f"Project developed and maintained by {Fore.BLACK}{Back.WHITE}Luckyluka17")
    print(f"Special thanks to {Fore.BLACK}{Back.WHITE}Polo228{Fore.RESET}{Back.RESET} for his knowledge of aeronautics\n")
    print("Documentation: https://luckyluka17.github.io/atc_tracker")
    print("Donation: https://buymeacoffee.com/Luckyluka17")
    print("API used: https://github.com/JeanExtreme002/FlightRadarAPI")