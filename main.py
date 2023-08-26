from flask import Flask, render_template, request
import datetime
import info


today = datetime.date.today()
if today.month >= 2 and today.month < 9:
    semester = "fall"
    year = today.year
else:
    semester = "spring"
    year = today.year + 1

courses = []

app = Flask("__name__")

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        subject = request.form["subject"].upper()
        course_number = request.form["course number"]
        crn = request.form["crn"]
        print(subject, course_number, crn)
        section, enroll = info.get_course(year, semester, subject, course_number, crn)
        if section:
            courses.append([subject, course_number, crn, section, enroll])
    return render_template("index.html", content=courses)

if __name__ == "__main__":
    app.run()