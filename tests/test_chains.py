"""Functionnal tests for the chains endpoint."""
from config import URL

import docker
import requests
import pytest
import re

REG = re.compile(r'Chain\s+([^\s]*)')

def parse_chains(output):
    return REG.findall(output)

@pytest.mark.filter_table
def test_chains_collection_for_filter_table():
    """Checks validity for the chains collection on the filter table."""
    client = docker.from_env()
    container = client.containers.list()[0]
    chains = parse_chains(
        container.exec_run('iptables -t filter -L').output.decode())

    response = requests.get('%s/chains/filter' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert set(chains) == set(response.json())

@pytest.mark.mangle_table
def test_chains_collection_for_mangle_table():
    """Checks validity for the chains collection on the mangle table."""
    client = docker.from_env()
    container = client.containers.list()[0]
    chains = parse_chains(
        container.exec_run('iptables -t mangle -L').output.decode())

    response = requests.get('%s/chains/mangle' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert set(chains) == set(response.json())

@pytest.mark.raw_table
def test_chains_collection_for_raw_table():
    """Checks validity for the chains collection on the raw table."""
    client = docker.from_env()
    container = client.containers.list()[0]
    chains = parse_chains(
        container.exec_run('iptables -t raw -L').output.decode())

    response = requests.get('%s/chains/raw' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert set(chains) == set(response.json())

@pytest.mark.nat_table
def test_chains_collection_for_nat_table():
    """Checks validity for the chains collection on the nat table."""
    client = docker.from_env()
    container = client.containers.list()[0]
    chains = parse_chains(
        container.exec_run('iptables -t nat -L').output.decode())

    response = requests.get('%s/chains/nat' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert set(chains) == set(response.json())

@pytest.mark.security_table
def test_chains_collection_for_security_table():
    """Checks validity for the chains collection on the security table."""
    client = docker.from_env()
    container = client.containers.list()[0]
    chains = parse_chains(
        container.exec_run('iptables -t security -L').output.decode())

    response = requests.get('%s/chains/security' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert set(chains) == set(response.json())

@pytest.mark.all_table
def test_chains_collection_for_unknown_table():
    """Checks that a 404 error when an unknown table is requested."""
    response = requests.get('%s/chains/unknown' % URL)

    assert 404 == response.status_code
    assert isinstance(response.json(), dict)
    assert 'message' in response.json()
    assert 'not exist' in response.json().get('message')
