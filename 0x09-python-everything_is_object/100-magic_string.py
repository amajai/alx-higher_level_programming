s = ""
def magic_string():
    global s; s += "BestSchool" if not s else ", BestSchool"
    return s
