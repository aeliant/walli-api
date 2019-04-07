"""Regroup all operations related to chains."""
import iptc

from ..utils.exceptions import TableNotFoundException, ChainNotFoundException


def list(table_name):
    """Return all chains for the given table."""
    if table_name not in iptc.Table.ALL:
        raise TableNotFoundException('Table %s does not exists.' % table_name)

    return [_.name for _ in iptc.Table(table_name).chains]

def fetch(table_name, chain_name):
    """Return information about a given chain."""
    if table_name not in iptc.Table.ALL:
        raise TableNotFoundException('Table %s does not exists.' % table_name)

    if chain_name not in [_.name for _ in iptc.Table(table_name).chains]:
        raise ChainNotFoundException(
            'Chain %s does not exists for table %s' % (chain_name, table_name))

    chain = iptc.Chain(iptc.Table(table_name), chain_name)

    return dict(
        policy=chain.get_policy().name if chain.get_policy() else None
    )
