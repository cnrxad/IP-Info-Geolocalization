import ipinfo
import socket
import webbrowser
from types import SimpleNamespace
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from colorama import Fore, Back, Style, init

try:
    import pyperclip
    HAS_PYPERCLIP = True
except Exception:
    HAS_PYPERCLIP = False

try:
    from ipwhois import IPWhois
    HAS_IPWHOIS = True
except Exception:
    HAS_IPWHOIS = False

init(autoreset=True)

ACCESS_TOKEN = "5d24aff3325639"  # usa tu token si quieres

def flag_emoji(country_code: str) -> str:
    if not country_code or len(country_code) != 2:
        return ""
    return chr(ord(country_code[0].upper()) - 65 + 0x1F1E6) + chr(ord(country_code[1].upper()) - 65 + 0x1F1E6)

def print_header():
    width = 78
    top = "╔" + "═" * width + "╗"
    print(Fore.MAGENTA + top)
    print(Fore.MAGENTA + "║" + " " * width + "║")
    # centered title
    title = "✿  KN IP-INFO  ✿"
    print(Fore.MAGENTA + "║" + title.center(width) + "║")
    print(Fore.MAGENTA + "║" + " " * width + "║")
    print(Fore.MAGENTA + "╚" + "═" * width + "╝")
    print()

def print_card(details):
    flag = flag_emoji(details.country) if getattr(details, "country", "") else ""
    asn = ""
    isp = ""
    if getattr(details, "org", None):
        parts = details.org.split(" ", 1)
        if parts:
            asn = parts[0]
            isp = parts[1] if len(parts) > 1 else ""
    lat, lon = ("", "")
    if getattr(details, "loc", None):
        try:
            lat, lon = details.loc.split(",")
        except Exception:
            lat, lon = details.loc, ""
    local_time = "(timezone no disponible)"
    if getattr(details, "timezone", None):
        try:
            tz = ZoneInfo(details.timezone)
            local_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
        except ZoneInfoNotFoundError:
            local_time = "(zona horaria desconocida)"

    border = "┌" + "─" * 60 + "┐"
    print(Fore.CYAN + border)
    print(Fore.CYAN + f"│ IP: {getattr(details, 'ip', '')}".ljust(60) + " │")
    print(Fore.CYAN + f"│ Hostname: {getattr(details, 'hostname', '')}".ljust(60) + " │")
    print(Fore.CYAN + f"│ País: {getattr(details, 'country', '')} {flag}".ljust(60) + " │")
    print(Fore.CYAN + f"│ Ciudad/Region: {getattr(details, 'city','')} / {getattr(details,'region','')}".ljust(60) + " │")
    print(Fore.CYAN + f"│ Coordenadas: {lat} , {lon}".ljust(60) + " │")
    print(Fore.CYAN + f"│ ASN: {asn}    ISP: {isp}".ljust(60) + " │")
    print(Fore.CYAN + f"│ Postal: {getattr(details, 'postal', '')}    TZ: {getattr(details, 'timezone','')}".ljust(60) + " │")
    print(Fore.CYAN + f"│ Hora local en IP: {local_time}".ljust(60) + " │")
    print(Fore.CYAN + "└" + "─" * 60 + "┘")
    print()

def safe_get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return ""

def make_details_for_empty():
    return SimpleNamespace(
        ip="",
        hostname="",
        city="",
        region="",
        country="",
        loc="",
        org="",
        postal="",
        timezone="",
    )

def prompt_open_map(details):
    if not getattr(details, "loc", ""):
        print(Fore.YELLOW + "No hay coordenadas para abrir en Maps.")
        return
    latlon = details.loc
    url = f"https://www.google.com/maps/@{latlon},15z"
    print(Fore.GREEN + "Abriendo Google Maps en el navegador...")
    webbrowser.open(url)

