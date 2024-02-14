# VS Code configurations for svelte

The launch configuration uses the environment variable `NODE_PATH` to determine the node executable used for debugging. This is useful when using a version manager like `nvm` or `n` to manage multiple versions of node.

```bash
export NODE_PATH=$(which node)
```

If using NVM, the following command can be used to set the `NODE_PATH` environment variable to the current version of node.

```bash
export NODE_PATH=$(nvm which current)
```

## Adding to project

```bash
cd my-svelte-project
degit satyamsoni2211/vscode_debugging_configurations/svelte .vscode
```
