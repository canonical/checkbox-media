# Welcome to the Checkbox Kivu project!

This repository contains the Checkbox Kivu Provider (Kivu-specific test cases and test plans for [Checkbox]) as well as everything that is required to build the [checkbox-kivu-classic] snap in the snapstore.

# Checkbox Kivu Provider

Located in the `checkbox-provider-kivu` directory, it contains:

- the test cases (also called "jobs" in the Checkbox jargon) and test plans to be run by Checkbox (in the `units` directory)
- the scripts required by some of the test cases (in the `bin` directory)
- the data (sample video, HTML pages) required by some of the test cases (in the `data` directory)
- unit tests for the scripts (in the `tests` directory)

# Requirements

- Ubuntu Jammy (22.04)
- Chromium browser
- Supported hardware platforms:
  - Intel platforms with recent GPU (>= Broadwell)
  - AMD platform with Radeon GPU
- At least 1 active display (typically, a laptop with closed lid will not work)

# Installation

Install the Checkbox runtime and the Kivu provider snaps:

```shell
sudo snap install checkbox22
sudo snap install checkbox-kivu-classic --classic
```

Make sure that the provider service is running and active:

```shell
systemctl status snap.checkbox-kivu-classic.remote-slave.service
```

# Install dependencies

Some test need dependencies, so in order to run all tests, you might way to install those dependencies.
A helper script is available to install them:

```shell
checkbox-kivu-classic.install-full-deps
```

# Automated Run

To run the full test plan:

```shell
checkbox-kivu-classic.test-runner-automated
```
To run the hardware decoding tests:

```shell
checkbox-kivu-classic.test-runner-automated-hwdec
```

# Interactive Run

Interactive run allows you to select test plan and specific tests to run.

```shell
checkbox.checkbox-cli remote 127.0.0.1
```

You will be presented with a long list of available test plans. You can filter this out using the `/` key to search for `Kivu`. Select the Kivu test plan, and follow the instructions on \
screen to start the test run.

# Develop the Checkbox Kivu provider

Since snaps are immutable, it is not possible to modify the content of the scripts or the test cases. Fortunately, Checkbox provides a functionality to side-load a provider on the DUT.

Therefore, if you want to edit a job definition, a script or a test plan, run the following commands on the DUT:

```shell
cd $HOME
git clone git@github.com:canonical/checkbox-kivu.git
mkdir /var/tmp/checkbox-providers
cp -r $HOME/checkbox-kivu/checkbox-provider-kivu /var/tmp/checkbox-providers/
```

You can then modify the content of the provider in `/var/tmp/checkbox-providers/checkbox-provider-kivu/`, and it's this version that will be used when you run the tests.

Please refer to the [Checkbox documentation] on side-loading providers for more information.

[Checkbox]: https://checkbox.readthedocs.io/
[checkbox-kivu-classic]: https://snapcraft.io/checkbox-kivu-classic
[Checkbox documentation]: https://checkbox.readthedocs.io/en/latest/side-loading.html
