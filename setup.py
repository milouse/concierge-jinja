#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import setuptools

from setuptools.command.test import test as TestCommand  # NOQA
import sys


class Tox(TestCommand):

    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import shlex
        import tox

        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


with open("README.rst", "rt") as readme_fp:
    long_description = readme_fp.read().strip()

REQUIREMENTS = (
    "concierge",
    "jinja2"
)

setuptools.setup(
    name="concierge_jinja",
    version="0.2",
    description="Maintainable SSH config",
    long_description=long_description,
    url="https://github.com/9seconds/concierge-jinja",
    author="Sergey Arkhipov",
    author_email="serge@aerialsounds.org",
    maintainer="Sergey Arkhipov",
    maintainer_email="serge@aerialsounds.org",
    license="MIT",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=REQUIREMENTS,
    entry_points={
        "concierge.templater": [
            "jinja = concierge_jinja.templater:Jinja2Templater"
        ]
    },
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ])
