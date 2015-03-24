# -*- coding: utf-8 -*-
"""PKR101: Professional narcisissm.

---
layout:     post
error_code: PKR101
source:     Pinker's book on writing
source_url: ???
title:      professional narcisissm
date:       2014-06-10 12:31:19
categories: writing
---

Points out academic narcisissm.

"""
from tools import memoize, existence_check


@memoize
def check(blob):
    """Suggest the preferred forms."""
    err = "PKR101"
    msg = "Professional narcisissm. Talk about the subject, not its study."

    narcisissm = [
        "In recent years, an increasing number of [a-zA-Z]{3,}sts have",
    ]

    return existence_check(blob, narcisissm, err, msg)