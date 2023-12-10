"""
Author: Rugh1
Date: 10.12.2023
Description: functions for cyber2.7 work
"""
import base64
import glob
import os
import shutil
import subprocess
import pyautogui


ERR = "error has occurred"

def dir_cmd(msg):
    """
    List files in a directory.

    :param msg: The command and the directory path.
    :type msg: list

    :return: Comma-separated list of files in the directory or an error message.
    :rtype: str
    """
    output = ERR
    try:
        if(len(msg) < 2):
             output = 'pls enter the all reqiured parm'
        else: 
            output = ','.join(glob.glob(msg[1] + '\\*.*'))
            if(output == ''):
                output = 'directory doesnt exist'
    except Exception as err:
        output += ' ' + str(err)
    finally:
        return output

def delete_cmd(msg):
    """
    Delete a file.

    :param msg: The command and the file path.
    :type msg: list

    :return: Success message or an error message.
    :rtype: str
    """
    output = ERR
    try:
        if(len(msg) < 2):
             output = 'pls enter the all reqiured parm'
        else: 
            os.remove(msg[1])
            output = 'file deleted successfully'
    except Exception as err:
        output += ' ' + str(err)
    finally:
        return output

def copy_cmd(msg):
    """
    Copy a file.

    :param msg: The command, source file path, and destination file path.
    :type msg: list

    :return: Success message or an error message.
    :rtype: str
    """
    output = ERR
    try:
        if(len(msg) < 3):
             output = 'pls enter the all reqiured parm'
        else: 
            shutil.copy(msg[1], msg[2])
            output = 'file copied successfully'
    except Exception as err:
        output += ' ' + str(err)
    finally:
        return output

def execute_cmd(msg):
    """
    Execute a command.

    :param msg: The command to be executed.
    :type msg: list

    :return: Success message or an error message.
    :rtype: str
    """
    output = ERR
    try:
        if(len(msg) < 2):
             output = 'pls enter the all reqiured parm'
        else: 
            subprocess.call(msg[1])
            output = 'command executed successfully'
    except Exception as err:
        output += ' ' + str(err)
    finally:
        return output

def take_screenshot_cmd(msg):
    """
    Take a screenshot and save it as 'screen.jpg'.

    :param msg: The command.
    :type msg: list

    :return: Success message or an error message.
    :rtype: str
    """
    output = ERR
    try:
        image = pyautogui.screenshot()
        image.save(r'screen.jpg')
        output = 'screenshot was taken successfully'
    except Exception as err:
        output += ' ' + str(err)
    finally:
        return output

def send_photo_cmd(msg):
    """
    Sends screenshot.

    :param msg: The command and the directory path.
    :type msg: list

    :return: image as base64 encode as astring.
    :rtype: str
    """
    output = ERR
    try:
        with open('screen.jpg', "rb") as image_file:
            #encode image to base64 as astring
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        output = encoded_string
    except Exception as err:
        output += ' ' + str(err)
    finally:
        return output


def exit_cmd(msg):
    """
    Exit the program.

    :param msg: The command.
    :type msg: list

    :return: Farewell message.
    :rtype: str
    """
    return "bye now"