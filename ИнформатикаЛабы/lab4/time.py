import time
from jsonToXMLParcer import parse_json, dump2xml
from jsonToXMLlib import jsonToXMLlib
from jsonToXMLmanually import jsonToXMLmanually
from jsonToXMLregex import jsonToXMLregex


parser = lambda x: dump2xml(parse_json(x))
ref = "C:/Users/utkae/PycharmProjects/json_to_xml/schedule.json"


def test(f, string):
    start_time = time.time()
    for _ in range(100):
        f(string)
    return time.time() - start_time


with open(ref, encoding='utf-8') as f:
    data = f.read()


print(
        f"With Own Parser: {test(parser, data)} seconds",
        f"With Libraries: {test(jsonToXMLlib, ref)} seconds",
        f"Without anything: {test(jsonToXMLmanually, ref)} seconds",
        f"With Regular Expressions: {test(jsonToXMLregex, ref)} seconds",
        sep="\n",
    )

