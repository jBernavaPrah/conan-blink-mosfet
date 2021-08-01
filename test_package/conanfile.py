import os

from conans import ConanFile, tools
from conan.tools.cmake import CMake


class BlinkTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain", "VirtualEnv"
    apply_env = False

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self):
            self.run(os.path.sep.join([".", "bin", "example"]), env="conanrunenv")
