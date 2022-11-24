from unittest.mock import patch

from django.test import TestCase, override_settings

from .importmap import Importmap


def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def ok():
            return True

        def json(self):
            return self.json_data

    if args[0] == "https://api.jspm.io/generate":
        return MockResponse(
            {
                "staticDeps": [
                    "https://ga.jspm.io/npm:@lit/reactive-element@1.4.1/css-tag.js",
                    "https://ga.jspm.io/npm:@lit/reactive-element@1.4.1/reactive-element.js",
                    "https://ga.jspm.io/npm:lit-element@3.2.2/lit-element.js",
                    "https://ga.jspm.io/npm:lit-html@2.4.0/is-server.js",
                    "https://ga.jspm.io/npm:lit-html@2.4.0/lit-html.js",
                    "https://ga.jspm.io/npm:lit@2.4.0/index.js",
                ],
                "dynamicDeps": [],
                "map": {
                    "imports": {"lit": "https://ga.jspm.io/npm:lit@2.4.0/index.js"},
                    "scopes": {
                        "https://ga.jspm.io/": {
                            "@lit/reactive-element": "https://ga.jspm.io/npm:@lit/reactive-element@1.4.1/reactive-element.js",
                            "lit-element/lit-element.js": "https://ga.jspm.io/npm:lit-element@3.2.2/lit-element.js",
                            "lit-html": "https://ga.jspm.io/npm:lit-html@2.4.0/lit-html.js",
                            "lit-html/is-server.js": "https://ga.jspm.io/npm:lit-html@2.4.0/is-server.js",
                        }
                    },
                },
            },
            200,
        )
    return MockResponse(None, 404)


@patch("requests.post", side_effect=mocked_requests_post)
@override_settings(IMPORTMAP_FILE_PATH="/tmp/importmap.importmap")
class ImportmapTest(TestCase):
    def setUp(self) -> None:
        self.importmap = Importmap()
        return super().setUp()

    def test_add_dependency(self, mocked_post):
        self.importmap.add(["lit"])
        self.assertEqual(
            self.importmap.importmap,
            {
                "imports": {"lit": "https://ga.jspm.io/npm:lit@2.4.0/index.js"},
                "scopes": {
                    "https://ga.jspm.io/": {
                        "@lit/reactive-element": "https://ga.jspm.io/npm:@lit/reactive-element@1.4.1/reactive-element.js",
                        "lit-element/lit-element.js": "https://ga.jspm.io/npm:lit-element@3.2.2/lit-element.js",
                        "lit-html": "https://ga.jspm.io/npm:lit-html@2.4.0/lit-html.js",
                        "lit-html/is-server.js": "https://ga.jspm.io/npm:lit-html@2.4.0/is-server.js",
                    }
                },
            },
        )

    def test_list_dependencies(self, mocked_post):
        self.importmap.add(["lit"])
        self.assertEquals(list(self.importmap.imports()), ['lit@2.4.0'])
