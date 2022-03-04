# rgiro_sweethome3d_worlds

The `rgiro_sweethome3d_worlds` ROS package provides a collection of Gazebo worlds exported from home interior designs made on Sweet Home 3D: [http://www.sweethome3d.com/](http://www.sweethome3d.com/).

*   Maintainer: Shoichi Hasegawa ([hasegawa.shoichi@em.ci.ritsumei.ac.jp](mailto:hasegawa.shoichi@em.ci.ritsumei.ac.jp)).
*   Author: Shoichi Hasegawa ([hasegawa.shoichi@em.ci.ritsumei.ac.jp](mailto:hasegawa.shoichi@em.ci.ritsumei.ac.jp)).

**Content:**

[[_TOC_]]

## Overview

| Type 1: Rooms with different content          | Type 2: Rooms with similar content           |
| --------------------------------------------- |--------------------------------------------- |
| Example: 2LDK                                 | Example: 2LDK                                |
| ![](sources/type_1/2ldk/2ldk_01/2ldk_01.jpeg) | ![](sources/type_2/2ldk/2ldk_01/2ldk_01.png) |

## Getting Started

Add the Gazebo models of the `rgiro_sweethome3d_worlds` ROS package to the `GAZEBO_MODEL_PATH` of your shell environment.

```shell
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:/path/to/rgiro_sweethome3d_worlds/models/
```

You can also execute the Gazebo worlds found in `worlds/` with, for example:

```shell
gazebo /path/to/rgiro_sweethome3d_worlds/worlds/type_2/1ldk/1ldk_01/ldk_01.world
```

## Submodule Integration

Assuming that SSH access has been granted:

```shell
git submodule add -b devel --name rgiro_sweethome3d_worlds git@gitlab.com:emlab/packages/rgiro_sweethome3d_worlds.git catkin_ws/src/rgiro_sweethome3d_worlds
```

Assuming that HTTPS access has been granted:

```shell
git submodule add -b devel --name rgiro_sweethome3d_worlds https://gitlab.com/emlab/packages/rgiro_sweethome3d_worlds.git catkin_ws/src/rgiro_sweethome3d_worlds
```

Make sure that the `devel` branch is tracked.

## Create New Worlds

1.   Install Sweet Home 3D and create a new layout: [http://www.sweethome3d.com/](http://www.sweethome3d.com/).
2.   Export the newly created layout as an `.obj` meshe file.
3.   Import the `.obj` meshe into the a new Gazebo `.sdf` model file.
4.   Adjust the scale, position, visual, and collision properties in the `.sdf` file.
5.   Finally, include the newly created `.sdf` file into a new Gazebo `.world` file.

**Note:** It seems that the unit and coordinate systems of Sweet Home 3D cannot be modified: [https://sourceforge.net/p/sweethome3d/bugs/584/](https://sourceforge.net/p/sweethome3d/bugs/584/).

## Contribution Guidelines

This repository strictly enforces file name conventions.
Please use prefixes to distinguish 1st-party resources from 3rd-party ones.
Also, all file names should follow the ROS conventions: use small characters and underscores `_` exclusively.

For example, the prefix `rgiro_` is added to the file names of worlds and models made by Ritsumeikan Global Innovation Research Organization (R-GIRO) while `sh3d_` and `3rd_` indicate Sweet Home 3D and 3rd-party resources, respectively.

## Sources

The Sweet Home 3D source files found in `sources/` have been imported from the `SweetHome3D_rooms` dataset: [https://github.com/EmergentSystemLabStudent/SweetHome3D_rooms](https://github.com/EmergentSystemLabStudent/SweetHome3D_rooms).

This dataset includes several room layouts originally created by the Emergent Systems Laboratory, Ritsumeikan University, for simulations using Unity.
The Sweet Home 3D data in `sources/` were copied from the commit [d6b18deb](https://github.com/EmergentSystemLabStudent/SweetHome3D_rooms/tree/d6b18deb697616392b68625f70ea3d63d5fb053c) and exported into meshes compatible with Gazebo.

## References

*   Sweet Home 3D official website: [http://www.sweethome3d.com/](http://www.sweethome3d.com/).
*   Sweet Home 3D introduction (ja): [https://bibinbaleo.hatenablog.com/entry/2017/03/29/173121](https://bibinbaleo.hatenablog.com/entry/2017/03/29/173121).
