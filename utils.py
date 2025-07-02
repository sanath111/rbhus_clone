#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os
import sys
import subprocess
import rbhus_clone_db
import rbhus_clone_db_sqlite
import debug
import argparse
import constants
import shlex

projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

db = rbhus_clone_db_sqlite.db()


### Users Table ###

def getUsers():
    get_user_details = "SELECT name FROM users"
    user_dets = db.execute(get_user_details, dictionary=True)
    all_users = [x['name'] for x in user_dets]
    return all_users

def getPassword(user):
    get_pass_cmd = f"SELECT password FROM users WHERE name='{user}'"
    pass_dict = db.execute(get_pass_cmd, dictionary=True)
    password = pass_dict[0]['password']
    return str(password.strip())

def getRole(user):
    get_role_cmd = f"SELECT role FROM users WHERE name='{user}'"
    role_dict = db.execute(get_role_cmd, dictionary=True)
    role = role_dict[0]['role']
    return str(role.strip())

def getAdmins():
    get_user_details = "SELECT * FROM users"
    user_dets = db.execute(get_user_details, dictionary=True)
    master_admin = [x['name'] for x in user_dets if x['role'] == "master_admin"]
    admins = [x['name'] for x in user_dets if x['role'] == "admin" or x['role'] == "master_admin"]
    return master_admin, admins

def addUser(username, password, role):
    add_user_cmd = f"INSERT INTO users (name,password,role) VALUES ('{username}','{password}','{role}') "
    add_user_result = db.execute(add_user_cmd)
    return add_user_result

def updatePassword(username, password):
    update_pass_cmd = f"UPDATE users SET password='{password}' WHERE name='{username}' "
    update_pass_result = db.execute(update_pass_cmd)
    return update_pass_result

def updateRole(username, role):
    update_role_cmd = f"UPDATE users SET role='{role}' WHERE name='{username}' "
    update_role_result = db.execute(update_role_cmd)
    return update_role_result

### Projects Table ###

def getProjNames():
    query_proj = "SELECT projName from projects"
    projects = db.execute(query_proj,dictionary=True)
    return projects

def getProjStatus(proj_name):
    get_proj_status = f"SELECT status FROM projects WHERE projName='{proj_name}'"
    status_dict = db.execute(get_proj_status, dictionary=True)
    status = status_dict[0]['status']
    return status

def getProjReadStatus(proj_name):
    get_proj_read_status = f"SELECT readOnly FROM projects WHERE projName='{proj_name}'"
    read_status_dict = db.execute(get_proj_read_status, dictionary=True)
    read_status = read_status_dict[0]['readOnly']
    return read_status

def setProjStatus(proj_name, status):
    set_proj_status = f"UPDATE projects SET status='{status}' WHERE projName='{proj_name}'"
    set_status_result = db.execute(set_proj_status)
    return set_status_result

def setProjReadStatus(proj_name, read_status):
    set_proj_read_status = f"UPDATE projects SET readOnly='{read_status}' WHERE projName='{proj_name}'"
    set_read_status_result = db.execute(set_proj_read_status)
    return set_read_status_result

def createNewProject(proj_name, proj_path, proj_status):
    new_proj_cmd = f"INSERT INTO projects (projName, path, status) VALUES ('{proj_name}', '{proj_path}', {proj_status}) "
    create_proj_result = db.execute(new_proj_cmd)
    return create_proj_result

### Assets Table ###

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
    return None

def getAssUser(asset_id):
    get_ass_user_cmd = f"SELECT assignedUser FROM assets WHERE assetID='{asset_id}'"
    user_dict = db.execute(get_ass_user_cmd, dictionary=True)
    user = user_dict[0]['assignedUser']
    return str(user.strip())

def getAssDetsByAssId(asset_id):
    get_ass_dets_cmd = f"SELECT * FROM assets WHERE assetID='{asset_id}'"
    ass_dict = db.execute(get_ass_dets_cmd, dictionary=True)
    dets = ass_dict[0]
    return dets

def getAssDetsByProjName(proj_name, ass_user=None):
    if ass_user:
        get_ass_dets_cmd = f"SELECT * FROM assets WHERE projName='{proj_name}' AND assignedUser='{ass_user}' ORDER BY stage"
    else:
        get_ass_dets_cmd = f"SELECT * FROM assets WHERE projName='{proj_name}' ORDER BY stage"
    ass_dict = db.execute(get_ass_dets_cmd, dictionary=True)
    return ass_dict

def getAllStages(proj_name):
    get_stages_cmd = f"SELECT stage FROM assets where projName='{proj_name}'"
    stages = db.execute(get_stages_cmd, dictionary=True)
    return stages

def createNewAsset(ass_id, proj_name, stage, path, ass_user):
    new_ass_cmd = f"INSERT INTO assets (assetID, projName, stage, path, assignedUser) VALUES ('{ass_id}','{proj_name}','{stage}','{path}','{ass_user}') "
    create_ass_result = db.execute(new_ass_cmd)
    return create_ass_result

def updateAssUser(proj_name, stage_name, username):
    update_ass_user_cmd = f"UPDATE assets SET assignedUser='{username}' WHERE projName='{proj_name}' AND stage='{stage_name}' "
    update_ass_user_result = db.execute(update_ass_user_cmd)
    return update_ass_user_result

### Stages Table ###

def getStageName(index):
    get_stage_name = f"SELECT name FROM stages WHERE `index`={index}"
    stage_name_dict = db.execute(get_stage_name, dictionary=True)
    stage_name = stage_name_dict[0]['name']
    return str(stage_name)

def getStageIndex(stage_name):
    get_stage_index = f"SELECT `index` FROM stages WHERE `name`='{stage_name}'"
    stage_index_dict = db.execute(get_stage_index, dictionary=True)
    stage_index = stage_index_dict[0]['index']
    return str(stage_index)

def getStageDets():
    get_stage_details = "SELECT * FROM stages"
    stage_dets = db.execute(get_stage_details, dictionary=True)
    return stage_dets

### Roles Table ###

def getRoles():
    get_all_roles = "SELECT role FROM roles"
    role_dets = db.execute(get_all_roles, dictionary=True)
    all_roles = [x['role'] for x in role_dets]
    return all_roles

### Run Commands ###

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

