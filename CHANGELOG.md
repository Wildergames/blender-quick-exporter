# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Check [README.md](README.md) for planned changes.

---

## [1.1.0] - 2021-05-26

### Added
- Added support for Collections, which will include all enabled Objects within each added Collection in the exported file.


---

## [1.0.3] - 2021-03-30

### Fixed
- Export path without a `.fbx` extension resulted in exporting a nameless `.fbx` file. Now if no filename ending in `.fbx` is found in the export path, the exported filename will default to `{package.name}.fbx`. 

---

## [1.0.2] - 2020-10-18

### Changed
- Added author and license info header comments to python files

---

## [1.0.1] - 2020-10-06

### Changed
- Moved UI from `Properties > Scene` to `View3D > Sidebar`

### Fixed
- fixed error when exporting from any context besides `OBJECT`

---

## [1.0.0] - 2020-10-01

### Initial release

🙂