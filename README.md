# Load the IOTA app onto the Ledger Nano S

## Prerequisites

- Make sure that your Ledger Nano S is running firmware 1.4.2.
For update instructions see: [How to update my Ledger Nano S with the firmware 1.4](https://support.ledgerwallet.com/hc/en-us/articles/360001340473-How-to-update-my-Ledger-Nano-S-with-the-firmware-1-4)
- Ensure that the following packages are installed:
  - libudev-dev
  - libusb-1.0-0-dev
  - python-dev
  - virtualenv

### Ledger udev rules

When running on Linux, make sure the following rules have been added to `/etc/udev/rules.d/`. This is prerequisite for any software (not just this script) in order to access the Ledger Nano S!

Ensure that the current user belongs to the `plugdev` group and install the rules provided by LedgerHQ:
```
wget -q -O - https://raw.githubusercontent.com/LedgerHQ/udev-rules/master/add_udev_rules.sh | sudo bash
```

If connection issues still persist afterwards, please refer to
https://support.ledgerwallet.com/hc/en-us/articles/115005165269-Fix-connection-issues

## Install the ledgerblue Python package

It is recommended to install ledgerblue in a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
```
virtualenv ledger
source ledger/bin/activate
pip install ledgerblue
```

## Load the IOTA Ledger app

- Connect your Ledger to the PC and unlock it.
- To load the app, be sure that the dashboard is opened in the Ledger.
- Run the following command from the folder that contains the `app.hex` to load the pre-compiled app onto the Ledger:
```
python install_app.py
```
- Accept all the messages on the Ledger.
