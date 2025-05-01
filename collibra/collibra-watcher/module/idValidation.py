import requests
import logging
import warnings
from api.POST_auth_sessions import POST_auth_sessions
from api.DELETE_auth_sessions_current import DELETE_auth_sessions_current

def idValidation(clbraDomain, usr, psswrd):
    try:
        # Login to a Collibra session.
        response = response_log = POST_auth_sessions(clbraDomain, usr, psswrd)
        response.raise_for_status()

        # Logout from a Collibra session.
        response = response_log = DELETE_auth_sessions_current(clbraDomain, usr, psswrd)
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        warnings.warn(err)
        logging.exception(err)
        logging.info(response_log.json())
        raise SystemExit(err)

    return 1
