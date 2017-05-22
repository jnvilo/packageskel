from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
import unittest
#import mock

from pathlib import Path
import shutil
from tests.utilities import module_function_name
from packageskel.packageskel import PackageSkel

class TestPackageSkel(unittest.TestCase):
    #@mock.patch(module_function_name(print))
    #def test_should_print_hello_world(self, mock_print):
    #    skeleton = python_skeleton.PythonSkeleton()
    #    skeleton.hello()
    #    mock_print.assert_called_once_with('Hello world!')


    def test_get_templates_dir(self):
        #pskel = Pack

        pass
    

    def test_copy_skeleton(self):
        """Tests whethere the default
        skeleton directory can be copied. """
        

        package_name = "test_package"
        destination_path = "/tmp"
        
        # This test makes sure the directory does not exist already
        
        template_dir = Path(destination_path, package_name)
        if template_dir.exists():
            shutil.rmtree(template_dir.as_posix())
        
        pskel = PackageSkel(package_name, destination_path=destination_path)
        pskel.copy_skeleton()
        self.assertTrue(template_dir.exists, msg="Successfully copied template")

        
        
