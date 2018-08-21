from conan.packager import ConanMultiPackager
from conans import tools
from conans import __version__ as conan_version
from conans.model.version import Version

if __name__ == "__main__":
    if tools.os_info.is_windows:
        builder = ConanMultiPackager(username="fw4spl")
        builder.add({"os_build": "Windows", "arch_build": "x86"}, {}, {}, {})
        builder.add({"os_build": "Windows", "arch_build": "x86_64"}, {}, {}, {})
        builder.run()
    else:
        print("This package is only available on Windows")
