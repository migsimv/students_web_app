from flask import Flask, render_template, redirect, url_for
from models import db, Student
from forms import StudentForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
   #     db.drop_all()    
    db.create_all()  


@app.route("/")
def index():
    students = Student.query.order_by(Student.last_name).all()
    return render_template("index.html", students=students)


@app.route("/students/new", methods=["GET", "POST"])
def create_student():
    form = StudentForm()
    
    if form.validate_on_submit():
        student = Student(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            age=form.age.data,
            birth_date=form.birth_date.data,
            active=form.active.data
        )
        db.session.add(student)
        db.session.commit()
        
        return redirect(url_for("index"))
    
    return render_template("create.html", form=form)


@app.route("/students/<int:student_id>")
def show_student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template("show.html", student=student)


@app.route("/students/<int:student_id>/edit", methods=["GET", "POST"])
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    form = StudentForm(obj=student)
    
    if form.validate_on_submit():
        student.first_name = form.first_name.data
        student.last_name = form.last_name.data
        student.email = form.email.data
        student.age = form.age.data
        student.birth_date = form.birth_date.data
        student.active = form.active.data
        db.session.commit()
        
        return redirect(url_for("show_student", student_id=student.id))
    
    return render_template("edit.html", form=form, student=student)


@app.route("/students/<int:student_id>/delete", methods=["POST"])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)