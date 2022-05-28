import json
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine
from form import ContactForm
import requests
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
 'db': 'ventilator',
'host': 'localhost',
'port': 27017
}
db = MongoEngine()
db.init_app(app)


class ventilator(db.Document):
    name = db.StringField()
    capacity = db.StringField()
    price=db.IntField()
    make=db.StringField()
    mfdate =db.StringField()
  
    def to_json(self):
        return {"name": self.name,
                "capacity": self.capacity,
                "price":self.price,
                'make':self.make,
                'mfdatw':self.mfdatw,
                
                }


@app.route('/', methods=['POST'])
def create_record():
 
 record = json.loads(request.data)
 c = ventilator(name=record['name'],
        capacity=record['capacity'],
            price=record['price'],
            make=record['make'],
            mfdate=record['mfdate'],
            
            )
 c.save()
 return jsonify(c.to_json())

@app.route('/add',methods=['GET','POST'])
def add():
 form = ContactForm()  
 if request.method=="GET":
   return render_template("add.html",form=form)
 else:
      x={
            "name":request.form['name'],
            "capacity":request.form['capacity'],
            "price":request.form['price'],
            "make":request.form['make'],
            "mfdate":request.form['mfdate'],
   
         }
      
      y=json.dumps(x)
    
      response = requests.post(url="http://127.0.0.1:5000/",data=y)
      #loaded_json = json.loads(x)
      
      return render_template('x.html',a=x)
 
if __name__ == '__main__': 
 app.run(debug = True)
 