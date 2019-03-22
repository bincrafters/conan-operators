from conans import ConanFile, tools
import os

class OperatorsConan(ConanFile):
    name = "operators"
    version = "1.1.1"
    description = "C++11 header-only library that provides highly efficient, move aware operators for arithmetic data types."
    url = "https://github.com/bincrafters/conan-operators"
    homepage = "https://github.com/taocpp/operators"
    license = "MIT"
    author = "Paul le Roux <pleroux0@outlook.com>"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    no_copy_source = True

    def source(self):
        tools.get("{}/archive/{}.tar.gz".format(self.homepage, self.version))
        extracted_dir = "operators-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*.hpp", dst="include", src="{}/include".format(self.source_subfolder))

    def package_id(self):
        self.info.header_only()
