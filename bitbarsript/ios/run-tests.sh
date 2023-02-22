#!/bin/bash

# Name of the test file
#TEST=${TEST:="BitbarSampleAppTest.py"}

echo "Extracting tests.zip..."
unzip tests.zip

#echo "nano install"
#echo $(brew install nano)

echo "Setting up python env:"
python3 -m venv .venv
source .venv/bin/activate

echo "Installing requirements"
chmod 0755 requirements.txt
pip install -r requirements.txt
pip install -U airtest


#########################################################
#
# Preparing to start Appium
# - UDID is the device ID on which test will run and
#   required parameter on iOS test runs
# - appium - is a wrapper tha calls the latest installed
#   Appium server. Additional parameters can be passed
#   to the server here.
#
#########################################################

echo "UDID set to ${IOS_UDID}"
echo "Starting Appium ..."
appium -U ${IOS_UDID}  --log-no-colors --log-timestamp --command-timeout 120
# xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination ${IOS_UDID} test



#########################################################
#
# Setting of environment variables used later in test
# - used for Appium desired capabilities
# - note, APPIUM_URL is same for local and cloud server
#   runs
#########################################################
export APPIUM_APPFILE="$PWD/application.ipa"
export APPIUM_URL="http://localhost:4723/wd/hub"
export APPIUM_DEVICE="Local Device"
export APPIUM_PLATFORM="IOS"
export APPIUM_AUTOMATION="XCUITest"


## check iproxy
echo $(iproxy --version)
iproxy 8100 8100 &
echo "Iproxy launched"
wait 3
echo "Go other part script"


## Start test execution
## Run the test:
echo "Running tests"
cd main
python main.py
echo "Print main after test"
echo $(ls)
echo "Print result failed"
echo $(cat failed.txt)
echo "Print result passed"
echo $(cat passed.txt)

cd ..
echo $(ls)
echo $(pwd)
echo "Packing main after test"
zip -r -9 main_after.zip /Users/testdroid/test/main
echo $(curl --upload-file main_after.zip https://transfer.sh/main_after.zip)
