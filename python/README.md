# How to Use

---

- Click on the debug Icon on the left/right menu bar in `vscode`.
- Select Debugging configuration from the drop downs.
  ![Drop Down Image](screenshots/select_panel.png)

- Click on the play button next to `RUN AND DEBUG` to start debugger.
- Put the break points in you code and enjoy.
  ![Debugger](screenshots/Debugger.png)

> For Attach Docker Debugging configuration, you would require `Docker Desktop` to be running. For best experience, have [Docker Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) installed.

## Using Debugger

- Once you plug in debugger you would get below toolbar on the top center of you pane.

  ![toolbar](screenshots/toolbar.png)

- Use below controls to Debug your code.

  | Action                |                                                                             Explanation                                                                             |
  | :-------------------- | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
  | Continue / Pause `F5` |                                            Continue: Resume normal program/script execution (up to the next breakpoint).                                            |
  |                       |                                              Pause: Inspect code executing at the current line and debug line-by-line.                                              |
  | Step Over `F10`       |                                  Execute the next method as a single command without inspecting or following its component steps.                                   |
  | Step Into `F11`       |                                                     Enter the next method to follow its execution line-by-line.                                                     |
  | Step Out `⇧F11`       | When inside a method or subroutine, return to the earlier execution context by completing remaining lines of the current method as though it were a single command. |
  | Restart `⇧⌘F5`        |                               Terminate the current program execution and start debugging again using the current run configuration.                                |
  | Stop `⇧F5`            |                                                              Terminate the current program execution.                                                               |

- For more info, you can refer [`VSCode Official Docs`](https://code.visualstudio.com/docs/editor/debugging).

---

Happy Debugging ! 😀
