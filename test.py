# ANSI escape codes for text colors
class TextColors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

# ANSI escape codes for background colors
class BackgroundColors:
    RESET = "\033[0m"
    BLACK = "\033[40m"
    RED = "\033[41m"
    GREEN = "\033[42m"
    YELLOW = "\033[43m"
    BLUE = "\033[44m"
    MAGENTA = "\033[45m"
    CYAN = "\033[46m"
    WHITE = "\033[47m"

if __name__ == "__main__":
    print(TextColors.RED + "This text is red." + TextColors)
    print(TextColors.GREEN + "This text is green." + TextColors.RESET)
    print(TextColors.YELLOW + "This text is yellow." + TextColors.RESET)
    print(TextColors.BLUE + "This text is blue." + TextColors.RESET)
    print(TextColors.MAGENTA + "This text is magenta." + TextColors.RESET)
    print(TextColors.CYAN + "This text is cyan." + TextColors.RESET)

    # You can combine text colors and background colors
    print(TextColors.RED + BackgroundColors.YELLOW + "Red text on yellow background." + TextColors.RESET + BackgroundColors.RESET)
