# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.12] - 2026-06-01

### Fixed
- Moved `jupyterlab` and `ipykernel` to a `local` optional extra to fix installation in Colab environments

## [0.0.11] - 2026-04-30

### Added
- Widgets for updating the imaging modality from the main panel

### Changed
- Updated widget values to reflect current modality parameters
- Updated PSF depth and sampling rate values in modality parameters
- Removed redundant messages when selecting modalities
- Fixed correct value assignment for using localisations
- Updated order of widgets in the select modality panel

## [0.0.10] - 2026-04-08

### Changed
- Use experiment method for structural integrity when passing parameters

## [0.0.9] - 2026-04-08

### Changed
- Probe widget: clarified the two options for using an example probe or creating one from a template

## [0.0.8] - 2026-04-02

### Added
- Button to relabel and plot a new labelled structure

## [0.0.7] - 2026-03-30

### Added
- Structure: checkbox to show the structure central axis
- Structure: entry point to change the central axis of a structure
- Text widget for global orientation of labelled particles in the virtual sample

### Changed
- Updated metric options to take values from defaults
- Use experiment method to select and build structure
- Changed order of widgets in virtual sample and categorised with headers
- Reduced stepsize in float sliders

## [0.0.6] - 2026-01-15

### Added
- Section for probe conjugation parameters and degree-of-labelling (DoL) widgets
- Option for probe template when customising a custom probe
- Extended description for the section to set the reference image

### Changed
- Renamed "Defect" to "Incomplete Labelling" and then to "Structural Integrity" throughout
- Set reference structure at structure selection
- Dropped support for Python 3.9
- Parameter sweep: add checkbox to use a list instead of a slider for value ranges
- Parameter sweep: change total values to stepsize for parameter ranges
- Parameter sweep: max value for stepsize is the max of the range
- Parameter sweep: report number of values when using sliders
- Parameter sweep: updated index numbering in slider ranges
- Set sliders with continuous update to false

## [0.0.5] - 2026-01-12

### Added
- Slider for frames when displaying simulation results

### Changed
- Renamed "Convolved Volume" to "Volume Projection" for option clarity
- Clarified text and headers for parameterising the virtual sample

### Fixed
- Fixed index to preview projections

## [0.0.4] - 2026-01-07

### Fixed
- Fixed missing label and results display
- Fixed all labels for missing tags in widgets
- Updated buttons across the package to use direct `widget.Button` instances
- Commented out all `continuous_update` parameters for widgets created with `ezinput`

## [0.0.3] - 2026-01-06

### Added
- Support for `sitespecific` and `sequence` as probe targets
- ExM as a parameter for the virtual sample
- Sample dimensions widget in the virtual sample panel
- Display modality options from experiment example modalities

### Fixed
- Fixed preview images
- Fixed parameters shown while previewing analysis results
- Bugfix for changing fluorophore configuration parameters
- Updated acquisition parameters in widgets to have all channels available
- Fixed update behaviour when selecting a custom probe with a fluorophore

## [0.0.2] - 2025-12-12

### Added
- Dropdown menu to select fluorophore in the probe widget
- Widgets to specify fluorophore parameters and save as local configuration
- Option to use a minimal probe as template when customising a probe
- Extra options for fluorophore parameters
- Support for saving custom fluorophore to the local configuration directory
- Check for local fluorophore configuration files
- Channels included in the acquisition parameters widget

## [0.0.1] - 2025-12-02

Initial release with functionalities from VLab4Mic (0.0.8).

