# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Slimmed the runtime dependencies so the package installs cleanly on Google
  Colab. `jupyterlab` and `ipykernel` moved out of the default `dependencies`
  into a new `local` optional extra. On Colab those packages are already
  provided by the host; pinning them forced an upgrade of Colab's own
  `ipykernel`/`jupyterlab`, which triggered a "Restart session" prompt and
  produced `google-colab` dependency-resolver conflicts. The bare
  `pip install vlab4micjupyter` (as run by the notebooks) now only pulls
  `vlab4mic`, `ipywidgets`, `ipympl` and `ezinput`. Local users install
  `vlab4micjupyter[local]` to also get a Jupyter server.

## [0.0.2] 2025-12-12

Add option to use a different fluorophore in a second probe

## [v0.0.1]

Initial release with functionalities from VLab4Mic (0.0.8)

### Fixed


### Added


### Changed

