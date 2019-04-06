"""Regroup all operations related to tables."""
import iptc


def fetch():
    """Return all registred tables."""
    return iptc.Table.ALL
