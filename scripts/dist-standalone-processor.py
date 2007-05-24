#!/usr/bin/python
import os
import shutil
from utils import *

processorDir = "./dist/processor/socorro"

def setup(distPath):
  makeDistDirs(distPath, ["lib"])
  copyLibFiles(["monitor.py", "processor.py", "helpers.py", "__init__.py"],
               distPath, "/lib/")
  copyModule("simplejson", "./webapp/socorro/lib/simplejson/*.py", distPath)
  copyModule("models", "./webapp/socorro/models/*.py", distPath)
  shutil.copy("./webapp/socorro/lib/__init__.py",
              os.path.join(distPath, "__init__.py"))
  shutil.copy("./scripts/start-processor.py",
              os.path.join(distPath, "../start-processor.py"))
  shutil.copy("./docs/README-standalone-processor.txt",
              os.path.join(distPath, "../README.txt"))

setup(processorDir)
