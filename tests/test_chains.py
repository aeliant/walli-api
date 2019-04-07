"""Functionnal tests for the chains endpoint."""
from config import URL

import docker
import requests
import pytest
import re

REG_CHAIN = re.compile(r'Chain\s+([^\s]*)')

def parse_chains_names(output):
    return REG_CHAIN.findall(output)

def parse_chain_policy(chain_name, output):
    m = re.search(
        r'Chain {chain_name} \(policy\s([^\)]*)\)'.format(
            chain_name=chain_name
        ), output)

    return m.group(1) if m else None

@pytest.mark.filter_table
def test_chains_collection_for_filter_table():
    """Checks validity for the chains collection on the filter table."""
    client = docker.from_env()
    container = client.containers.list()[0]
    chains = parse_chains_names(
        container.exec_run(['iptables', '-t', 'filter', '-L']).output.decode())

    response = requests.get('%s/chains/filter' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert set(chains) == set(response.json())

@pytest.mark.filter_table
def test_chain_item_for_filter_table():
    """Checks validity for the chain item of the filter table."""
    client = docker.from_env()
    container = client.containers.list()[0]

    res = container.exec_run(['iptables', '-t', 'filter', '-L']).output.decode()
    chains = parse_chains_names(res)

    for chain_name in chains:
        response = requests.get('%s/chains/filter/%s' % (URL, chain_name))

        assert 200 == response.status_code
        assert isinstance(response.json(), dict)
        assert 'policy' in response.json()
        assert parse_chain_policy(chain_name, res) == \
            response.json().get('policy')

@pytest.mark.mangle_table
def test_chains_collection_for_mangle_table():
    """Checks validity for the chains collection on the mangle table."""
    client = docker.from_env()
    container = client.containers.list()[0]
    chains = parse_chains_names(
        container.exec_run(['iptables', '-t', 'mangle', '-L']).output.decode())

    response = requests.get('%s/chains/mangle' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert set(chains) == set(response.json())

@pytest.mark.mangle_table
def test_chain_item_for_mangle_table():
    """Checks validity for the chain item of the mangle table."""
    client = docker.from_env()
    container = client.containers.list()[0]

    res = container.exec_run(['iptables', '-t', 'mangle', '-L']).output.decode()
    chains = parse_chains_names(res)

    for chain_name in chains:
        response = requests.get('%s/chains/mangle/%s' % (URL, chain_name))

        assert 200 == response.status_code
        assert isinstance(response.json(), dict)
        assert 'policy' in response.json()
        assert parse_chain_policy(chain_name, res) == \
            response.json().get('policy')

@pytest.mark.raw_table
def test_chains_collection_for_raw_table():
    """Checks validity for the chains collection on the raw table."""
    client = docker.from_env()
    container = client.containers.list()[0]
    chains = parse_chains_names(
        container.exec_run(['iptables', '-t', 'raw', '-L']).output.decode())

    response = requests.get('%s/chains/raw' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert set(chains) == set(response.json())

@pytest.mark.raw_table
def test_chain_item_for_raw_table():
    """Checks validity for the chain item of the raw table."""
    client = docker.from_env()
    container = client.containers.list()[0]

    res = container.exec_run(['iptables', '-t', 'raw', '-L']).output.decode()
    chains = parse_chains_names(res)

    for chain_name in chains:
        response = requests.get('%s/chains/raw/%s' % (URL, chain_name))

        assert 200 == response.status_code
        assert isinstance(response.json(), dict)
        assert 'policy' in response.json()
        assert parse_chain_policy(chain_name, res) == \
            response.json().get('policy')

@pytest.mark.nat_table
def test_chains_collection_for_nat_table():
    """Checks validity for the chains collection on the nat table."""
    client = docker.from_env()
    container = client.containers.list()[0]
    chains = parse_chains_names(
        container.exec_run(['iptables', '-t', 'nat', '-L']).output.decode())

    response = requests.get('%s/chains/nat' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert set(chains) == set(response.json())

@pytest.mark.nat_table
def test_chain_item_for_nat_table():
    """Checks validity for the chain item of the nat table."""
    client = docker.from_env()
    container = client.containers.list()[0]

    res = container.exec_run(['iptables', '-t', 'nat', '-L']).output.decode()
    chains = parse_chains_names(res)

    for chain_name in chains:
        response = requests.get('%s/chains/nat/%s' % (URL, chain_name))

        assert 200 == response.status_code
        assert isinstance(response.json(), dict)
        assert 'policy' in response.json()
        assert parse_chain_policy(chain_name, res) == \
            response.json().get('policy')

@pytest.mark.security_table
def test_chains_collection_for_security_table():
    """Checks validity for the chains collection on the security table."""
    client = docker.from_env()
    container = client.containers.list()[0]
    chains = parse_chains_names(
        container.exec_run(['iptables', '-t', 'security', '-L']).output.decode())

    response = requests.get('%s/chains/security' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert set(chains) == set(response.json())

@pytest.mark.security_table
def test_chain_item_for_security_table():
    """Checks validity for the chain item of the security table."""
    client = docker.from_env()
    container = client.containers.list()[0]

    res = container.exec_run(['iptables', '-t', 'security', '-L']).output.decode()
    chains = parse_chains_names(res)

    for chain_name in chains:
        response = requests.get('%s/chains/security/%s' % (URL, chain_name))

        assert 200 == response.status_code
        assert isinstance(response.json(), dict)
        assert 'policy' in response.json()
        assert parse_chain_policy(chain_name, res) == \
            response.json().get('policy')

@pytest.mark.all_table
def test_chains_collection_for_unknown_table():
    """Checks that a 404 error when an unknown table is requested."""
    response = requests.get('%s/chains/unknown' % URL)

    assert 404 == response.status_code
    assert isinstance(response.json(), dict)
    assert 'message' in response.json()
    assert 'not exist' in response.json().get('message')
