import pytest
import subprocess
import tempfile

from hr import hr
encrypted_password = '$6$PJB/6tU3YJhpmIuo$xupl0/eAl/81xDN1N84nXYeiU92vZn/UpRe.uvPJ91Ns6cxGa1XNnLLpDYIOlN5WBLPJHS4JEp8boqRPcwr3l.'
user = {
    'name': 'kevin',
    'groups': ['wheel', 'dev'],
    'password': encrypted_password
}

def test_create_user(mocker):
    """
    Utilise useradd to add user
    """
    mocker.patch('subprocess.run')
    assert hr.create_user(user)
    subprocess.run.assert_called_with(['useradd', user['name']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def test_delete_user(mocker):
    """
    Utilise userdel to delete user
    """
    mocker.patch('subprocess.Popen')
    assert hr.delete_user(user['name'])
    subprocess.Popen.assert_called_with(['userdel', '--remove', user['name']], stdout=subprocess.PIPE)

def test_update_user(mocker):
    """
    Utilise usermod to update user
    """
    mocker.patch('subprocess.Popen')
    hr.update_user(user)
    subprocess.Popen.assert_called_with(['usermod','-p', encrypted_password,user['name']], stdout=subprocess.PIPE)

def test_parse_inventory_file():
    """
    Utilise json.dumps to parse inventory file
    """
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(b"""
    [
        {
            "name": "kevin",
            "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
        }
    ]
    """)
    f.close()
    expect_users=[{"name":"kevin","password":"$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"}]
    users = hr.parse_inventory_file(f.name)
    assert expect_users == users


