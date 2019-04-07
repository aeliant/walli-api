"""Regroup all operations related to chains."""
import iptc

from ..utils.exceptions import TableNotFoundException


def fetch(table_name):
    """Return all chains for the given table."""
    if table_name not in iptc.Table.ALL:
        raise TableNotFoundException('Table %s does not exists.' % table_name)

    return [_.name for _ in iptc.Table(table_name).chains]
