# VSCODE DEBUGGING CONFIGURATIONS

---

This repository is a collection of Optimal `Debugging` configurations for [Visual Studio Code](https://code.visualstudio.com/). Developers face a hard time setting up debuggers for there application in `Visual Studio Code` due to complex launch and task configuration that changes per `platform`.

This repository has optimal debugging configurations for below:

- [nodejs (javascript)](nodejs_debug)
  - [Debugger with restart configuration](nodejs_debug/.vscode/launch.json#L6)
  - [Debugging with Docker](nodejs_debug/.vscode/launch.json#L20)
  - [Attaching debugger to existing server](nodejs_debug/.vscode/launch.json#L35)
- [nodejs (typescript)](nodets_debug)
  - [Debugging with restart configuration](nodets_debug/.vscode/launch.json#L7)
  - [Debugging without restart configuration](nodets_debug/.vscode/launch.json#L40)
- [reactjs (javascript)](react-debug)
  - [Debugging ReactJs with Chrome](react-debug/.vscode/launch.json#L6)
  - [Debugging ReactJs with msEdge](react-debug/.vscode/launch.json#L16)
- [python](python_demo)
  - [FastAPI Debug configuration](python_debug/.vscode/launch.json#L8)
  - [Flask Debugging configuration](python_debug/.vscode/launch.json#L21)
  - [Flask Debugging configuration with Flask Cli](python_debug/.vscode/launch.json#L31)
  - [Debugging Python Application in Docker](python_debug/.vscode/launch.json#L48)
