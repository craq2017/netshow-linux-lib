# disable docstring checking
# pylint: disable=C0111
# disable checking no-self-use
# pylint: disable=R0201
# pylint: disable=W0212
# disable invalid name
# pylint: disable=C0103
from asserts import assert_equals
import netshowlib.linux.common as common

# # Tests for common.py

def test_sort_ports():
    ports = ['vlan115', 'swp1', 'vlan115-v0', 'BondQObb', 'swp46.21', 'swp46', 'swp2', 'swp2.1', 'swp2.10', 'swp2.100']
    from nose.tools import set_trace; set_trace()
    _output = common.sort_ports(ports)
    assert_equals(_output, '')

# test printing out range of numbers"
def test_group_ports_just_numbers():
    a = ['1', '2', '3', '4', '5', '10']
    assert_equals(common.create_range('', a), ['1-5', '10'])


# common - test group ports with no subifaces"
def test_group_port_no_subiface():
    a = ['swp1', 'swp2', 'swp3', 'swp4',
         'swp10', 'swp11', 'swp12', 'swp20']
    assert_equals(common.group_ports(a), ['swp1-4', 'swp10-12', 'swp20'])


def test_group_ports_where_one_does_not_have_number():
    a = ['downlink', 'downlink2', 'swp1', 'swp2', 'swp3']
    assert_equals(common.group_ports(a), ['downlink', 'downlink2', 'swp1-3'])


# test group ports with subifaces"
def test_group_port_with_subiface():
    a = ['swp1', 'swp2', 'swp3', 'swp4',
         'bond0.100', 'bond1.100', 'bond3.100',
         'swp33.100', 'swp34.100', 'swp40.100',
         'swp10', 'swp11', 'swp12', 'swp20']
    assert_equals(common.group_ports(a), ['bond0-1.100',
                                          'bond3.100',
                                          'swp33-34.100',
                                          'swp40.100',
                                          'swp1-4',
                                          'swp10-12',
                                          'swp20'])


def test_block_to_cidr_netmask():
    "common - convert block netmask to cidr"
    ipv6mask = 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe'
    assert_equals(common.netmask_dot_notation_to_cidr(ipv6mask), 127)
    ipv4mask = '255.255.254.0'
    assert_equals(common.netmask_dot_notation_to_cidr(ipv4mask), 23)
