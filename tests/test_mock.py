import asyncio
import unittest
from unittest.mock import MagicMock, Mock, patch, call, mock_open

import tests


class ProductionClass:

    def method(self):
        self.something(1, 2, 3)

    def something(self, a, b, c):
        pass

    def closer(self, something):
        something.close()

    def some_method(self):
        return "real result"


def some_function():
    # keep the class path same
    instance = tests.test_mock.ProductionClass()
    return instance.some_method()


vals = {(1, 2): 1, (2, 3): 2}


def side_effect(*args):
    return vals[args]


DEFAULT = "default"
data_dict = {"file1": "data1",
             "file2": "data2"}


def open_side_effect(name):
    return mock_open(read_data=data_dict.get(name, DEFAULT))()


class AsyncContextManager:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


class TestMock(unittest.TestCase):

    def test_recording_method_calls(self):
        real = ProductionClass()
        # Mock method
        real.something = MagicMock()
        real.method()
        # Recording method calls on objects
        real.something.assert_called_once_with(1, 2, 3)

    def test_method_call_on_an_obj(self):
        real = ProductionClass()
        mock = Mock()
        # called mock.close()
        real.closer(mock)
        mock.close.assert_called_once_with()

    def test_mocking_classes(self):
        # need to keep the module same.
        with patch('tests.test_mock.ProductionClass') as mock:
            instance = mock.return_value
            instance.some_method.return_value = "the mocked result"
            result = some_function()
            assert result == "the mocked result"

    def test_naming_mocks(self):
        mock = MagicMock(name='foo')
        print(mock)
        print(mock.method)

    def test_tracking_all_calls(self):
        mock = MagicMock()
        mock.method()
        mock.attribute.method(10, x=53)
        expected = [call.method(), call.attribute.method(10, x=53)]
        call_result = mock.mock_calls
        self.assertEqual(call_result, expected)
        print(call_result)
        m = Mock()
        m.factory(important=True).deliver()
        # get the nested calls, parameter not record, below return True
        self.assertEqual(m.mock_calls[-1], call.factory(important=False).deliver())
        self.assertEqual(m.mock_calls[-1], call.factory(important=True).deliver())

    def test_setting_return_value(self):
        # mock a class return value
        mock = Mock()
        mock.return_value = 3
        self.assertEqual(mock(), 3)

        # mock method
        mock.method.return_value = 3
        self.assertEqual(mock.method(), 3)

        # mock return value in constructor
        mc = Mock(return_value=3)
        self.assertEqual(mc(), 3)

        # mock a attribute
        m = Mock()
        m.x = 3
        self.assertEqual(m.x, 3)

    def test_mock_complex(self):
        mock = Mock()
        cursor = mock.connection.cursor.return_value
        cursor.execute.return_value = ['foo']
        # chained calls
        res = mock.connection.cursor().execute("SELECT 1")
        self.assertEqual(['foo'], res)

        expected = call.connection.cursor().execute("SELECT 1").call_list()
        self.assertEqual(expected, mock.mock_calls)

    def test_raising_exception(self):
        mock = Mock(side_effect=Exception("Boom!"))
        with self.assertRaises(Exception):
            mock()

    def test_side_effect(self):
        mock = MagicMock(side_effect=[4, 5, 6])
        self.assertEqual(4, mock())
        self.assertEqual(5, mock())
        self.assertEqual(6, mock())

    def test_side_effect1(self):
        mock = MagicMock(side_effect=side_effect)
        self.assertEqual(1, mock(1, 2))
        self.assertEqual(2, mock(2, 3))

    def test_async_iterator(self):
        mock = MagicMock()
        # AsyncMock and MagicMock have support to mock Asynchronous Iterators through __aiter__
        mock.__aiter__.return_value = [1, 2, 3]

        async def main():
            return [i async for i in mock]

        print(asyncio.run(main()))

    def test_async_context(self):
        mock = MagicMock(AsyncContextManager())

        async def main():
            async with mock as result:
                pass

        asyncio.run(main())
        mock.__aenter__.assert_awaited_once()
        mock.__aexit__.assert_awaited_once()

    def test_mock_from_obj(self):
        # Mock allows you to provide an object as a specification for the mock, using the spec keyword argument.
        # Accessing methods / attributes on the mock that don’t exist on your specification object will
        # immediately raise an attribute error.
        mock = Mock(spec=ProductionClass)
        with self.assertRaises(AttributeError):
            mock.invalid_method()

        def f(a, b, c):
            pass

        mock_func = Mock(spec=f)
        mock_func(1, 2, 3)
        mock_func.assert_called_with(a=1, b=2, c=3)

    def test_mock_open_per_file(self):
        with patch('builtins.open', side_effect=open_side_effect):
            with open('file1') as file:
                self.assertEqual('data1', file.read())

            with open('file2') as file:
                self.assertEqual('data2', file.read())

            with open('file3') as file:
                self.assertEqual('default', file.read())
