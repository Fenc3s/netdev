"""
Copyright (c) 2019 Sergey Yakovlev <selfuryon@gmail.com>.

Vendors unit module
"""
from netdev.vendors.cisco_like import CiscoCLIModes, create_cisco_like_dmanager

__all__ = ("create_cisco_like_dmanager", "CiscoCLIModes")