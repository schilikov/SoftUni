from pyfiglet import figlet_format


def print_art(msg):
    print(figlet_format(msg))


print_art(input())