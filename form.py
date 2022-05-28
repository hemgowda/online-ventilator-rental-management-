from flask_wtf import Form 
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField 
from wtforms import validators, ValidationError 
from flask import Flask, render_template, request, flash
 
class ContactForm(Form): 
 name = TextField("Name ",[validators.Required("Please enter your name.")]) 
 capacity = TextField("capacity",[validators.Required("Please enter your capacity of ventilator.")])   
 price = SelectField('price', choices = [('1000', '1000'),('2000', '2000'),('5000', '5000'),('10000', '10000'),]) 
 make = TextField("make ",[validators.Required("Please enter required field")])
 mfdate = TextField("mfdate ",[validators.Required("Please enter required field")]) 
 submit = SubmitField("Submit") 