# coding: utf-8
from fabric.api import run, env, cd, shell_env

from config import load_config


# 第一次部署脚本
def prod_deploy_first():
    config = load_config('PRODUCTION')
    env.host_string = config.HOST_STRING
    env.key_filename = config.HOST_KEY_FILENAME
    with cd('/opt/parkserver'):
        with shell_env(MODE='PRODUCTION'):
            run('git reset --hard HEAD')
            run('git pull')
            with cd('app'):
                run('bower update --allow-root')
            run('pip install -r requirements.txt')
            run('/etc/init.d/supervisor stop')
            run('/etc/init.d/supervisor start')


def dev_deploy_first():
    config = load_config('DEV')
    env.host_string = config.HOST_STRING
    env.key_filename = config.HOST_KEY_FILENAME
    with cd('/opt/parkserver'):
        with shell_env(MODE='TESTING'):
            run('git reset --hard HEAD')
            run('git pull')
            with cd('app'):
                run('bower update --allow-root')
            run('pip install -r requirements.txt')
            run('/etc/init.d/supervisor stop')
            run('/etc/init.d/supervisor start')


def test_deploy_first():
    config = load_config('TESTING')
    env.host_string = config.HOST_STRING
    env.key_filename = config.HOST_KEY_FILENAME
    with cd('/opt/parkserver'):
        with shell_env(MODE='TESTING'):
            run('git reset --hard HEAD')
            run('git pull')
            with cd('app'):
                run('bower update --allow-root')
            run('pip install -r requirements.txt')
            run('/etc/init.d/supervisor stop')
            run('/etc/init.d/supervisor start')


# 更新脚本
def prod_update():
    config = load_config('PRODUCTION')
    env.host_string = config.HOST_STRING
    env.key_filename = config.HOST_KEY_FILENAME
    with cd('/opt/parkserver'):
        with shell_env(MODE='PRODUCTION'):
            run('git reset --hard HEAD')
            run('git pull')
            run('supervisorctl restart parkserver')


def dev_update():
    config = load_config('DEV')
    env.host_string = config.HOST_STRING
    env.key_filename = config.HOST_KEY_FILENAME
    with cd('/opt/parkserver'):
        with shell_env(MODE='PRODUCTION'):
            run('git reset --hard HEAD')
            run('git pull')
            run('supervisorctl restart parkserver')


def test_update():
    config = load_config('TESTING')
    env.host_string = config.HOST_STRING
    env.key_filename = config.HOST_KEY_FILENAME
    with cd('/opt/parkserver'):
        with shell_env(MODE='PRODUCTION'):
            run('git reset --hard HEAD')
            run('git pull')
            run('supervisorctl restart parkserver')


# 重启脚本
def prod_restart():
    config = load_config('PRODUCTION')
    env.host_string = config.HOST_STRING
    env.key_filename = config.HOST_KEY_FILENAME
    run('supervisorctl restart parkserver')


def dev_restart():
    config = load_config('DEV')
    env.host_string = config.HOST_STRING
    env.key_filename = config.HOST_KEY_FILENAME
    run('supervisorctl restart parkserver')


def test_restart():
    config = load_config('TESTING')
    env.host_string = config.HOST_STRING
    env.key_filename = config.HOST_KEY_FILENAME
    run('supervisorctl restart parkserver')