def summary_text(details) -> str:
    latlon = details.loc or ""
    parts = [
        f"IP: {details.ip}",
        f"Host: {getattr(details,'hostname','')}",
        f"Location: {getattr(details,'city','')}, {getattr(details,'region','')} ({getattr(details,'country','')})",
        f"Coords: {latlon}",
        f"ISP/ASN: {getattr(details,'org','')}",
        f"Timezone: {getattr(details,'timezone','')}",
    ]
    return " | ".join(p for p in parts if p)

def do_ip_whois(ip):
    """
    Perform IP WHOIS using ipwhois if available.
    Returns a short summary string (or error message).
    """
    if not HAS_IPWHOIS:
        return "(ipwhois no instalado; instala 'ipwhois' para WHOIS de IPs)"
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap(asn_methods=["whois", "http"])
        # Extract useful fields safely
        asn = res.get("asn", "")
        asn_country = res.get("asn_country_code", "")
        asn_registry = res.get("asn_registry", "")
        network = res.get("network", {}) or {}
        net_name = network.get("name", "")
        net_cidr = network.get("cidr", "")
        net_country = network.get("country", "")
        entities = res.get("entities", [])
        # Build readable summary
        lines = [
            f"ASN: {asn} ({asn_registry})",
            f"ASN country: {asn_country}",
            f"Network: {net_name} {net_cidr} ({net_country})",
        ]
        if entities:
            lines.append(f"Entities: {', '.join(entities[:5])}")
        return "\n".join(lines)
    except Exception as e:
        return f"(error en WHOIS: {e})"

print_header()

ip_address = input(Fore.YELLOW + "ingrese la dirección IP: ").strip()
print()

if not ip_address:
    print(Fore.RED + "tienes que proporcionar una ip (pero igual muestro la tarjeta con campos vacíos).")
    details = make_details_for_empty()
else:
    handler = ipinfo.getHandler(ACCESS_TOKEN)
    try:
        details = handler.getDetails(ip_address)
        if not getattr(details, "hostname", ""):
            details.hostname = safe_get_hostname(ip_address)
    except Exception as e:
        print(Fore.RED + f"No se pudo conectar a ipinfo: {e}")
        details = make_details_for_empty()
        details.ip = ip_address
        details.hostname = safe_get_hostname(ip_address)

print_card(details)

while True:
    options_line = "Opciones: [m] abrir Maps  [c] copiar resumen  [s] guardar en last_ip.txt  [w] whois  [q] salir"
    print(Fore.MAGENTA + options_line)
    choice = input(Fore.YELLOW + "→ ").strip().lower()
    if choice == "m":
        prompt_open_map(details)
    elif choice == "c":
        text = summary_text(details)
        if HAS_PYPERCLIP:
            pyperclip.copy(text)
            print(Fore.GREEN + "Resumen copiado al portapapeles.")
        else:
            print(Fore.RED + "pyperclip no instalado — aquí está el resumen:\n" + text)
    elif choice == "s":
        try:
            with open("last_ip.txt", "w", encoding="utf-8") as f:
                f.write(getattr(details, "ip", "") or "")
            print(Fore.GREEN + "IP guardada en last_ip.txt")
        except Exception as e:
            print(Fore.RED + f"No se pudo guardar: {e}")
    elif choice == "w":
        ip_for_whois = getattr(details, "ip", "") or ip_address
        if not ip_for_whois:
            print(Fore.RED + "No hay IP para WHOIS.")
        else:
            print(Fore.YELLOW + f"Realizando WHOIS para {ip_for_whois} ...")
            whois_result = do_ip_whois(ip_for_whois)
            print(Fore.GREEN + "=== WHOIS (resumen) ===")
            print(Fore.RESET + whois_result)
            print(Fore.GREEN + "=======================")
    elif choice == "q":
        break
    else:
        print(Fore.RED + "opción inválida. pulsa m/c/s/w/q")

print(Fore.CYAN + "✿ fin")

