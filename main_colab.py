import os
import sys

py_folder = '/content/repo'
print('adding', py_folder, 'to sys.path')
if not py_folder in sys.path:
    sys.path.append(py_folder)

argv = '--model-dir ./models/v2_93/ ' \
       '--model-name model-90000 ' \
       '--before-ch 31 ' \
       '--deploy-vis ' \
       '--gpu_memory_fraction 0.9 ' \
       '--output-dir ./output/v2_93/Regular ' \
       '--test-list datas/Regular/list.txt ' \
       '--prefix datas/Regular'.split(' ')
os.chdir('/content/drive/My Drive/colab/unshake/demo')

import importlib
import imp

import deploy_bundle

imp.reload(deploy_bundle)
deploy_bundle.argv = argv
