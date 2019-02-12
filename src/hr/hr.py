import subprocess

def create_user(user):
    print(f"Adding user `{user['name']}`")
    try:
        p = subprocess.run(['useradd', user['name']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(p.stderr)
        print(p.stdout)
    except:
        print(f"Failed to add user {user['name']}")
        sys.exit(1)
    return True

def delete_user(username):
    return subprocess.Popen(['userdel','--remove', username], stdout=subprocess.PIPE)

def update_user(user):
    return subprocess.Popen(['usermod','-p', user['password'], user['name']], stdout=subprocess.PIPE)

