import glob
import os
import shutil
import subprocess
import pyautogui

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
        image = pyautogui.screenshot()
        image.save(r'screen.jpg')
        output = 'screenshot was taken successfully'
    except Exception as err:
        output += ' ' + str(err)
    finally:
        return output

