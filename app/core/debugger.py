import datetime

from app.settings import DEBUG


class Debugger(object):
    """
    Add [prefix] to print message
    """

    def __init__(self, prefix):
        """
        :param prefix: Prefix to add in front of every message
        """
        self.prefix = None
        self.set_prefix(prefix)
    
    def set_prefix(self, prefix):
        if prefix:
            self.prefix = "[%s]" % str(prefix).replace("][", "|").replace("] [", "|")
        else:
            self.prefix = ""
    
    def log(self, msg, **kwargs):
        msg = "%s %s %s" % (
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            self.prefix,
            msg,
        )
        if DEBUG:
            print(msg)
