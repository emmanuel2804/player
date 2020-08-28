import random

channel_id = -1001446514035

def unpack_info():
    pass

#return a dictionary with the report info
def parse_report(text):
    report = {}
    lines = []
    lines = text.splitlines()
    

#return a list of strings, [guildTag,playerName,atk,def,lvl]    
def __get_basics__(line):
    basics = []
    basics = line.split()


def parse_guild_deflist(text):
    result = ""
    lines = text.splitlines()
    g_name = get_gname_from_line(lines[0])
    result += g_name + " Total Defence:\n"
    result += "\t🛡"
    total = get_total(lines)
    result += total.__str__()
    return result

def parse_guild_atklist(text):
    result = ""
    lines = text.splitlines()
    g_name = get_gname_from_line(lines[0])
    result += g_name + " Total Attack:\n"
    result += "\t\u2694"
    total = get_total(lines)
    result += total.__str__()
    return result

def roster_encode(text):
    Roster = {}
    
    return Roster

def get_gname_from_line(line):
    result = []
    result = line.rsplit(maxsplit=2)
    return result[0]

def get_total(lines):
    total = 0
    for line in lines:
        if(line[0] == '#'):
            items = line.split()
            number = get_number_str(items[1])
            if(number.isdecimal()):
                total += (int)(number)
            else:
                print('Error')
    return total

#separa un icono del numero ex: (icono)number -> number
def get_number_str(text):
    number = ""
    i = 1
    l = len(text)
    while(i<l):
        number += text[i]
        i += 1
    return number

def get_quest(q):
    if q == 'f':
        return 0
    elif q == 's':
        return 1
    elif q == 'v':
        return 2
    elif q == 'r':
        return random.randint(0, 2)

    return random.randint(0, 2)

###
### Testing Utils functionalities
###

# text = "🦈Digital OCean Defence Rating\n#1 🛡201 Adolf Hitler\n#2 🛡188 L Da Vinci\n#3 🛡134 Clyde\n#4 🛡125 GhostRanger\n#5 🛡117 EAVO DIAMOND\n#6 🛡104 Jack the Ripper\n#7 🛡99 Sundance Kid\n#8 🛡99 Anvil_Master\n#9 🛡89 Mata Hari"
# result = parse_guild_deflist(text)
# print(result)