## Accept the webcam permissions

Instructions for automatically accepting webcam & mic permissions:
https://testingbot.com/support/selenium/permission-popups

These are actually using a fake video stream, that won't work for the purpose.

## Chromium flags

### CLI flags to fake video and mic streams

#### With file

#### With random data

## WebRTC server to connect to

Tested receiving and presenting WebRTC data from https://github.com/TannerGabriel/WebRTC-Video-Broadcast.git

## Testing power draw

### powertop

https://wiki.archlinux.org/title/powertop

- Crashes on both my AMD systems when trying to use the CSV output. Maybe because I didn't run enough on battery power?

### powerstat

### Perf counters

sudo cpupower frequency-set --governor performance
echo -1 | sudo tee /proc/sys/kernel/perf_event_paranoid

#### baseline (sleep for 10s)

perf stat -e power/energy-pkg/ sleep 10

#### Run chromium

perf stat -e power/energy-pkg/ chromium

#### Every second

perf stat -e power/energy-pkg/ -I 1000 chromium

# Example

## Setup:

# On a remote fixed host

## launch WebRTC server

docker run -d -p 4000:4000 webrtcvideobroadcast

# On test device

## set up perf_event support on test device

sudo cpupower frequency-set --governor performance
echo -1 | sudo tee /proc/sys/kernel/perf_event_paranoid

## Navigate to broadcast URL with test device to enable access to mic and video:

(sikulix to visit https://localhost:4000/broadcast.html and close itself)

## Test

- Run sleep N
- Run chromium without optimisation flags to visit broadcast.html
- Run chromium with optimisation flags to visit broadcast.html

4. Visit broadcast.html with perf stats on, no flags:

perf stat -e power/energy-pkg/ chromium http://localhost:4000/broadcast.html

perf stat -e power/energy-cores/,power/energy-ram/,power/energy-gpu/,power/energy-pkg/,power/energy-psys chromium https://localhost:4000/broadcast.html

5.  Close chromium after N seconds.

6.  Visit broadcast.html with perf stats on:
    perf stat -e power/energy-pkg/ timeout 10s chromium http://localhost:4000/broadcast.html

              3,674.97 Joules power/energy-pkg/

          34.606339526 seconds time elapsed

7.  Sleep for N seconds and do the same measurement:

    perf stat -e power/energy-pkg/ sleep 34

    Performance counter stats for 'system wide':

          3,274.36 Joules power/energy-pkg/

    34.001334823 seconds time elapsed
