# Installation

Grasshopper is a visual programming language for Rhino3D, a popular 3D modelling software.
You can install Llama using the **Package Manager**.

## Package Manager

1. Open Rhino3D and launch the **Package Manager** from the _Tools_ menu — or click the [link](rhino://package/search?name=Llama).

2. Search for **Llama** and click **Install**. The Package Manager will download and install the plugin.
3. Restart Rhino3D to activate the plugin.

!!! note
    If you have correctly followed the steps above, you will find the **Llama** tab on the Grasshopper toolbar.

## Install CalculiX

Llama requires a [CalculiX](http://www.calculix.de/) (`ccx`) executable to run analyses.

1. Download CalculiX from [calculix.de](http://www.calculix.de/) or use a prebuilt binary such as [bConverged](https://bconverged.com/calculix/).
2. Install or extract the executable on your machine.

!!! note
    Llama will automatically try to detect the CalculiX executable on your system. If it cannot be found, you can manually set the path in the **Run with Exe** component.
