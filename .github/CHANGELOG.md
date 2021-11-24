# Changelog

## [0.0.3](https://github.com/certego/pydragonfly/releases/tag/0.0.3)

- Fixed "Please select at least one entrypoint" error in `Analysis.create` when uploading DLL samples.

## [0.0.2](https://github.com/certego/pydragonfly/releases/tag/0.0.2)

> Supports Dragonfly >= 1.0.6

- New resource class `Dragonfly.UserPreferences`.
- Update API URL in `Dragonfly.Analysis.create` function.
- New parameter `dll_entrypoints` in `Dragonfly.Analysis.CreateAnalysisRequestBody` dataclass. Support for same in the CLI.
- Update `EXPANDABLE_FIELDS` property in `Dragonfly.Report` class.

## [v0.0.1](https://github.com/certego/pydragonfly/releases/tag/v0.0.1)

- Initial Release.
