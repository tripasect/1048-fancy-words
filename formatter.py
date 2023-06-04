origin = open("DEF.txt")
body = origin.read()
definitions = [i.strip() for i in body.split('\n\n\n')]


"""
aberration | ˌabəˈrāSH(ə)n |
noun
a departure from what is normal, usual, or expected, typically one that is unwelcome: they described the outbreak of violence in the area as an aberration | I see these activities as some kind of mental aberration | [mass noun] : the decade was seen as a period of aberration in the country's progress towards a democratic society.
• Biology a characteristic that deviates from the normal type: color aberrations.
• Optics the failure of rays to converge at one focus because of limitations or defects in a lens or mirror.
• Astronomy the apparent displacement of a celestial object from its true position, caused by the relative motion of the observer and the object.
DERIVATIVES
aberrational | -SHənl | adjective
ORIGIN
late 16th century: from Latin aberratio(n-), from aberrare ‘to stray’ (see aberrant).
"""


def s(entry):
    lines = entry.split("\n")
    word = lines[0].split()[0]
    phonetic = '| ' + lines[0].split(" | ")[1][:-2] + ' |'
    fos = lines[1]
    definition = ''
    for line in lines[2:]:
        definition += line
        definition += "\n"
    entry = (word, phonetic, fos, definition)
    body = ""
    body += "**" + entry[0] + "**" + "    " + entry[1]
    body += "<br>\n"
    body += "*" + entry[2] + "*"
    body += "<br>\n"
    body += entry[3]
    return body


target = open('final.md', 'w')
for d in definitions:
    try:
        target.write(s(d))
    except IndexError:
        pass
    target.write("\n\n")

target.close()
