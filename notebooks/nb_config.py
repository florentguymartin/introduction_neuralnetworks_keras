### taken from http://drivendata.github.io/cookiecutter-data-science/#notebooks-are-for-exploration-and-communication with small modifications

# Load the "autoreload" extension
#%load_ext autoreload

# always reload modules marked with "%aimport"
# see http://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html?highlight=autoreload
#%autoreload 2

import os
import sys

# add the 'src' directory as one where we can import modules
src_dir = os.path.join(os.getcwd(), os.pardir, 'src')
sys.path.append(src_dir)
# this allows to import modules or packages contained in 'src' folder

# add the folder above the package in python path. This allows to 'import Py_Data_talk'
package_dir = os.path.join(os.getcwd(), os.pardir, os.pardir)
sys.path.append(package_dir)