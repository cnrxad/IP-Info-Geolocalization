# cnrxad puto amo

import ipinfo
from colorama import Fore, Back, Style, init

init(autoreset=True)

ip_address = input(Fore.YELLOW + "ingrese la dirección IP: ")
access_token = "5d24aff3325639"  # este es el mío pero puede usar el tuyo propio, https://ipinfo.io/signup

handler = ipinfo.getHandler(access_token)
details = handler.getDetails(ip_address)


if ip_address == "":
    print(Fore.RED + "tienes que proporcionar una ip")
else:
    print(Fore.RESET + " ")
    print(
        Fore.RESET
        + "   _,.----.    .-._                                ,-.--,    ,---.                    "
    )
    print(
        Fore.RESET
        + " .' .' -   \  /==/ \  .-._    .-.,.---.   .--.-.  /=/, .'  .--.'  \       _,..---._   "
    )
    print(
        Fore.RESET
        + "/==/  ,  ,-'  |==|, \/ /, /  /==/  `   \  \==\ -\/=/- /    \==\-/\ \    /==/,   -  \  "
    )
    print(
        Fore.RESET
        + "|==|_   `-' \ |==| ,  | -|  |==|   '='  /   |==|,  - |     \==\,   - \  |==|  .=.   | "
    )
    print(
        Fore.RESET
        + "|==|   _  , | |==| -   _ |  |==|- ,   .'   /==/   ,   \    /==/ -   ,|  |==|,|   | -| "
    )
    print(
        Fore.RESET
        + "\==\.       / |==|  /\ , |  |==|_  . ,'.  /==/, .--, - \  /==/-  /\ - \ |==|  '='   / "
    )
    print(
        Fore.RESET
        + " `-.`.___.-'  /==/, | |- |  /==/  /\ ,  ) \==\- \/=/ , /  \==\ _.\=\.-' |==|-,   _`/  "
    )
    print(
        Fore.RESET
        + "              `--`./  `--`  `--`-`--`--'   `--`-'  `--`    `--`         `-.`.____.'   "
    )
    print(
        Fore.RESET
        + "--------------------------------------------------------------------------------------"
    )
    print(Fore.RESET + " ")
    print(Fore.RESET + f"IP: {details.ip}")
    print(Fore.RESET + f"ciudad: {details.city}")
    print(Fore.RESET + f"región: {details.region}")
    print(Fore.RESET + f"país: {details.country}")
    print(Fore.RESET + f"coordenadas: {details.loc}")

    print(" ")

    while True:
        entrada = input(Fore.YELLOW + "¿deseas saber más información? - y/n:").lower()

        if entrada == "y":
            print(Fore.RESET + " ")
            print(
                Fore.RESET
                + "   _,.----.    .-._                                ,-.--,    ,---.                    "
            )
            print(
                Fore.RESET
                + " .' .' -   \  /==/ \  .-._    .-.,.---.   .--.-.  /=/, .'  .--.'  \       _,..---._   "
            )
            print(
                Fore.RESET
                + "/==/  ,  ,-'  |==|, \/ /, /  /==/  `   \  \==\ -\/=/- /    \==\-/\ \    /==/,   -  \  "
            )
            print(
                Fore.RESET
                + "|==|_   `-' \ |==| ,  | -|  |==|   '='  /   |==|,  - |     \==\,   - \  |==|  .=.   | "
            )
            print(
                Fore.RESET
                + "|==|   _  , | |==| -   _ |  |==|- ,   .'   /==/   ,   \    /==/ -   ,|  |==|,|   | -| "
            )
            print(
                Fore.RESET
                + "\==\.       / |==|  /\ , |  |==|_  . ,'.  /==/, .--, - \  /==/-  /\ - \ |==|  '='   / "
            )
            print(
                Fore.RESET
                + " `-.`.___.-'  /==/, | |- |  /==/  /\ ,  ) \==\- \/=/ , /  \==\ _.\=\.-' |==|-,   _`/  "
            )
            print(
                Fore.RESET
                + "              `--`./  `--`  `--`-`--`--'   `--`-'  `--`    `--`         `-.`.____.'   "
            )
            print(
                Fore.RESET
                + "--------------------------------------------------------------------------------------"
            )
            print(Fore.RESET + " ")

            print(Fore.RESET + f"compañía: {details.org}")
            print(Fore.RESET + f"código postal: {details.postal}")
            print(Fore.RESET + f"zona horaria: {details.timezone}")
            print(
                Fore.RESET + f"google maps: https://www.google.com/maps/@{details.loc}"
            )
            print(Fore.RESET + f"vista detallada: https://ipinfo.io/{details.ip}")
            print(Fore.RESET + " ")
            break
        elif entrada == "n":
            break
        else:
            print(Fore.RED + "pulsa y/n!")

