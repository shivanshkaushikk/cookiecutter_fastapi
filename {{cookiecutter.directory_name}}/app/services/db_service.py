# -*- coding: utf-8 -*-
"""
This class helps in establishing database connection
"""

__version__ = '0.1'
__author__ = 'Utkarsh Srivastava'

import traceback
import logging
from sqlalchemy import create_engine
import urllib
import pandas as pd
from app.utils.yaml_parser import Config


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class DBService:

    def __init__(self) -> None:
        super().__init__()
        self.__db_host = Config.get_config_val('properties.database.host')
        self.__db_port = Config.get_config_val('properties.database.port')
        self.__db_username = Config.get_config_val('properties.database.user')
        self.__db_password = Config.get_config_val('properties.database.password')
        self.__db_schema = Config.get_config_val('properties.database.schema')
        self.__db_conn_string = f"""mysql+pymysql://{self.__db_username}:%s@{self.__db_host}:{self.__db_port}/{self.__db_schema}"""
        logger.info(self.__db_conn_string)

    def execute_sql_query(self, sql_query):
        """
        takes a string query and returns a dataframe
        :param sql_query: str
        :return: pd.DataFrame
        """
        df_response = None
        if sql_query is not None and sql_query != '':
            try:
                db_local_engine = create_engine(self.__db_conn_string % urllib.parse.quote_plus(self.__db_password))
                df_response = pd.read_sql_query(sql_query, con=db_local_engine)
                db_local_engine.dispose()
            except Exception as e:
                logger.error(e)
                traceback.print_exc()
            return df_response
