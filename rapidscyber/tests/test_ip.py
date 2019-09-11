import pytest

import cudf
import rapidscyber.ip

def test_ip_to_int():
    input = cudf.Series(["5.79.97.178", "94.130.74.45"])
    expected = cudf.Series([89088434, 1585596973])
    actual = rapidscyber.ip.ip_to_int(input)
    assert actual.equals(expected)

def test_int_to_ip():
    input = cudf.Series([89088434, 1585596973])
    expected = cudf.Series(["5.79.97.178", "94.130.74.45"])
    actual = rapidscyber.ip.int_to_ip(input)
    assert actual.equals(expected)

def test_is_ip():
    input = cudf.Series(["5.79.97.178", "1.2.3.4", "5", "5.79", "5.79.97", "5.79.97.178.100"])
    expected = cudf.Series([True, True, False, False, False, False])
    actual = rapidscyber.ip.is_ip(input)
    assert actual.equals(expected)

def test_is_reserved():
    input = cudf.Series(["240.0.0.0", "255.255.255.255", "5.79.97.178"])
    expected = cudf.Series([True, True, False])
    actual = rapidscyber.ip.is_reserved(input)
    assert actual.equals(expected)

def test_is_loopback():
    input = cudf.Series(["127.0.0.1", "5.79.97.178"])
    expected = cudf.Series([True, False])
    actual = rapidscyber.ip.is_loopback(input)
    assert actual.equals(expected)

def test_is_link_local():
    input = cudf.Series(["169.254.0.0", "5.79.97.178"])
    expected = cudf.Series([True, False])
    actual = rapidscyber.ip.is_link_local(input)
    assert actual.equals(expected)

def test_is_unspecified():
    input = cudf.Series(["0.0.0.0", "5.79.97.178"])
    expected = cudf.Series([True, False])
    actual = rapidscyber.ip.is_unspecified(input)
    assert actual.equals(expected)

def test_is_multicast():
    input = cudf.Series(["224.0.0.0", "239.255.255.255", "5.79.97.178"])
    expected = cudf.Series([True, True, False])
    actual = rapidscyber.ip.is_multicast(input)
    assert actual.equals(expected)

def test_is_private():
    input = cudf.Series(["0.0.0.0", "5.79.97.178"])
    expected = cudf.Series([True, False])
    actual = rapidscyber.ip.is_private(input)
    assert actual.equals(expected)

def test_is_global():
    input = cudf.Series(["0.0.0.0", "5.79.97.178"])
    expected = cudf.Series([False, True])
    actual = rapidscyber.ip.is_global(input)
    assert actual.equals(expected)

def test_netmask():
    input = cudf.Series(["5.79.97.178", "94.130.74.45"])
    expected = cudf.Series(["255.255.128.0", "255.255.128.0"])
    actual = rapidscyber.ip.netmask(input, 17)
    assert actual.equals(expected)

def test_hostmask():
    input = cudf.Series(["5.79.97.178", "94.130.74.45"])
    expected = cudf.Series(["0.0.127.255", "0.0.127.255"])
    actual = rapidscyber.ip.hostmask(input, 17)
    assert actual.equals(expected)

def test_mask():
    input_ips = cudf.Series(["5.79.97.178", "94.130.74.45"])
    input_masks = cudf.Series(["255.255.128.0", "255.255.128.0"])
    expected = cudf.Series(["5.79.0.0", "94.130.0.0"])
    actual = rapidscyber.ip.mask(input_ips, input_masks)
    assert actual.equals(expected)