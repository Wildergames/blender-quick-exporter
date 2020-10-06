# Blender Quick Exporter
A Blender addon which allows users to configure exportable packages from objects within a blender file. These `export packages` can be exported manually and/or automatically as individual FBX files.

This addon is intended to be a set-it-and-forget-it solution to FBX exporting. Once you've created and configured your export packages, you shouldn't need to change and of the Quick Exporter settings very often. Simply modify your mesh, and press the one of the Export buttons.

# Quick Start
1. Install addon
2. Open addon Panel `(View3D > Sidebar > Quick Exporter)`
3. Create a new `'Export Package'`
4. Add a `name` to the new 'Export Package'
5. Add a `path` to export your package to.
6. Add an `object` (or multiple) to the 'Export Package'
7. If necessary, modify the 'Export Package' settings
8. Click one of the two `Export` buttons

Now you have an 'Export Package' which will always export the objects you've specified to the location specified, with one click of a button.


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

# Blender Development Lifehacks
We decided to throw these in here so they aren't forgotten, as blender scripting can sometimes be a bit frustrating.

## Reload Scripts Shortcut
Add a `Reload Scripts` shortcut to Blender from `Edit > Preferences > Keymap` by adding a new item to the `Window` category, with the script text set to `script.reload`

We disable `Repeat` and use `F8` as the shortcut key.  

## Toggle Console Shortcut
Add a `Toggle Console` shortcut to Blender from `Edit > Preferences > Keymap` by adding a new item to the `Window` category, with the script text set to `wm.console_toggle`

We disable `Repeat` and use `F9` as the shortcut key.  

## Symlinking Addon Directories
Symlink the `src` directory to a directory in the Blender addons folder to avoid having to manually copy+paste your addon into the Blender addons folder every time you make a change to your scripts.

**Windows** - From the command line, use the following command:  
`mklink /J "C:\Users\{USERNAME}\AppData\Roaming\Blender Foundation\Blender\{BLENDER_VERSION}\scripts\addons\quick-exporter" "./src"`

**MacOS** - From the Terminal, use the following command:  
`ln -s './src' 'Macintosh HD/Users/{USERNAME}/Library/Application Support/Blender/{BLENDER_VERSION}/scripts/addons/quick-exporter'`

## Module Reloading
Use importlib.reload(module) to reload addon modules when scripts are reloaded, otherwise Blender will cache your scripts and won't update until you restart the editor. This, combined with the `Reload Scripts Shortuct` tip above make development much quicker.

```python
# Check if your scripts have already been imported
# If true, reload instead of importing

import bpy

if "x" not in locals():
	from . import x, y, z
	print("Quick Exporter: Importing")
else:
	import importlib
	x = importlib.reload(x)
	y = importlib.reload(y)
	z = importlib.reload(z)
	print("Quick Exporter: Reloading Scripts") 

# replace x y z with your own script names
# It's not elegant, but it does the job!
```

## Quickly Find the Right Documentation
Check the built-in templates first! Located at `Text Editor > Templates` - This has a lot of great examples of common functionality.

When looking for Blender scripting documentation, search for `bpy.{namespace}`. This  will usually show scripting pages, instead of usage docs and tuts.

Also, it seems as if searching for the *namespace* of an class instead of the class's name will sometimes yield better search results!
