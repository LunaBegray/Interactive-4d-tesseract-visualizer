---

# 4D Tesseract Interactive Visualization

This program visualizes a 4-dimensional tesseract (hypercube) in a 3D space, using pygame and numpy to handle the graphics and calculations. The tesseract can be interactively rotated on multiple axes and zoomed in and out, providing an intuitive way to explore 4D geometry in a 3D projection.

## Features
- **Interactive Rotation**: Rotate the tesseract in 4D space along multiple axes using mouse movements or keyboard inputs.
- **Zoom**: Zoom in and out with the mouse wheel to explore the tesseract from different distances.
- **UI Controls**: Display and adjust the rotation speed and zoom factor using on-screen information.
- **Smooth Animation**: Continuous rotation in multiple directions for a dynamic 3D effect.

## Requirements

- **Python 3.x**
- **pygame**: For rendering the graphical window and handling user input.
- **numpy**: For performing mathematical operations such as matrix multiplication and transformations.

You can install the required libraries using `pip`:

```bash
pip install pygame numpy
```

## Running the Program

To run the program, simply execute the Python script:

```bash
python tesseract_visualization.py
```

### Controls
- **Mouse**:
  - **Left Mouse Button**: Click and drag to rotate the tesseract along the `XZ` and `YW` axes.
  - **Right Mouse Button**: Toggle the on-screen UI to adjust rotation speed and zoom.
  - **Mouse Wheel**: Zoom in and out to change the perspective.
  
- **Keyboard**:
  - **Arrow Keys**: Use the arrow keys to rotate the tesseract along the `XZ` and `YW` axes manually.
  - **Zoom**: The zoom factor can also be controlled with the mouse wheel (or using keyboard shortcuts if you modify the script).
  
### UI Info Display
When the UI is toggled on:
- **Rotation Speed**: Displays the current speed of the tesseract’s rotation.
- **Zoom Factor**: Displays the current zoom level affecting the 3D projection.

## How It Works

### 4D to 3D Projection
The program simplifies the 4D tesseract's 16 vertices and uses rotation matrices to rotate these vertices in 4D space. After applying the rotations, the 4D vertices are projected into 3D space using a perspective divide, creating a 3D view of the 4D object. The zoom factor adjusts the depth of this projection.

### Rotation
- The program allows the tesseract to rotate along four axes:
  - `XZ`: Rotation in the `X` and `Z` plane.
  - `YW`: Rotation in the `Y` and `W` plane.
  - `ZW`: Rotation in the `Z` and `W` plane.
  - `XY`: Rotation in the `X` and `Y` plane.
  
By combining these axes, the tesseract can be rotated in more complex ways, providing a dynamic and evolving visualization.

### Customization
You can easily modify the program by changing constants and functions:
- **Rotation speed**: Modify `rotation_speed` to control how quickly the tesseract rotates.
- **Zoom**: Adjust the `zoom_factor` to control the level of zoom applied during projection.
- **Color and Styling**: Customize the appearance by altering the `BACKGROUND_COLOR`, `LINE_COLOR`, and `LINE_WIDTH`.

---
