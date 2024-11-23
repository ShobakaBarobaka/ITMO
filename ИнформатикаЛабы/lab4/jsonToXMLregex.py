def jsonToXMLregex(ref):
    import re

    with open(ref, encoding='utf-8') as f:
        s = f.read()

    s = "<root>" + s[1:-1] + "</root>"
    objName = r'".+?": '
    objNames = re.findall(objName, s)
    tags = ["<" + x[1:-3] + ">" for x in objNames]
    for i in range(len(tags)):
        s = s.replace(objNames[i], tags[i], 1)

    content = r'<.+?>\".+?\"\,*\n|<.+?>\d+\,*\n|<.+?>true\,*\n|<.+?>false\,*\n|<.+?>none\,*\n'
    contents = re.findall(content, s)
    for i in range(len(contents)):
        s = s.replace(contents[i], contents[i][:-2] + "</" + contents[i][1:contents[i].index(">") + 1] + "\n", 1)

    s = s.replace("{", "")
    s = s.replace("}", "")

    strings = s.split("\n")

    for k in range(1, len(strings)):
        onlyTag = r'\s*<[^/]+?>\s*'
        if re.fullmatch(onlyTag, strings[k]):
            for m in range(k, len(strings)):
                if re.fullmatch(r'\s*,\s*', strings[m]):
                    strings[m] = re.sub(r',', "</" + strings[k].strip()[1:-1] + ">", strings[m])
                    break
    for st in strings:
        if len(st.strip()) == 0:
            strings.remove(st)

    insertion = None
    for k in range(1, len(strings)):
        openArrTag = r'\s*<[^/]+?>\[\s*'
        if re.fullmatch(openArrTag, strings[k]):
            stst = strings[k].strip()
            tabs = len(strings[k][:strings[k].index("<")])
            strings[k] = strings[k][:-1]
            for w in range(k, len(strings)):
                stst1 = strings[w].strip()
                if stst1 == "]":
                    tabs1 = len(strings[w][:strings[w].index("]")])
                    if tabs == tabs1:
                        strings[w] = strings[w].replace("]", "\t" + "</" + stst[1:-1])
                        insertion = w
                        break
            for w2 in range(k, insertion):
                stst2 = strings[w2].strip()
                if stst2 == ",":
                    tabs2 = len(strings[w2][:strings[w2].index(",")])
                    if tabs2 == tabs + 4:
                        strings[w2] = strings[w2].replace(",", "</" + stst[1:-1])
                        strings.insert(w2 + 1, " " * tabs2 + stst[:-1])

    almxml = "\n".join(strings)
    almxml = almxml.replace("\"", "")
    almxml = re.sub(r'(\W)(\s+)(\W)', r'\1\3', almxml)

    return almxml
