from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import flat
import result
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)
class Word(db.Model):
	word = db.Column(db.String(200), nullable=False, primary_key=True)
	def __repr__(self):
		return '<Task %r>' % self.id
class Definition(db.Model):
	definition = db.Column(db.String(200), nullable=False, primary_key=True)
	def __repr__(self):
		return '<Task %r>' % self.id
class Examples(db.Model):
	examples = db.Column(db.String(200), nullable=False, primary_key=True)
	def __repr__(self):
		return '<Task %r>' % self.id
class Synonimes(db.Model):
	synonimes = db.Column(db.String(200), nullable=False, primary_key=True)
	def __repr__(self):
		return '<Task %r>' % self.id
class Antonyms(db.Model):
	antonyms = db.Column(db.String(200), nullable=False, primary_key=True)
	def __repr__(self):
		return '<Task %r>' % self.id
@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		Word.query.delete()
		Definition.query.delete()
		Examples.query.delete()
		Synonimes.query.delete()
		Antonyms.query.delete()
		task_content = request.form['content']
		with open('text.txt', "a") as myfile:
			myfile.write(task_content+"\n")
		task_content=result.main(task_content)
		if task_content[0][0]!=request.form['content']:
			t=[]
			for i in task_content:
				t.append(i[0])
			return render_template('problem.html', tasks=t)
		try:
			if task_content[0][1]==0.0:
				return render_template('problem.html', tasks=[])
		except:
			pass
		new_task = Word(word='\n\n'.join(str(elem) for elem in list(flat.flatten(task_content[0]))))
		try:
			db.session.add(new_task)
			db.session.commit()
		except:
			pass
		try:
			new_task = Definition(definition='\n\n'.join(str(elem) for elem in list(flat.flatten(task_content[1]))))
			try:
				db.session.add(new_task)
				db.session.commit()
			except:
				pass
		except:
			print("xcfvgbhunij")
			pass
		try:
			new_task = Examples(examples='\n\n'.join(str(elem) for elem in list(flat.flatten(task_content[2]))))
			try:
				db.session.add(new_task)
				db.session.commit()
			except:
				pass
		except:
			pass
		try:
			new_task = Synonimes(synonimes='\n\n'.join(str(elem) for elem in list(flat.flatten(task_content[3]))))
			try:
				db.session.add(new_task)
				db.session.commit()
			except:
				pass
		except:
			pass
		try:
			new_task = Antonyms(antonyms='\n\n'.join(str(elem) for elem in list(flat.flatten(task_content[4]))))
			try:
				db.session.add(new_task)
				db.session.commit()
			except:
				pass
		except:
			pass
		return redirect('/')
	else:
		try:
			print(session['my_var'])
		except:
			Word.query.delete()
			Definition.query.delete()
			Examples.query.delete()
			Synonimes.query.delete()
			Antonyms.query.delete()
			session['my_var'] =1
		tasks = Word.query.all()+Definition.query.all()+Examples.query.all()+Synonimes.query.all()+Antonyms.query.all()
		return render_template('index.html', tasks=tasks)
if __name__ == "__main__":
	app.run(debug=True)
