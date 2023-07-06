import unittest
from unittest import IsolatedAsyncioTestCase

events = []

import logging
from logging import config

logging.config.fileConfig(
    'logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class AsyncConnection:

    def __int__(self):
        pass


class Test(IsolatedAsyncioTestCase):

    def setUp(self):
        events.append("setUp")

    async def asyncSetUp(self):
        self._async_connection = await AsyncConnection()
        events.append("asyncSetUp")

    async def test_response(self):
        events.append("test_response")
        response = await self._async_connection.get("https://example.com")
        self.assertEqual(response.status_code, 200)
        self.addAsyncCleanup(self.on_cleanup)

    def tearDown(self):
        events.append("tearDown")

    async def asyncTearDown(self):
        await self._async_connection.close()
        events.append("asyncTearDown")

    async def on_cleanup(self):
        events.append("cleanup")


if __name__ == "__main__":
    unittest.main()
