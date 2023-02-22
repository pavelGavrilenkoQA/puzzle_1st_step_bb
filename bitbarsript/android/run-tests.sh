#!/bin/bash
###### Cloud testrun dependencies start
echo "Extracting tests.zip..."
echo $PWD
echo $(ls)
unzip tests.zip

echo "apt"
echo $(apt update)
echo $(apt install nano)
echo "sudo apt"
echo $(sudo apt update)
echo "adb ser com pack"
echo $(adb version)
echo $(adb devices)
echo $(adb kill-server)


echo "Installing pip for python"
python -m venv .venv
source .venv/bin/activate

echo "Installing Appium Python Client 0.24 and xmlrunner 1.7.7"
chmod 0755 requirements.txt

echo "Try start with 1ns airtest install"
#pip install -r requirements.txt
pip install -U airtest
echo "Copy presetup adb"
cp -f /root/Android/Sdk/platform-tools/adb .venv/lib/python3.6/site-packages/airtest/core/android/static/adb/linux/  ## это сработало
#echo "Delete old adb in airtest"
#rm /test/.venv/lib/python3.6/site-packages/airtest/core/android/static/adb/linux/adb
#/root/Android/Sdk/platform-tools/adb -- Path to base adb BitBar machine
#echo "Copy new adb to air test"
#cp adb .venv/lib/python3.6/site-packages/airtest/core/android/static/adb/linux/
#echo $(ls)
#echo $(ls .venv/lib/python3.6/site-packages/airtest/core/android/static/adb/linux/)

## Run the test:
echo "Running tests"

#rm -rf screenshots
cd main
echo $(ls)
echo "I go to last stop before start"
python main.py
echo "Print main after test"
echo $(ls)
echo "Print result failed"
echo $(nano failed.txt)
echo "Print result passed"
echo $(nano passed.txt)

cd ..
echo $(ls)
echo "Packing main after test"
zip -r -9 main_after.zip /test/main
echo $(curl --upload-file main_after.zip https://transfer.sh/main_after.zip)
