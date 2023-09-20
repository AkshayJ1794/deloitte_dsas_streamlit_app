Set objShell = CreateObject("WScript.Shell")

' Get the current directory
currentDirectory = CreateObject("Scripting.FileSystemObject").GetAbsolutePathName(".")

' Path to the Streamlit script (app.py in the same directory)
streamlitScriptPath = currentDirectory & "\app.py"

' Command to run Streamlit
command = "streamlit run """ & streamlitScriptPath & """"

' Run the command to start Streamlit
objShell.Run command, 1, True

