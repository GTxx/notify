import multiprocessing
import os

config_file_path = os.path.abspath(__file__)

workers = multiprocessing.cpu_count() * 2 + 1
bind = '127.0.0.1:8000'
chdir = os.path.join(os.path.dirname(config_file_path), 'notify')
