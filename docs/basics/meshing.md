# Meshing

Llama integrates [Gmsh](https://gmsh.info/) for tetrahedral mesh generation.

## Tetra Mesh

The **Gmsh Tetra Mesh** component generates a tetrahedral mesh from a geometry file. It supports **STEP**, **IGES**, and **STL** input formats. STEP and IGES files are processed with the OpenCASCADE geometry kernel, while STL files use Gmsh's built-in kernel.

Llama automatically locates the Gmsh executable on your system. If it cannot be found, you can provide the path manually.

### Parameters

| Input               | Description                                          |
| ------------------- | ---------------------------------------------------- |
| Geometry File       | Path to the geometry file (`.step`, `.iges`, `.stl`) |
| Min Size            | Minimum characteristic element length                |
| Max Size            | Maximum characteristic element length                |
| Element Order       | Element order (1 = linear, 2 = quadratic)            |
| Algorithm 3D        | 3D meshing algorithm                                 |
| Optimize            | Enable mesh optimization                             |
| Optimize Netgen     | Enable Netgen optimization                           |
| Smoothing           | Number of smoothing steps                            |
| High Order Optimize | Optimization level for high-order elements           |

### Output

A tetrahedral mesh that can be converted to a Llama structural model using the **Tetra Mesh to Model** component.

## Hex Mesh

Hexahedral meshes can be imported from external tools and converted using the **Hex Mesh to Model** component.
