# What is Quick Exporter?
Quick Exporter is a **free** Blender addon by [Wilder](https://wilder.games), which allows users to configure and manage exportable packages from objects within a Blender file.

These **Export Packages** can be exported manually and/or automatically, as a single or individual FBX files.

This addon is intended to act as a **set-it-and-forget-it** solution to FBX exporting.

Once you've created and configured your export packages, you shouldn't need to change the Quick Exporter settings very often. Simply make changes, click Export, and you're done.

<br>

<p float="left">
  <img src="screenshots/001.png" width="24%" />
  <img src="screenshots/002.png" width="24%" /> 
  <img src="screenshots/003.png" width="24%" />
  <img src="screenshots/004.png" width="24%" />
</p>

<br>

# What does it accomplish?
**In Blender?**  
Quick Exporter allows for faster, easier, and more straightforward exporting from Blender. It saves your export data (including settings, locations, objects to include) and delegates all the work of remembering or coordinating this information into a handy editor panel.

**For game development?**  
Instead of importing your *.blend* files directly into your projects, or using Blender's built-in (but non-persistent) *Export To* functions, Quick Exporter allows you to set up an asset pipeline which disconnects your source files from your asset files. The benefit of this being: More control over export settings, locations, and update frequency.

<br>

# Free, huh?
Heck yeah, **100% free**.

That said, any donations are highly appreciated.

Donations and purchases help us continue to support our tools for the game development community.

<br>

# Source Code  
As a Blender addon, the Quick Exporter source code is bundled with every version. 

Officially, Quick Exporter is available for download from [github](https://github.com/wildergames/blender-quick-exporter) and [itch.io](https://wilder-games.itch.io/blender-quick-exporter)

For more information, visit the Wilder website: [wilder.games](https://wilder.games)

<br>

## License
We haven't yet chosen a license for Quick Exporter.

<br>

## Open Source Considerations
We're new to open-source, so please, bear with us!

We'd love to allow the community to be involved with the continued development of Quick Exporter and our other tools in the future, but we couldn't decide the best way to do so.

If you have any suggestions on which license we should be using, please let us know.

<br>

---

<br>

# How to Use
Using Quick Exporter is intended to be quick and easy. 

<br>

## Quick Start
1. Install addon
2. Open addon panel *(View3D > Sidebar > Quick Exporter)*
3. Create a new *'Export Package'*
4. Add a *name* to the new export package
5. Add a *path* to export your package to
6. Add any number of *objects* to the new export package
7. If necessary, modify the export settings
8. Click one of the two *Export* buttons, or enable *Auto-Export*

That's it.

Now you have an Export Package which will always export the objects you've specified to the location specified, using the settings specified. This can be done with one click of a button, or when the file is saved.

<br>

## Installation
This addon can be installed by copying the contents of *quick-exporter.zip* into your Blender addons directory.

Make sure to copy the entire *quick-exporter* directory to your Blender addons directory.

<br>

## The 'Quick Exporter' Panel
This addon is controlled from a single panel in Blender, located at:  
*3D Viewport &gt; Sidebar &gt; Quick Exporter*

<br>

## Creating an Export Package
An *'Export Package'* is a collection of Blender scene objects intended to be exported to a single .fbx file.

From the Quick Exporter panel, you can create a new export package from the package list. With this complete, you'll be able to set all the necessary .fbx export settings, as well as a path for your exported .fbx file.

<br>

## Exporting an Export Package
Once you've created and configured one or more export packages, the *Export All* button will export all packages to their intended locations.

Alternatively, you may select an individual package from the list, and click the *Export 'Package'* button, where 'Package' is the name of your selected package.

<br>

## Auto-Export
In the Quick Exporter panel, there is an option to enable auto-exporting on save. You can choose one of the following options:

**Disabled**  
This will prevent Quick Exporter from automatically exporting on save. This is the default auto-export setting. With this option selected, users are required to manually use the <em>Export</em> buttons through the Quick Exporter interface.

**Auto-Export On Save**  
This will export all packages when the Blend File is saved.

<br>

---

<br>

# Planned Features
We're planning on adding more features to Quick Exporter in the future, including:

**Export Settings data objects**  
Adding the ability to store and reference various embedded Export Settings objects (just like Materials, or Textures), instead of having one unique set of settings per Export Package. This would allow us to also store defaults for various export platforms and variations. For example: FBX Standard, Unity, Unity (Animated), Unreal, etc.

**Support for more export file types**  
Adding support for exporting more than just .fbx files.

---

<br>
