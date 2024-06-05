# Welcome to the Checkbox OpenCL project!

This repository contains the Checkbox OpenCL Provider (OpenCL-specific test cases and test plans for [Checkbox]) as well as everything that is required to build the [checkbox-opencl-regression] snap in the snapstore.

# Checkbox OpenCL Provider

Located in the `checkbox-provider-opencl` directory, it contains:

- the test cases (also called "jobs" in the Checkbox jargon) and test plans to be run by Checkbox (in the `units` directory)

## PENDING
The following will be updated later but currently still contain data from the checkbox-kivu project
- the scripts required by some of the test cases (in the `bin` directory)
- the data (sample video, HTML pages) required by some of the test cases (in the `data` directory)
- unit tests for the scripts (in the `tests` directory)

# Requirements

- Ubuntu Jammy or Noble (22.04/24.04)
- Supported hardware platforms:
  - Intel platforms with recent GPU (>= Broadwell)

# Installation

Install the Checkbox runtime and the Kivu provider snaps:

```shell
sudo snap install --classic snapcraft
sudo snap install checkbox22
lxd init --auto
git clone https://github.com/mckees/checkbox-opencl-regression
cd checkbox-opencl-regression
snapcraft
sudo snap install --dangerous --classic ./checkbox-opencl-regression_2.0_amd64.snap
systemctl restart snap.checkbox-opencl-regression.remote-slave.service
checkbox-opencl-regression.regression-testing
```

Make sure that the provider service is running and active:

```shell
systemctl status snap.checkbox-opencl-regression.remote-slave.service
```

# Install dependencies

Some test need dependencies, so in order to run all tests, you might way to install those dependencies.
A helper script is available to install them:

```shell
checkbox-opencl-regression.install-full-deps
```

# Automated Run

To run the full test plan:

```shell
checkbox-opencl-regression.regression-testing

```
# Develop the Checkbox OpenCL provider

Since snaps are immutable, it is not possible to modify the content of the scripts or the test cases. Fortunately, Checkbox provides a functionality to side-load a provider on the DUT.

Therefore, if you want to edit a job definition, a script or a test plan, run the following commands on the DUT:

```shell
cd $HOME
git clone https://github.com/mckees/checkbox-opencl-regression
mkdir /var/tmp/checkbox-providers
cp -r $HOME/checkbox-opencl-regression/checkbox-provider-opencl /var/tmp/checkbox-providers/
```

You can then modify the content of the provider in `/var/tmp/checkbox-providers/checkbox-provider-opencl/`, and it's this version that will be used when you run the tests.

Please refer to the [Checkbox documentation] on side-loading providers for more information.

[Checkbox]: https://checkbox.readthedocs.io/
[checkbox-kivu-classic]: https://snapcraft.io/checkbox-kivu-classic
[Checkbox documentation]: https://checkbox.readthedocs.io/en/latest/side-loading.html
