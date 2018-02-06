import os
import sys
from typing import List
from unittest import TestCase, skip

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from scripts import backend, frontend
from scripts.utils import command_line_args
from scripts.utils.command_line_args import CommandMap


class ParserTester(TestCase):

    def assert_raises_parser_error(self,
                                   command_map: CommandMap,
                                   args: List[str]):
        parser = command_line_args.create_parser(backend.command_map)
        parsed_args = parser.parse_args(args)
        with self.assertRaises(TypeError):
            command_line_args.execute_command(parsed_args, command_map)


class TestSingleServerParser(ParserTester):

    def assert_backend_and_frontend_raise_error(self, args: List[str]):
        self.assert_raises_parser_error(command_map=backend.command_map,
                                        args=args)
        self.assert_raises_parser_error(command_map=frontend.command_map,
                                        args=args)

    def test_dependency_management_requires_dependencies(self):
        self.assert_backend_and_frontend_raise_error(args=['add'])
        self.assert_backend_and_frontend_raise_error(args=['upgrade'])
        self.assert_backend_and_frontend_raise_error(args=['remove'])

    def test_only_dependency_management_allows_variable_arguments(self):
        self.assert_backend_and_frontend_raise_error(args=['types', 'bad'])
        self.assert_backend_and_frontend_raise_error(args=['run', 'bad'])
        self.assert_backend_and_frontend_raise_error(args=['install', 'bad'])


class TestRunParser(ParserTester):

    @skip('not implemented')
    def test_execute_on_target_environment_requires_target_action(self):
        raise NotImplementedError

    @skip('not implemented')
    def test_dependency_management_requires_target_specification(self):
        raise NotImplementedError

    @skip('not implemented')
    def test_dependency_management_requires_dependencies(self):
        raise NotImplementedError

    @skip('not implemented')
    def test_only_dependency_management_allows_variable_arguments(self):
        raise NotImplementedError
