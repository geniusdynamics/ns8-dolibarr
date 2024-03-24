#!/usr/bin/env python3

#
# Copyright (C) 2023 Nethesis S.r.l.
# SPDX-License-Identifier: GPL-3.0-or-later
#

import agent
import json
import os
import sys

request = json.load(sys.stdin)

# Bind the new domain, overriding previous values (unbind)
agent.bind_user_domains([request["ldap_domain"]])