# -*- coding: utf-8 -*-
"""
This class caters to constants
"""

__version__ = '0.1'
__author__ = 'Utkarsh Srivastava'


class Constants:
    DOC_ID_PASSPORT = "Passport"
    DOC_ID_VISA = "Visa"

    DOC_CLASSES = {
        0: DOC_ID_PASSPORT,
        1: DOC_ID_VISA

    }

    DOC_INV_CLASSES = dict(zip(DOC_CLASSES.values(), DOC_CLASSES.keys()))
