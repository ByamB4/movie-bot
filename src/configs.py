import os

DEBUG_LEVEL = 2
PROJECT_NAME = os.path.dirname(os.path.abspath(__file__)).split('/')[-2]


def get_project_root():
    cwd = os.path.dirname(os.path.abspath(__file__))
    return cwd[:cwd.find(PROJECT_NAME) + len(PROJECT_NAME)]


def get_static_root():
    return os.path.join(get_project_root(), 'static')
