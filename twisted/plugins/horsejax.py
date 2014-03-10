from twisted.application.service import ServiceMaker

serviceMaker = ServiceMaker(
    'horsejax', 'horsejax.api',
    'Horsejax API', 'horsejax')
