def jsonToXMLlib(ref):
    import xmltodict
    import simplejson as json1
    with open(ref, encoding='utf-8') as f:
        data = json1.load(f)
    data = {'root': data}
    xml_string = xmltodict.unparse(data, pretty=True)
    return xml_string
