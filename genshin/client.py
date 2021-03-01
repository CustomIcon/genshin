from urllib.request import Request, urlopen
import json
from typing import Optional
from urllib import error
import ast

from .errors import UnknownError, GenshinError, HostDownError
from .types import Types, Artifacts, Characters, Domains, Elements, Materials, Nations, Weapons

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 RuxitSynthetic/1.0 v8950574280 t38550 ath9b965f92 altpub cvcv=2'}

class Client:
    def __init__(
        self,
        *,
        host: str = "https://api.genshin.dev",
        path: Optional[str] = None,
        headers: dict = headers
    ) -> None:
        self._host = host
        self._path = path
        self._headers = headers
    def do_req(self, path):
        if path:
            req = Request(self._host + "/" + path, headers=self._headers)
        else:
            req = Request(self._host, headers=self._headers)
        return ast.literal_eval(
            json.dumps(
                json.loads(
                    urlopen(req).read().decode("utf-8"),
                ),
                sort_keys=True,
                indent=4
            )
        )

    def get_types(
        self,
    ):
        try:
            req = self.do_req(path=None)
            return Types(req)
        except error.HTTPError as e:
            raise UnknownError(e)

    def get_artifacts(self,):
        try:
            req = self.do_req(path="artifacts")
            return Artifacts(req)
        except error.HTTPError as e:
            raise UnknownError(e)
        except error.URLError as e:
            raise HostDownError(e)

    def get_characters(self):
        try:
            req = self.do_req(path="characters")
            return Characters(req)
        except error.HTTPError as e:
            raise UnknownError(e)
        except error.URLError as e:
            raise HostDownError(e)

    def get_domains(self):
        try:
            req = self.do_req(path="domains")
            return Domains(req)
        except error.HTTPError as e:
            raise UnknownError(e)
        except error.URLError as e:
            raise HostDownError(e)

    def get_elements(self):
        try:
            req = self.do_req(path="elements")
            return Elements(req)
        except error.HTTPError as e:
            raise UnknownError(e)
        except error.URLError as e:
            raise HostDownError(e)

    def get_materials(self):
        try:
            req = self.do_req(path="materials")
            return Materials(req)
        except error.HTTPError as e:
            raise UnknownError(e)
        except error.URLError as e:
            raise HostDownError(e)

    def get_nations(self):
        try:
            req = self.do_req(path="nations")
            return Nations(req)
        except error.HTTPError as e:
            raise UnknownError(e)
        except error.URLError as e:
            raise HostDownError(e)

    def get_weapons(self):
        try:
            req = self.do_req(path="weapons")
            return Weapons(req)
        except error.HTTPError as e:
            raise UnknownError(e)
        except error.URLError as e:
            raise HostDownError(e)



