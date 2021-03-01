class Error(Exception):
    pass


class UnknownError(Error):
    pass


class GenshinError(Error):
    pass


class HostDownError(Error):
    pass