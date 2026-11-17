# print("Hello Gehlee")

# import - this is from python: used to load a module or library so we can use it.
# ifcopenshell: is a third-party Python library that allows us to open, modify, edit IFC files.
import ifcopenshell

# ifc_file is a variable to store the ifc file as opened using ifcopenshell
# ifcopenshell.open() this is an ifcopenshell library function that opens an ifc file and allows us to edit to manipulate it
# Just make sure that the BasicHouse.ifc does exist in the same folder as main.py
ifc_file = ifcopenshell.open("BasicHouse.ifc")

# print() is a Python command to display information in the terminal
# ifc_file.schema represents the IFC schema version IFC2X3 and IFC4
print("IFC File Loaded:", ifc_file.schema)

# walls is the variable to store all the information of all walls in our ifc file
# ifc_file.by_type: access all the walls in the loaded ifc file (ifc_file)
# .by_type() is from ifcopenshell: search for IFC entities by the indicated type (IfcWall)
walls = ifc_file.by_type("IfcWall")

# len() counts the items within a collection
# f allows us to create a string or message and embedded with code
# {len(walls)} allows us to print the number of alls walls we gathered from the ifc file.
print(f"Number of walls: {len(walls)}")


# loop - allows a repeat a task 
# for EACH wall in the walls collection/variable we will run a task
# wall - temporarily represents the current item (wall) being looped
for wall in walls:
    # .GlobalId identifies the specific IFC object (wall)
    # .Name stores the specific IFC object (wall)'s name
    print(wall.GlobalId, wall.Name)

# get all the IFCDoor entities from ifc file and save to doors variable
doors = ifc_file.by_type ("IfcDoor")
# get all the IFCDoor entities from ifc file and save to windows variable
windows = ifc_file.by_type("ifcWindow")

print(f"Doors: {len(doors)}")
print(f"Windows: {len(windows)}")

# 1. Get and save all the IfcSlab from our ifc files in the variable called slabs
# 2. Print and display the number of IfcSlab in our ifc file

slabs = ifc_file.by_type("IfcSlab")

print(f"Slabs: {len(slabs)}")

# Get and display the number of storeys and elevation: Explore the Spatial Structure
# project -> site -> building -> storey
# [0] is to get the first IfcProject
# Loop through all the sites, buildings to get and print all the storey and its elevation from the project
project = ifc_file.by_type("IfcProject")[0]

# loop through all the sites in the project
# loops through all the buildings in the sites
# loops through all the storeys and display its Name and Elevation
for site in project.IsDecomposedBy[0].RelatedObjects:
    for building in site.IsDecomposedBy[0].RelatedObjects:
        for storey in building.IsDecomposedBy[0].RelatedObjects:
            print("Storey", storey.Name, "Elevation", storey.Elevation)


# List all IFC type in our ifc file
# set is used to create a collection of unique values (will remove duplicated value)
# loop through all elements (el) in ifc_file, then for each element (el) use the is_a() method which returns the ifctype of an element
# types should then contain only unique ifctypes
types = set(el.is_a() for el in ifc_file)

# Print all ifctypes
print("Object types in file:", types)


# Change all the wall names in our IFC file.

# loop through all the walls in the ifc file
# enumerate() provide the index and an item (wall)
for i, wall in enumerate(walls,1):
    wall.Name = f"Renamed_Wall_{i}"
    print(f"Updated Wall: {wall.GlobalId} -> {wall.Name}")


# export the updated IFC file
# write() is used to create a new ifc file and inside it we add its new name 
ifc_file.write("BasicHouse_Updated.ifc")