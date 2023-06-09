# VSCODE DEBUGGING CONFIGURATIONS

---

This repository is a collection of Optimal `Debugging` configurations for [Visual Studio Code](https://code.visualstudio.com/). Developers face a hard time setting up debuggers for there application in `Visual Studio Code` due to complex launch and task configuration that changes per `platform`.

This repository has optimal debugging configurations for below:

- [nodejs (javascript)](javascript)
  - [Debugger with restart configuration](javascript/.vscode/launch.json#L6)
  - [Debugging with Docker](javascript/.vscode/launch.json#L20)
  - [Attaching debugger to existing server](javascript/.vscode/launch.json#L35)
- [nodejs (typescript)](typescript)
  - [Debugging with restart configuration](typescript/.vscode/launch.json#L7)
  - [Debugging without restart configuration](typescript/.vscode/launch.json#L40)
- [reactjs (javascript)](react)
  - [Debugging ReactJs with Chrome](react/.vscode/launch.json#L6)
  - [Debugging ReactJs with msEdge](react/.vscode/launch.json#L16)
- [python](python)
  - [FastAPI Debug configuration](python/.vscode/launch.json#L8)
  - [Flask Debugging configuration](python/.vscode/launch.json#L21)
  - [Flask Debugging configuration with Flask Cli](python/.vscode/launch.json#L31)
  - [Debugging Python Application in Docker](python/.vscode/launch.json#L48)

For Official Documents on debugging with `Visual Studio Code`, refer [here](https://code.visualstudio.com/docs/editor/debugging).

---

## Tips to use

- Just copy over `.vscode` folder in your projects.
- Every `.vscode` folder contains `launch.json` configuration file and `tasks.json` file for automated tasks.
- Once, the folder is copied over, you would be able to see, debugging configurations under the `RUN AND DEBUG` section in the control pane.
  ![Debugger](screenshots/Screenshot%202023-04-26%20at%207.38.01%20PM.png)
- Select the appropriate configuration and launch.

## Contributing

---

- Fork the Repository and create a new `feature` / `hotfix` branch.
- Make you Code changes / Add a new configuration.
- Please use proper `Linting` and `Formatting` in your code.
- Raise a PR, I will review and merge the source code.
- Reach out to me if you wanna be one of the collaborators.

## License

---

`VSCODE Debugger Configurations` is released under the **MIT**.

**tl;dr**: _"free to use as long as you credit me"_.

---

Happy Debugging !😀

Made with Love by [@satyamsoni](https://github.com/satyamsoni2211).
