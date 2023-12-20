class Unauthorized(Exception):
    pass

class Forbidden(Exception):
    pass

class BadRequest(Exception):
    pass

class InternalServerError(Exception):
    pass

class NotFound(Exception):
    pass

class BloxlinkError(Exception):
    pass

class UnhandledError(Exception):
    pass

def _raise_error_code(code, message):
    if code == 401:
        raise Unauthorized(message)
    elif code == 403:
        raise Forbidden(message)
    elif code == 404:
        raise NotFound(message)
    elif code == 400:
        raise BadRequest(message)
    elif code == 500:
        raise InternalServerError(message)
    else:
        raise UnhandledError(message)
    
def _raise_error_message(message):
    raise BloxlinkError(message)