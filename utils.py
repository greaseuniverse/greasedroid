import argparse
import subprocess
import os
import shutil

def initialze(apk_filename="TrackerControl-githubRelease-latest.apk"):
    print(os.getcwd())
    if os.path.exists(apk_filename[:-4]) and os.path.isdir(apk_filename[:-4]):
        shutil.rmtree(apk_filename[:-4])
    print("[+] App directory deleted")

def decode(apk_filename="TrackerControl-githubRelease-latest.apk"):
    print(os.getcwd())
    subprocess.run("apktool d ./store/"+apk_filename, shell=True)
    print("[+] Decoded")

def build(apk_filename="TrackerControl-githubRelease-latest.apk"):
    print(os.getcwd())
    subprocess.run("apktool b  -use-aapt2 ./"+apk_filename[:-4], shell=True)
    print("[+] Built")

def sign(apk_filename="TrackerControl-githubRelease-latest.apk"):
    print(os.getcwd())
    subprocess.run("jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore release-key.keystore -keypass 23599331 -storepass 23599331 ./"+str(apk_filename[:-4])+"/dist/"+str(apk_filename)+" alias_name", shell=True)
    print("[+] Signed")
    print("[>] Exported: ./"+str(apk_filename[:-4])+"/dist/"+str(apk_filename))
