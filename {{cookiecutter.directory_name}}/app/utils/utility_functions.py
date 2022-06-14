import random
import re
import uuid
from itertools import permutations
from pathlib import Path

import numpy as np
import datetime as _datetime
import dateutil.relativedelta as _relativedelta
import base64
import json
import zipfile
from io import BytesIO
import os
import shutil

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
# a regular expression for validating an Email
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class UtilityFunctions:

    @staticmethod
    def is_email_valid(email):
        if re.search(regex, email):
            return True
        else:
            return False

    @staticmethod
    def get_random_number(upper_range):
        """
        get random number between 0 and upper range
        :return:
        """
        return int(random.randint(0, upper_range))

    @staticmethod
    def unzip_file(file_relative_path, output_location):
        try:
            Path(output_location).mkdir(exist_ok=True)
            with zipfile.ZipFile(file_relative_path) as file:
                file.extractall(path=output_location + "/")
        except Exception as e:
            logger.error(e)

    @staticmethod
    def get_datetime_obj_from_mmdd(mmdd_val, year=str(_datetime.date.today().year)):
        """
        gets datetime object from value in mmdd format. This would be assumed to be Qatar Time Zone
        TODO - check when year ends, what needs to be done
        :param mmdd_val: string in mmdd format. year would be assumed to be present
        :param year: pass year in YYYY format, if not passed current year is assumed
        :return: datetime object
        """
        datetime_val = None
        if len(mmdd_val) == 4:
            # fetching the current year, month and day of today
            # year = str(_datetime.date.today().year)
            month = mmdd_val[:2]
            date = mmdd_val[2:]

            try:
                date_str = date + "/" + month + "/" + year + " 00:00:00"
                datetime_val = _datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
            except Exception as e:
                logger.error(e)
        return datetime_val

    @staticmethod
    def get_time_range_for_date(date_obj):
        start = None
        end = None
        if isinstance(date_obj, _datetime.date) or isinstance(date_obj, _datetime.datetime):
            start = _datetime.datetime(
                year=date_obj.year,
                month=date_obj.month,
                day=date_obj.day,
                hour=0,
                minute=0,
                second=0
            )

            end = _datetime.datetime(
                year=date_obj.year,
                month=date_obj.month,
                day=date_obj.day,
                hour=23,
                minute=59,
                second=59
            )
        return start, end


    @staticmethod
    def get_uuid():
        return uuid.uuid1().__str__()

    @staticmethod
    def get_formatted_string_from_datetime(datetime_obj, date_format="%Y-%m-%d %H:%M:%S"):
        response = None
        if isinstance(datetime_obj, _datetime.datetime):
            response = datetime_obj.strftime(date_format)
        return response

    @staticmethod
    def get_formatted_string_from_date(datetime_obj, date_format="%Y-%m-%d"):
        response = None
        if isinstance(datetime_obj, _datetime.date):
            response = datetime_obj.strftime(date_format)
        return response
