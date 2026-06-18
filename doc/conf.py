# docs/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))

project = 'a.vim'
copyright = '2025, gyniu'
author = 'gyniu'
release = '0.1'

extensions = ['sphinx.ext.autodoc']  # 根据需要添加其他扩展
