def jsonToXMLmanually(ref):
    with open(ref, encoding='utf-8') as f:
        s = f.read()

    s = "<root>" + s[1:-1] + "</root>"
    for x in range(len(s) + 200):
        # replace object names with opening tags
        if s[x] == '\"':  # searching for an opening quote as start of object name
            for i in range(x + 1, len(s)):
                if s[i].isspace():  # checking is text after quote is object name
                    break
                else:
                    if s[i:i + 2] == "\":":
                        tag = s[x + 1:i]
                        s = s.replace(s[x:i + 3], '<' + tag + '>', 1)
                        k = 0
                        for n in range(i + 1, len(s)):
                            if s[n] != "\n":
                                k += 1
                            else:
                                if s[i + k] == ",":
                                    content = s[i + 1: i + k]  # после открывающего тега
                                    if len(content) != 0 and (content.isdigit() or
                                                              (content[0] == "\"" and content[-1] == "\"")
                                                              or content == "true" or content == "false"):
                                        s = s[:i + k] + "</" + tag + ">" + s[i + k + 1:]
                                        break
                                else:
                                    content = s[i + 1: i + k + 1]  # после открывающего тега
                                    if len(content) != 0 and (
                                            content.isdigit() or (content[0] == "\"" and content[-1] == "\"")
                                            or content == "true" or content == "false"):
                                        s = s[:i + k + 1] + "</" + tag + ">" + s[i + k + 1:]
                                        break
                                break
                        break


    s = s.replace("{", "")
    s = s.replace("}", "")


    strings = s.split("\n")

    for k in range(1, len(strings)):
        stst = strings[k].strip()
        if len(stst) != 0:
            if stst[0] == "<" and stst[-1] == ">" and stst.count("<") == 1 and stst.count(">") == 1 and "/" not in stst:
                for m in range(k, len(strings)):
                    if strings[m].strip() == ",":
                        strings[m] = strings[m].replace(",", "</" + strings[k].strip()[1:-1] + ">", 1)
                        break
    for st in strings:
        if len(st.strip()) == 0:
            strings.remove(st)

    insertion = None
    for k in range(1, len(strings)):
        stst = strings[k].strip()
        if len(stst) >= 2:
            if stst[0] == "<" and stst[-2:] == ">[":
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


    isShift = [0] * len(strings)
    numberOfTabs = [0] * len(strings)

    for i in range(1, len(strings)):
        prevstrp = strings[i - 1].strip()
        curstrp = strings[i].strip()
        spacesprev = len(strings[i - 1]) - len(prevstrp)  # number of leading spaces in previous line
        spacesthis = len(strings[i]) - len(curstrp)  # number of leading spaces in current line
        shift = spacesprev - spacesthis
        if shift < 0:
            isShift[i] = 1
        if shift > 0:
            isShift[i] = -1

    for i in range(1, len(strings) - 1):
        if isShift[i] == 1:
            numberOfTabs[i] = numberOfTabs[i-1] + 1
        if isShift[i] == 0:
            numberOfTabs[i] = numberOfTabs[i-1]
        if isShift[i] == -1:
            numberOfTabs[i] = numberOfTabs[i-1] - 1

    for i in range(len(strings)):
        strings[i] = strings[i].strip()

    for i in range(len(strings)):
        strings[i] = "\t" * numberOfTabs[i] + strings[i]

    almxml = "\n".join(strings)
    almxml = almxml.replace("\"", "")

    return almxml


