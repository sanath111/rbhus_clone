#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
import subprocess
import rbhus_clone_db
import debug
import argparse
import constants
import shlex

projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

db = rbhus_clone_db.db()


def getAssID(proj_name, stage_name):
    get_ass_id_cmd = f"SELECT assetID FROM assets WHERE projName='{proj_name}' and stage='{stage_name}'"
    id_dict = db.execute(get_ass_id_cmd, dictionary=True)
    asset_id = id_dict[0]['assetID']
    return str(asset_id.strip())

def getAssPath(asset_id=None, proj_name=None, stage_name=None):
    if asset_id:
        get_path_cmd = f"SELECT path FROM assets WHERE assetID='{asset_id}'"
        path_dict = db.execute(get_path_cmd, dictionary=True)
        path = path_dict[0]['path']
        return str(path.strip())
    if proj_name and stage_name:
        get_path_cmd = f"SELECT path FROM assets WHERE projName='{proj_name}' and stage='{stage_name}'"
        path_dict = db.execute(get_path_cmd, dictionary=True)
        path = path_dict[0]['path']
        return str(path.strip())

def getAssUser(asset_id):
    get_ass_user_cmd = f"SELECT assignedUser FROM assets WHERE assetID='{asset_id}'"
    user_dict = db.execute(get_ass_user_cmd, dictionary=True)
    user = user_dict[0]['assignedUser']
    return str(user.strip())

def getAssDets(asset_id):
    get_ass_dets_cmd = f"SELECT * FROM assets WHERE assetID='{asset_id}'"
    ass_dict = db.execute(get_ass_dets_cmd, dictionary=True)
    dets = ass_dict[0]
    return dets

def getRole(user):
    get_role_cmd = f"SELECT role FROM users WHERE name='{user}'"
    role_dict = db.execute(get_role_cmd, dictionary=True)
    role = role_dict[0]['role']
    return str(role.strip())

def getAllStages(proj_name):
    get_stages_cmd = f"SELECT stage FROM assets where projName='{proj_name}'"
    stages = db.execute(get_stages_cmd, dictionary=True)
    return stages

def run_command(cmd):
    debug.info(f"Executing command: {cmd}")

    try:
        split_cmd = shlex.split(cmd)
        debug.info(f"Command split for execution: {split_cmd}")

        p = subprocess.Popen(
            split_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        stdout, stderr = p.communicate()

        debug.info(f"Return code: {p.returncode}")
        debug.info(f"Standard output: {stdout.strip()}")
        debug.info(f"Error output: {stderr.strip()}")

        if p.returncode == 0:
            return 'success'
        elif p.returncode == 1:
            return f'failed: {stdout.strip()}'
        else:
            return f'unknown return code {p.returncode}: {stderr.strip()}'

    except subprocess.SubprocessError as ex:
        debug.info(f"Subprocess error occurred: {ex}")
    except Exception as ex:
        debug.info(f"An unexpected error occurred: {ex}")

    return None

