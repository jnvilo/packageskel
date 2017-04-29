from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division


from builtins import FileExistsError

from pathlib import Path
import os
import argparse
import sys
import shutil
import os

class PackageSkel(object):

    def __init__(self, package_name, destination_path):

        self.package_name = package_name
        self.destination_path = destination_path


    def get_rename_list(self):

        templates_dir = self.get_templates_dir()
        for r,d,f in os.walk(templates_dir):
            for file in f:
                print(os.path.join(root,file))




    def deploy_template(self):
        """
        All this does right now is to copy the default template contents.
        """

        templates_dir = self.get_templates_dir()
        package_dir = self.package_name

        if self.destination_path == None:
            self.destination_path = Path(os.getcwd())

        package_path = Path(self.destination_path, package_dir)

        if package_path.exists():
            print("{} exists. Deleting it.".format(package_path))
            shutil.rmtree(package_path.as_posix())

        print("Creating package skeleton {}".format(package_path))
        shutil.copytree(templates_dir, package_path.as_posix())

        #Rename the module packageskel to package_name
        orig_module_dir = Path(package_path,"packageskel").as_posix()
        new_module_dir = Path(package_path, self.package_name).as_posix()
        os.rename(orig_module_dir, new_module_dir)


        #Rename the packageskel.py to package_name
        orig_pyfile = Path(new_module_dir, "packageskel.py").as_posix()
        new_pyfile = Path(new_module_dir, "{}.py".format(self.package_name)).as_posix()
        os.rename(orig_pyfile, new_pyfile)


        #Rename the packagesle.py in tests to packageskel_tests.py
        test_pyfile = Path(package_path, "tests/packageskel.py").as_posix()
        new_test_pyfile = Path(package_path, "tests/{}_tests.py".format(self.package_name)).as_posix()

        os.rename(test_pyfile, new_test_pyfile)






    def get_templates_dir(self):
        file_path = os.path.abspath(__file__)
        file_dir, file_name = os.path.split(file_path)
        return os.path.join(file_dir,"templates","default")

def make_template():

    try:
        package_name = sys.argv[1]
    except IndexError as e:
        print("Package name is required.")
        sys.exit()

    destination_path = os.getcwd()
    print("Going to create package skeleton in : {}".format(destination_path))

    pskel = PackageSkel(package_name, destination_path)

    try:
        #pskel.deploy_template()
        pskel.get_rename_list()
    except FileExistsError as e:
        print("{} already exists as a directory. Aborting.".format(package_name))


if __name__ == "__main__":



    make_template()
