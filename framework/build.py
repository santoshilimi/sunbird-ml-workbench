# [TODO] compile the ML workbench
# [TODO] run tests
# [TODO] check for lints
# [TODO] packaging - framwork and core operators

from pybuilder.core import init, use_plugin

use_plugin("python.core")
# use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("exec")

default_task = "publish"

name = "mlworkbench"
version = "0.0.1"
license = "AGPL"

@init
def initialize(project):
    project.build_depends_on('mockito')
    project.set_property('publish_command', 'cp target/dist/mlworkbench-0.0.1/dist/mlworkbench-0.0.1.tar.gz ../dist')