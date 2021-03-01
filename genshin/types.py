from datetime import datetime
from urllib.request import Request, urlopen
import ast
import json

from .utils import pretty, Attrify


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 RuxitSynthetic/1.0 v8950574280 t38550 ath9b965f92 altpub cvcv=2'}


class Format:
    def __str__(self) -> str:
        return json.dumps(
            self.__dict__,
            indent=4,
            # sort_keys=True
        )

    def __repr__(self) -> str:
        return self.__str__()


class Types(Format):
    def __init__(
        self,
        results=dict,
        **kwargs
    ):
        self.avaliable = results["types"]

class Artifacts(Format):
    def __init__(
        self,
        results=list,
        **kwargs
    ):
        dic = {}
        for artifact in results:
            req = Request("https://api.genshin.dev/artifacts/"+artifact, headers=headers)
            value = ast.literal_eval(
                json.dumps(
                    json.loads(
                        urlopen(req).read().decode("utf-8"),
                    ),
                )
            )
            dic[artifact] = value
        self.list = Attrify(dic)


class Characters(Format):
    def __init__(
        self,
        results=list,
        **kwargs
    ):
        dic = {}
        for character in results:
            req = Request(
                "https://api.genshin.dev/characters/"+character,
                headers=headers
                )
            value = ast.literal_eval(
                json.dumps(
                    json.loads(
                        urlopen(req).read().decode("utf-8"),
                    ),
                )
            )
            dic[character] = value
        self.list = Attrify(dic)


class Domains(Format):
    def __init__(
        self,
        results=list,
        **kwargs
    ):
        dic = {}
        for domain in results:
            req = Request(
                "https://api.genshin.dev/domains/"+domain,
                headers=headers
                )
            value = ast.literal_eval(
                json.dumps(
                    json.loads(
                        urlopen(req).read().decode("utf-8"),
                    ),
                )
            )
            dic[domain] = value
        self.list = Attrify(dic)


class Elements(Format):
    def __init__(
        self,
        results=list,
        **kwargs
    ):
        dic = {}
        for element in results:
            req = Request(
                "https://api.genshin.dev/elements/"+element,
                headers=headers
                )
            value = ast.literal_eval(
                json.dumps(
                    json.loads(
                        urlopen(req).read().decode("utf-8"),
                    ),
                )
            )
            dic[element] = value
        self.list = Attrify(dic)


class Materials(Format):
    def __init__(
        self,
        results=list,
        **kwargs
    ):
        dic = {}
        for material in results:
            req = Request(
                "https://api.genshin.dev/elements/"+material,
                headers=headers
                )
            value = ast.literal_eval(
                json.dumps(
                    json.loads(
                        urlopen(req).read().decode("utf-8"),
                    ),
                )
            )
            dic[material] = value
        self.list = Attrify(dic)


class Nations(Format):
    def __init__(
        self,
        results=list,
        **kwargs
    ):
        dic = {}
        for nation in results:
            req = Request(
                "https://api.genshin.dev/elements/"+nation,
                headers=headers
                )
            value = ast.literal_eval(
                json.dumps(
                    json.loads(
                        urlopen(req).read().decode("utf-8"),
                    ),
                )
            )
            dic[nation] = value
        self.list = Attrify(dic)


class Weapons(Format):
    def __init__(
        self,
        results=list,
        **kwargs
    ):
        dic = {}
        for weapon in results:
            req = Request(
                "https://api.genshin.dev/elements/"+weapon,
                headers=headers
                )
            value = ast.literal_eval(
                json.dumps(
                    json.loads(
                        urlopen(req).read().decode("utf-8"),
                    ),
                )
            )
            dic[weapon] = value
        self.list = Attrify(dic)