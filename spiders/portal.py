import json
import logging
import time
from collections import namedtuple
from datetime import datetime
from typing import List, Dict

import mysql.connector
import requests

logger = logging.getLogger(__name__)

PortalRes = namedtuple("PortalRes", "status message data")
PortalTreeData = namedtuple("PortalTreeData", "query limit offset total hits")
TreeNode = namedtuple("TreeNode", "app_code app_tree level"
                                  " app_tag id follow binded tree_node source_url")
AppDetails = namedtuple("AppDetails", "status code tree_node name creator createTime mailGroup"
                                      " groupCode owner developer pm level app_type parent_system tags")

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,fr;q=0.6,sv;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'APP_LIST_ACTIVE_VIEW_ID=10924; APP_DETAIL_ACTIVE_TAB_ID=tab3; APP_DETAIL_ACTIVE_ENV_ID=prod; PORTALAPPLISTID="2|1:0|10:1702524433|15:PORTALAPPLISTID|16:eWlzaGVuLmNhaQ==|a97383be5150b9d6e4e30f103c5023c00bfb477e9230156e00119fb9c2bc96e7"; session=eyJ1c2VyX2lkIjoieWlzaGVuLmNhaSJ9.ZYgjog.yHoQgm8nTEcyKha_MK61vqFpO-Q; QN1=0001290049a859fdd2b0b654; APPSERVICETOKEN=0DF0F04D6A87D9528CD2B2BDF3254FB4; APPQTALK=yishen.cai; QN1=00012700072c59d2e4e0f245',
    'DNT': '1',
    'Origin': 'http://portal.corp.qunar.com',
    'Referer': 'http://portal.corp.qunar.com/portal/apptree',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}


class Portal(object):
    add_app_code_info = ("INSERT INTO t_appcode_info"
                         "(app_code, app_desc, app_code_path, status, create_by, update_by, create_time, update_time) "
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="l-standdb27.noah.beta.cn0",
            port=4570,
            user="u462036",
            password="cfced18fac4d5380",
            database='db_train_demo')
        self.cur = self.cnx.cursor()
        logger.info("portal init complete...")

    def run(self):
        logger.info("portal start running...")
        # 1.get tree node;
        # 2.get details;
        # 3.parse and output to database;
        self.write_to_db([self.get_app_details(app.app_code) for app in self.get_app_tree()
                          if app.app_code.startswith('f_')])

    def get_app_tree(self) -> List[TreeNode]:
        url = "http://portal.corp.qunar.com/applist/app_code/query_member_appcodes"
        payload = """
            {
                "binded": "all",
                "app_level": "all",
                "offset": 0,
                "page_size": 10000,
                "source_url": "",
                "app_code": ""
            }
        """
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            body_str = response.text
            obj_data = json.loads(body_str)
            hits: List[Dict] = obj_data['data']['hits']
            nodes = [TreeNode(*hit.values()) for hit in hits]
            logger.info("get nodes of {}".format(str(len(nodes))))
            return nodes
        except Exception as e:
            logger.error(e)
        return list()

    def get_app_details(self, app_code: str) -> AppDetails | None:
        try:
            logger.info('get details of {}'.format(app_code))
            url = "http://portal.corp.qunar.com/apptree/app_code/get_appcode_discard_flow?app_code={}&_ts=1703503210621"

            response = requests.request("GET", url.format(app_code), headers=headers, data={})
            obj_data: Dict = json.loads(response.text)
            info: Dict = obj_data['data']['info']
            detail = AppDetails(*info.values())
            logger.info('details of {} is {}'.format(app_code, detail))
            time.sleep(1)
            return detail
        except Exception as e:
            logger.error(e)
        return None

    def write_to_db(self, details: List[AppDetails]):
        logger.info("write total {} details to db".format(str(len(details))))
        for detail in details:
            logger.info("write details of {}".format(detail.code))
            self.cur.execute(self.add_app_code_info, (
                detail.code,
                detail.name,
                detail.tree_node,
                1,
                detail.creator,
                detail.creator,
                datetime.now(),
                datetime.now()
            ))
            self.cnx.commit()
