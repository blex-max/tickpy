# TickPy

Timer classes with a focus on periodic timing in while loops.


## Plausible extensions

Things I can/will implement at request or my need:
  - extend cmod (checking if a period has elapsed essentially) to optionally take a `period_start` parameter - effectively decoupling period tracking from the start time when desired, and returning False if .counter has not yet reached period start.
  - optionally autoupdate when calling cmod and so on. Almost certainly ill-advised for the applications I envisage using this module for however.


## Licence

GPL3 applies to all files and folders in this repo
