# TickPy

Timer classes with a focus on periodic timing in while loops.

# Usage

I use this module when I'm working with finite state machines, or in other words programs where the main function is a long-running while loop. My applications are usually pretty simple; most often I'm prototyping what will become a C program on a chip in python - this module lets me approximate that scenario pretty quickly.

It's all pretty simple stuff in here and it's a very small library - have a quick read of the code in the tickpy/ dir. In short, tickers are counters that update over a given interval, and timers track time in a more traditional sense. In both cases, functions are provided for operations like 'how long since' or 'has this period elapsed', and so on.

# Testing

A test suite with complete coverage is available for this repo. It is implemented with pytest.

## Plausible extensions

Things I can/will implement at request or my need:
  - extensions to period checking functions for both timer and ticker classes
    - extend ticker .cmod() to optionally take a `period_start` parameter - effectively decoupling period tracking from the start time when desired, and returning False if .counter has not yet reached period start.
  - optionally autoupdate when calling cmod and so on. Almost certainly ill-advised for the applications I envisage using this module for however.

## Licence

GPL3 applies to all files and folders in this repo.
