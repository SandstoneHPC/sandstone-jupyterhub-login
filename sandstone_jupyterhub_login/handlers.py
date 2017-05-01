from sandstone.lib.handlers.base import BaseHandler
from sandstone import settings
import requests
import os

class JupyterHubLoginHandler(BaseHandler):
    def get(self):
        # The XSRF token must be manually set in the absence of
        # a web form. Accessing the property is enough to set it.
        self.xsrf_token

        api_token = os.environ['JUPYTERHUB_API_TOKEN']
        hub_api_url = os.environ['JUPYTERHUB_API_URL']

        url = '{hub_url}/authorizations/token/{token}'.format(
            hub_url=hub_api_url,
            token=api_token
        )

        # Has user deconfigured certificate verification?
        verify = getattr(settings,'VERIFY_JH_CERT',True)

        res = requests.get(
            url,
            headers={
                'Authorization': 'token %s' % api_token
            },
            verify=verify
        )


        username = res.json()['name']

        if username:
            self.set_secure_cookie('user', username)
            self.redirect('/user/{}'.format(username))
        else:
            self.set_status(403)
            self.redirect(self.get_login_url())


class JupyterHubLogoutHandler(BaseHandler):
    def get(self):
        # clear the user cookie
        self.clear_cookie('user')
        self.clear_cookie('_xsrf')

        # redirect to hub home
        self.set_status(302)
        self.redirect('/hub/home')
