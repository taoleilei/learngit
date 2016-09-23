from Infrastructure.Core.HttpRequest import BaseRequestHandler
from UIAdmin import Config
import os


class AdminRequestHandler(BaseRequestHandler):
    """docstring for AdminRequestHandler"""

    def render(self, template_name, **kwargs):
        if Config.base_template_path:
            template_name = os.path.join(Config.base_template_path, template_name)
        super(BaseRequestHandler, self).render(template_name, **kwargs)
