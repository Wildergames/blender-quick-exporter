# Blender Quick Exporter
A **free** Blender addon which allows users to configure and manage exportable packages from objects within a Blender file. These `Export Packages` can be exported manually and/or automatically as individual FBX files.

This addon is intended to be a set-it-and-forget-it solution to FBX exporting. Once you've created and configured your export packages, you shouldn't need to change the Quick Exporter settings very often. Simply make changes, click Export, and you're done!

Visit the [**Blender Quick Exporter** itch.io page](https://wilder-games.itch.io/blender-quick-exporter) for more information.

# Quick Start
A small number of steps to quickly begin using Quick Exporter:
1. Install addon
2. Open addon Panel `(View3D > Sidebar > Quick Exporter)`
3. Create a new `'Export Package'`
4. Add a `name` to the new 'Export Package'
5. Add a `path` to export your package to.
6. Add an `object` (or multiple) to the 'Export Package'
7. If necessary, modify the 'Export Package' settings
8. Click one of the two `Export` buttons

Now you have an 'Export Package' which will always export the objects you've specified to the location specified. This can be done with one click of a button, or when the file is saved.


# Installation
This addon is installed by copying the src directory into your Blender addons directory, as `quick-exporter`


# How to Use

## The 'Quick Exporter' Panel
This addon is controlled from a single panel in Blender, located at: `3D Viewport > Sidebar > Quick Exporter`


## Creating an Export Package
An `Export Package` is a collection of Blender scene objects intended to be exported to a single .fbx file. 

From the Quick Exporter panel, you can create a new export package from the package list.

Once you've done that, you'll be able to set all the necessary .fbx export settings, as well as a path for your exported .fbx file.

Once you've set up an export package, you shouldn't need to modify it again.


## Exporting an Export Package
Once you've created and configured one or more export packages, the `Export All` button will export all packages to their intended locations.

Alternatively, you may select an individual package from the list, and click the `Export 'Package'` button, where "Package" is the name of your selected package.


## Auto-Export
In the Quick Exporter panel, there is an option to enable auto-exporting on save. You can choose one of three options:

- `Disabled` - This will prevent Quick Exporter from automatically exporting on save. This is the default auto-export setting. With this option selected, users are required to manually use the `Export` buttons through the Quick Exporter interface.

- `Auto-Export On Save` - This will export all packages when the Blend File is saved.

---

# License
NONE YET

---

# Planned Features
We're planning on adding more features to Quick Exporter in the future, including:

**Export Settings data objects**  
One major change we can see being useful would be the ability to store and reference various Export Settings objects (just like Materials, or Textures), instead of having one unique set of settings per Export Package. This would allow us to also store defaults for various export platforms, like Unity and Unreal.

**Support for more export file types**  
We're planning to eventually add the ability to use Quick Exporter to export more than just .fbx files.

---
