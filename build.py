from conan.packager import ConanMultiPackager
from conans import tools

if __name__ == "__main__":
    if tools.os_info.is_windows:
        builder = ConanMultiPackager(username="fw4spl")
        builder.run()
    else:
        print("This package is only available on Windows")
