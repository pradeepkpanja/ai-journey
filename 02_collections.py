#to create a list [] is used and to create a tuple () is used
# List of favourite tools
favourite_tools = ["VSCode", "PyCharm", "Jupyter Notebook", "Sublime Text", "Atom"]

print("Favourite Tools:", favourite_tools)
favourite_tools.append("Notepad++")
print("Updated Favourite Tools:", favourite_tools)
favourite_tools[2] = "Scikit-learn"
print("Final Favourite Tools:", favourite_tools)


#Tuple of favourite tools

favourite_tools_tuple = ("VSCode", "PyCharm", "Jupyter Notebook", "Sublime Text", "Atom")

print("Favourite Tools Tuple:", favourite_tools_tuple)
favourite_tools_tuple = favourite_tools_tuple + ("Notepad++",)
print("Updated Favourite Tools Tuple:", favourite_tools_tuple)
print("Length of Favourite Tools Tuple:", len(favourite_tools_tuple))

#Dictionary of favourite tools

favourite_tools_dict = {
    "VSCode": "Code Editor",
    "PyCharm": "IDE for Python",
    "Jupyter Notebook": "Interactive Computing",
    "Sublime Text": "Text Editor",
    "Atom": "Hackable Text Editor"
}

print("Favourite Tools Dictionary:", favourite_tools_dict)

favourite_tools_dict["VSCode"] = "Favourite Code Editor"
print("Updated Favourite Tools Dictionary:", favourite_tools_dict)

favourite_tools_dict["Notepad++"] = "Text Editor"
print("Final Favourite Tools Dictionary:", favourite_tools_dict)