# -*- coding: utf-8 -*-
import os, configparser, click, requests, getpass, json, ctypes, zipfile, shutil
import inspect
import sys
from colorama import init, Fore, Back
SOURCE = False
user_dir = os.path.join("C:\\Users", getpass.getuser(), "AppData\\Roaming\\IRA")
cfg=configparser.ConfigParser()
sys.stdout.reconfigure(encoding='utf-8')
cwd = os.getcwd()

    

def cleardir(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def i(url, path):
    print(Fore.BLUE+"Downloading...")
    r = requests.get(url)
    with open(path, "wb") as f:
        print(Fore.BLUE+"Writing file...")
        f.write(r.content)
    print(Fore.GREEN+"Done")
def is_admin():
    if SOURCE:
        return True
    else:
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path,)
    return os.path.dirname(path)
    
prj_dir = get_script_dir()
wdir = get_script_dir()
def prepare(admin=True):
    try:
        global cfg, wdir
        #print(admin)
        os.chdir(prj_dir)
        if not admin:
            if not os.path.exists(user_dir):
                os.mkdir(user_dir)
            os.chdir(user_dir)
            wdir = user_dir
        if not os.path.exists("./data"):
            os.mkdir("data")
        if not os.path.exists("./temp"):
            os.mkdir("temp")
        if not os.path.exists("./ext"):
            os.mkdir("ext")
        if not os.path.exists("./data/config.ini"):
            print(get_script_dir())
            os.chdir(prj_dir)
            os.chdir("fatal")
            if SOURCE:
                cmd="python noconfig.py"
            else:
                if admin:
                    cmd="noconfig"
                else:
                    cmd="noconfig "+user_dir+"/data/config.ini"
            os.system(cmd)
            if admin:
                os.chdir("../")
            else:
                os.chdir(user_dir)
        cfg.read("data/config.ini")
        init(autoreset=True)
        main()
    except Exception as e:
        print(str(e))
        os.system("pause")
@click.command()
@click.option("-i", '--install', help="Package for installing")
@click.option("-e", "--extention", help="Extention for connecting. Format: name:path/to/zip/extention.zip")
#@click.option("-c", "--command", help="Command to execute. Avaliable:\n\t1. sync")
@click.option("-u", "--uninstall", help="Program to uninstall")
def main(install, extention, uninstall):
    """
    IRA (Install-Remove-Append)

    Ananlog of APT for Windows

    Supports Choco, WSL, Snap and Flatpak
    
    Argument: package with what you'll do operation
    """
    global cfg
    err = True
    if install:
        url = ""
        try:
            url = cfg.get("URL", install)
        except configparser.NoOptionError:
            print(Back.RED+Fore.GREEN+"Sorry, no package "+install+" found.")
        else:
            if url.split("|")[0] == "link":
                url = cfg.get("URL", url.split("|")[1])
            if url.split("|")[0] == "url":
                i(url.split("|")[1], "temp/file."+url.split("|")[2])
                print(Fore.BLUE+"Running installer...")
                path = ".\\temp\\file."+url.split("|")[2]
            else:
                print(Fore.BLUE+"Running extention...")
                os.chdir(url.split("|")[3])
                path = url.split("|")[1]
            os.system(path)
            os.chdir(wdir)
            print(Fore.GREEN+"Program installed.")
        finally:
            err = False
    if extention:
        ext_path = extention.split(":")[1]
        #print(ext_path)
        os.chdir(cwd)
        if not os.path.exists(ext_path):
            print(Back.RED+Fore.GREEN+"Sorry, that path doesn't exists")
        else:
            ext_folder = os.path.join(wdir, "ext", extention.split(":")[0])
            if not os.path.exists(ext_folder):
                os.mkdir(ext_folder)
            else:
                cleardir(ext_folder)
            if not zipfile.is_zipfile(ext_path):
                print(Fore.RED+"Extention is not a ZIP-file")
            else:
                z = zipfile.ZipFile(ext_path, 'r')
                print(Fore.BLUE+"Extracting...")
                z.extractall(ext_folder)
                print(Fore.GREEN+"Extracted")
                config = os.path.join(ext_folder, "config.json")
                if not os.path.exists(config):
                    cleardir(ext_folder)
                    print(Fore.RED+"No config file found!")
                else:
                    with open(config) as json_cfg:
                        data = json.load(json_cfg)
                    cfg.set("Extentions", data["name"], config)
                    for key, val in data["data"].items():
                        cfg.set("URL", key, "ext|"+"|".join(val)+"|"+ext_folder)
                    os.chdir(wdir)
                    with open("./data/config.ini", "w") as cfg_ini:
                        cfg.write(cfg_ini)
                    print(Fore.GREEN+"Exteniton sucsessifully installed.")
        err = False
    if uninstall:
        cmd = "wmic product where name=\"{0}\" call uninstall && cmd /c echo \"Uninstall {0} complete.\" & pause >> nul"
        code = os.system(cmd.format(uninstall))
        if code != 0:
            print(Fore.RED+"An error was oucutted.")
        err = False
    """if command:
        if command == "sync":
            if not is_admin():
                print(Fore.RED+"For sync you need admin worstation. Restarting with admin rights...")
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                err = False
            else:
                sync()"""
                
    if err:
        print("Incorrect syntax\nRun ira1 --help for details")
    os.system("pause")
if __name__ == '__main__':
        if is_admin():
            prepare()
        else:
            q = input("You are not admin. Would you like to use admin workstation?(y/n): ")
            if q == "y":
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            else:
                prepare(False)