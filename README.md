# sandstone-jupyterhub-login
Use JupyterHub as a multi-user spawner for Sandstone IDE

## Installation
Install the Python module to your Sandstone IDE environment first
```
python setup.py install
```

Then modify your Sandstone IDE configuration to use the Sandstone JupyterHub Login handler, and to pull the URL prefix from the environment.
```python
import os

LOGIN_HANDLER = 'sandstone_jupyterhub_login.handlers.JupyterHubLoginHandler'

URL_PREFIX = os.environ.get('SANDSTONE_PREFIX', '')
```

JupyterHub can now invoke Sandstone IDE by running
```
<sandstone-python-path>/bin/sandstone-jupyterhub
```
