import json
import re, os
from typing import Dict, Iterable

import requests
from django.conf import settings


class Importmap:
    def __init__(self) -> None:
        with open(settings.IMPORTMAP_FILE_PATH, 'a+', encoding="utf-8") as file:
            file.seek(0, os.SEEK_END)
            if file.tell():
                file.seek(0)
                self._importmap = json.loads(file.read())
            else:
                self._importmap = {'imports': {}}

    @property
    def importmap(self) -> Dict:
        return self._importmap

    def imports(self) -> Iterable:
        for key, value in self._importmap['imports'].items():
            result = re.search(r"""(?P<registry>https://.*?):(?P<name>.*)@(?P<version>.*?)/(?P<subpath>.*)""", value)
            if key == f'{result.group("name")}/{result.group("subpath")}':
                yield f'{result.group("name")}@{result.group("version")}/{result.group("subpath")}'
            else:
                yield f'{result.group("name")}@{result.group("version")}'

    def add(self, names) -> None:
        install = [*self.imports(), *names]
        response = requests.post("https://api.jspm.io/generate", data=json.dumps({
            "install": install,
            "env": [
                "browser",
                "production",
                "module"
            ]
        }))
        if response.ok:
            self._importmap = response.json()['map']
            with open(settings.IMPORTMAP_FILE_PATH, 'w', encoding="utf-8") as file:
                json.dump(self._importmap, file, indent=2)
