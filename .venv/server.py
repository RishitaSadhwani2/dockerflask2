#Student Name-Rishita Sadhwani
#ASU ID-1234157173
#DATE -November 30,2024
from flask import Flask,render_template,request,redirect,url_for

hardware_resources={
    "Stove":"Available",
    "Oven":"Available",
    "Mixer":"Available",
    "Knife":"Available"
}

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('Index.html',resources=hardware_resources)
    


    
@app.route('/resource/<tool>',methods=['GET'])
def request_resource_web(tool):
    if hardware_resources.get(tool)=="Available":
        hardware_resources[tool]="Occupied"
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=9001)