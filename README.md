# fcSuite


fcSuite for ComfyUI Introduction

fcFloatMatic is a custom module, that when configured correctly will increment through the lines generating you loras at different strengths. The JSON file will load the config.

Installation

Download the fcsuite.py file from this repository.

Move the fcsuite.py file into the custom_nodes folder within your ComfyUI installation. The path should look something like: ComfyUI_windows_portable\ComfyUI\custom_nodes.

Start (or restart) ComfyUI to load the new fcFloatMatic custom node. It should now be available for selection from the node menu.

Usage

Once installed, you can use the fcFloatMatic node as follows:

text: Enter your text data here. The data should be formatted as a series of float values, separated by spaces or new lines. Note that lines beginning with # will be treated as comments and will be ignored.

seed: you can ignore this, its a special variable which will increment per generation

increment_step: keep this at 1

max_value: set this to the number of lines

The node returns a tuple containing two elements:

The selected float value. The string representation of the selected float value.

Support

For any issues or questions, feel free to raise an issue on this GitHub repository. Contributions and suggestions are also welcome!
