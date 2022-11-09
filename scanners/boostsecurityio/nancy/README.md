# boostsecurityio/nancy

## Environment Variables

### `OSSI_USERNAME`
Set the OSS Index username.

### `OSSI_TOKEN`
set the OSS Index API token.

### `NANCY_ARGS`
Extra arguments given to `nancy sleuth`.

### `GOPKG_LOCK`
Default: `Gopkg.lock`

Path to a custom `Gopkg.lock` file.

### `GO_LIST_PATH`
Default: `.nancy-go-list.json`

Path to the output of the command `go list -json -deps ./...`. If the file does not exist, Go is expected to be in the build environment to run `go list`.

