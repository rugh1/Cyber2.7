import glob
import os
import shutil
import subprocess
from PIL import ImageGrab

ERR = "error has occurred"
IMAGE_PLACE = 'image-place.'

def dir_cmd(msg):
    output = ERR
    try:
        output = glob.glob(msg[1] + '\\*.*')

    except Exception as err:
        output += ' ' + str(err)

    finally:
        return output


def delete_cmd(msg):
    output = ERR
    try:
        os.remove(msg[1])
        output = 'file deleted successfully'
    except Exception as err:
        output += ' ' + str(err)

    finally:
        return output


def copy_cmd(msg):
    output = ERR
    try:
        shutil.copy(msg[1], msg[2])
        output = 'file copied successfully'
    except Exception as err:
        output += ' ' + str(err)

    finally:
        return output


def execute_cmd(msg):
    output = ERR
    try:
        subprocess.call(msg[1])
        output = 'file copied successfully'
    except Exception as err:
        output += ' ' + str(err)

    finally:
        return output


def take_screenshot_cmd(msg):
    output = ERR
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(filepath, 'PNG')  # Equivalent to `screenshot.save(filepath, format='PNG')`
        output = 'screenshot was taken successfully'
    except Exception as err:
        output += ' ' + str(err)

    finally:
        return output


def send_photo(msg):
    output = ERR
    try:
        
    except Exception as err:
        output += ' ' + str(err)

    finally:
        return output
