from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__)

app.config['SECRET_KEY'] = 'codingelements'

class CounterForm(FlaskForm):
	textbox = TextAreaField('Text', validators=[DataRequired()])
	submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
	form =  CounterForm()
	
	if form.validate_on_submit():
		sentence = form.textbox.data
		result = str(len(sentence.split()))
		# print(sentence)
		flash("Changes Done")
		return render_template('index.html', form=form, result = result)
	return render_template('index.html', form=form)


if __name__=='__main__':
	app.run(debug=True)