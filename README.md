# TickPy

Convenient timing classes with a focus on periodic timing in while loops.

The bulk of this module is given to `Ticker` classes - counters which increment tracking a given period. Much like a counter you might find on low-resource chip, when working on embedded applications. By example, if you set up a ticker with a period of 10ms, and in each iteration of your main loop you call .update() on the ticker, each time 10ms has elapsed the ticker will increment it's counter by 1. This is combined with various conveniences, such as functions for checking 'how long since' or 'has this period elapsed' and so on.

There are two flavours of `Ticker`, each with a slightly different sense of time. `FreeTicker` will increment it's counter by as many periods have passed since last updated - most accurately approximating an independent timer on a chip. `IncTicker` will only ever increment it's counter by 1 for each call to .update() - this is convenient if you don't want to bother worrying about what happens if the timer skips. Each flavour also has an extended child class, `Ext...Ticker` - this class adds some slightly more complicated state tracking of periods checked, to avoid reporting that a period has elapsed more than once for a given loop.

Also provided are some very simple `Timer` classes, which just track time without any period internal sense of period. These are `StaticTimer`, where `now` is fixed to the last time the timer was updated, and `Timer`, where `now` is always right now. These come with a couple of convience functions each, though these are less extensive than those present for the Tickers.

All classes rely on `time.perf_counter()` for reasonably accurate timing. This is the reason for the reliance on `python 3.13`, since the underlying implementation of `perf_counter()` has changed since `3.12`

I developed this module to use when working with finite state machines, or in other words programs where the main function is a long-running while loop. My applications are usually pretty simple; most often I'm prototyping what may become a C program on a chip - this module lets me approximate that scenario pretty quickly. It's all pretty simple stuff in here and it's a very small library - have a quick read of the code in the `tickpy/` dir.

## Dependencies

- `python >= 3.13`

## Installation

The latest version is available via PyPi for standard installation, e.g.
```
pip install tickpy
```
or however is most appropriate for your needs.

From source or a github release:
```
poetry install
```
or
```
pip install .
```

## Testing

A test suite with approximately complete coverage is available for this repo. It is implemented with pytest.

## Plausible extensions

Things I can/will implement at request or my need:
  - ensure compatibility with some older versions of python3
  - extensions to period checking functions for both timer and ticker classes
    - extend ticker .cmod() to optionally take a `period_start` parameter - effectively decoupling period tracking from the start time when desired, and returning False if .counter has not yet reached period start.
  - optionally autoupdate when calling cmod and so on. Almost certainly ill-advised for the applications I envisage using this module for however.

## Licence

GPL3 applies to all files and folders in this repo.
