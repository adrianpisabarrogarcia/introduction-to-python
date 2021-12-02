programm_langauges = ["JS", "Python", "PHP", "Ruby"]
text = "Hoy en día, los lenguajes de programación más utilizados son: "
for language in programm_langauges:
    if language == programm_langauges[-1]:
        text += " y " + language
    elif language == programm_langauges[-2]:
        text += language
    else:
        text += language + ", "


print(text)
