from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import pandas
import geopy
from geopy.geocoders import ArcGIS
nom=ArcGIS()

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    global file
    if request.method=="POST":
        file=request.files["file_name"]
        #content=file.read()
        #print(content)
        file.save(secure_filename("uploaded"+file.filename))
        df=pandas.read_csv("uploaded"+file.filename)
        df.columns = map(str.lower, df.columns)
        df_col=df.columns
        if "address" in df_col:
            print("Yes")
            pos=df.columns.get_loc("address")
            print(pos)
            n = df["address"].apply(nom.geocode)
            df["Coordinates"] = n
            df["Latitudes"]= df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
            df["Longitudes"]= df["Coordinates"].apply(lambda x: x.longitude if x!= None else None)
            del df["Coordinates"]
            df_col1=df.columns
            df.to_csv("uploaded"+file.filename)
        else:
            print("Column not present")
        #with open("uploaded"+file.filename,"w") as f:
        #    f.write(df)
        return render_template("index.html", btn="download.html")

@app.route("/download")
def download():
    return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__=="__main__":
    app.debug=True
    app.run(port=5001)