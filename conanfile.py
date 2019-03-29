#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools

class GlmConan(ConanFile):
    name = "jom"
    package_revision = "-r1"
    upstream_version = "1.1.2"
    version = "{0}{1}".format(upstream_version, package_revision)
    description = "jom is a clone of nmake to support the execution of multiple independent commands in parallel"
    url = "https://git.ircad.fr/conan/conan-jom"
    homepage = "https://wiki.qt.io/Jom"
    license = "LGPL"
    settings = "os", "arch", "compiler"

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        if not tools.os_info.is_windows:
            raise Exception("Only Windows is supported by jom")
        else:
            tools.get("https://download.qt.io/official_releases/jom/jom_1_1_2.zip")

    def package(self):
        self.copy("*", dst="", keep_path=True)

    def package_id(self):
        self.info.include_build_settings()
        del self.info.settings.compiler
        del self.info.settings.arch

    def package_info(self):
        self.output.info("Using jom %s" % self.upstream_version)
        self.env_info.path.append(self.package_folder)
