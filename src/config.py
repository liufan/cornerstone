import ConfigParser
from os.path import expanduser, join
import logging

log = logging.getLogger(__name__)


def config():
    home = expanduser("~")
    config_file = join(home, '.op_site')

    cf = ConfigParser.ConfigParser()
    cf.read(config_file)
    return cf
