#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile
from conans.client import tools

class GlmConan(ConanFile):
    name = "jom"
    version = "1.1.2"
    description = "jom is a clone of nmake to support the execution of multiple independent commands in parallel"
    url = "https://gitlab.lan.local/conan/conan-jom"
    homepage = "https://wiki.qt.io/Jom"
    license = "LGPL"
    build_policy = "missing"
    settings = "os_build", "arch_build", "arch", "compiler"

    def configure(self):
        if self.settings.os_build != "Windows":
            raise Exception("Only windows supported for jom")

    def build(self):
        tools.get("https://download.qt.io/official_releases/jom/jom_1_1_2.zip")
        os.rename("jom_1_1_2", "jom-{0}".format(self.version))

    def package(self):
        self.copy("*", dst="", keep_path=True)

    def package_id(self):
        self.info.include_build_settings()
        del self.info.settings.compiler
        del self.info.settings.arch

    def package_info(self):
        self.output.info("Using jom %s" % self.version)
        self.env_info.path.append(os.path.join(self.package_folder, "jom-{0}".format(self.version)))