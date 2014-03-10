from haddock.api import API, DefaultServiceClass
from twisted.application import strports
from twisted.python import usage
from twisted.web import server
from pkg_resources import resource_string

import horsephrase
import json



class horsejaxAPI(object):
    class v1(object):
        def generate_GET(self, request, params):
            """
            Generate a password with Glyph's horsephrase.
            """
            length = params.get("length", 4)
            return {"password": horsephrase.generate(length)}



class Options(usage.Options):
    optParameters = [
        ["port", "p", "8064"]
    ]

def makeService(options):
    """
    Make a service.

    @param options: The option parameters.
    @return: A service.
    """

    config = resource_string(__name__, "api.json").decode("utf-8")

    APIService = API(
        horsejaxAPI, json.loads(config))

    site = server.Site(APIService.getResource())
    return strports.service(options['port'], site)
