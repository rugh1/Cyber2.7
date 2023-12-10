import base64
import glob
import os
import shutil
import subprocess
import pyautogui
from functions import *

def test_dir_cmd():
    assert dir_cmd(["dir_cmd", "C:"]) != ERR
    assert dir_cmd(["dir_cmd", "path/to/nonexistent/directory"]) == "directory doesnt exist"

def test_delete_cmd():
    # Create a temporary file for testing
    with open("temp_file.txt", "w") as temp_file:
        temp_file.write("This is a test file.")

    assert os.path.exists("temp_file.txt")
    assert delete_cmd(["delete_cmd", "temp_file.txt"]) == "file deleted successfully"
    assert not os.path.exists("temp_file.txt")

def test_copy_cmd():
    # Create a temporary file for testing
    with open("temp_file.txt", "w") as temp_file:
        temp_file.write("This is a test file.")

    assert os.path.exists("temp_file.txt")
    assert copy_cmd(["copy_cmd", "temp_file.txt", "temp_file_copy.txt"]) == "file copied successfully"
    assert os.path.exists("temp_file_copy.txt")

def test_take_screenshot_cmd():
    assert take_screenshot_cmd(["take_screenshot_cmd"]) == "screenshot was taken successfully"
    assert os.path.exists("screen.jpg")
    os.remove("screen.jpg")

def test_exit_cmd():
    assert exit_cmd(["exit_cmd"]) == "bye now"
