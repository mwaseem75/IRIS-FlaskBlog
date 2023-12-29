Class dc.flaskblog [ Abstract ]
{

ClassMethod init(tPath, tName, tDescription = "") As %Status
{
 write !,"=============================="
 write !," The project is installed. Go to directory"
 write !,"   cd "_$G(tPath)
write !," set the environment variable if necessary"
 write !,"   python3 -m venv env"
 write !,"   source env/bin/activate # for Linux"
 write !,"   source env/Scripts/activate # for Windows"
 write !,"   pip3 install -r requirements.txt"
 write !," if necessary, correct the IRIS access parameters in the file "_$G(tPath)_"/website/myconfig.py"
 write !," run the application ",!,"   python3 app.py"
write !,"=============================="
 quit $$$OK
}

}

