Class dc.flaskblog [ Abstract ]
{

ClassMethod init(tPath, tName, tDescription = "") As %Status
{
 write !,"The project is installed. Go to directory"
 write !,"cd "_$G(tPath)
 write !,"python -m venv env"
 write !,"source env/bin/activate # for Linux"
 write !,"source env/Scripts/activate # for Windows"
 write !,"pip install -r requirements.txt"
 write !,"if necessary, correct the IRIS access parameters in the file "_$G(tPath)_"/website/myconfig.py"
 write !,"run the application ",!,"python3 app.py"
 quit $$$OK
}

}

