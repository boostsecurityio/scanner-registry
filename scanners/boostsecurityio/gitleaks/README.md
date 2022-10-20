# boostsecurityio/codeql

## Environment variables

### `GITLEAKS_CONFIG`
By default GitLeaks will look for a configuration file named `.gitleaks.toml` at the root of the repository. If the configuration is placed elsewhere, use `GITLEAKS_CONFIG` to set the path in the repository to the GitLeaks configuration to use.

If no configuration is provided, GitLeaks will use its default configuration file.
