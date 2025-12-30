import csv
import pdfkit
import jinja2
import helpers
import math

# This is a bunch of stuff I copied and pasted from Stack Overflow.
# It processes html templates.
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "templates/semester_report_template_sections.py"
template = templateEnv.get_template(TEMPLATE_FILE)

# Establish some class-wide variables
scores_csv = 'scores/semester_scores.csv'
class_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "number_of_students": 0, "score_total": 0, "score_average": 0}

# Open the scores csv, iterate through the rows:
with open(scores_csv, newline='') as csvfile:
	paper_scores = csv.reader(csvfile, delimiter='	', quotechar='|')
	# The first row is headers, just read them into a list for lableling later.
	assignment_names = next(paper_scores)[2:]
	print(assignment_names)
	for row in paper_scores:
		# Each row represents one student. Create a template context for them.
		student_name = row[0]
		total_score = 0
		print(student_name)

		midterm_grade = float(row[2])

		writing_assignments = 0
		for item in [row[3], row[4], row[5], row[6], row[7], row[8], row[9]]:
			if item == "x":
				writing_assignments += 1
		writing_score = round((writing_assignments * 100) / 6, 0)

		paper_score = float(row[12])
		discussion_score = float(row[13]) * 20

		total_points = round(midterm_grade + writing_score + paper_score + discussion_score, 0)
		percent = round(total_points / 4, 0)
		grade = helpers.letter_grade(percent)
		class_count[grade[0]] += 1
		class_count["number_of_students"] += 1
		class_count["score_total"] += percent
		context = {
			"midterm_grade": midterm_grade,
			"writing_score": writing_score,
			"writing_assignments": writing_assignments,
			"paper_score": paper_score,
			"discussion_score": discussion_score,
			"total_points": total_points,
			"percent": percent,
			"grade": grade,
			"student_name": student_name,
		}

		print(student_name + "   " + context["grade"] + "   " + str(context["percent"]))

		# fill in the html with the context
		sourceHtml = template.render(context=context)

		# process the html into a pdf, name it correctly
		file_name = "reports/" + student_name + " semester grade.pdf"
		pdfkit.from_string(sourceHtml, file_name)

class_count["score_average"] = class_count["score_total"] / class_count["number_of_students"]
print(class_count)
