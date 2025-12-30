<!DOCTYPE html>
<html>
<head>
    <style>
        table {border: 1px solid black; border-collapse: collapse; width: 100%;}
        th {border: 1px solid black; border-collapse: collapse;}
        td {border: 1px solid black; border-collapse: collapse;}
    </style>
</head>
<body style="padding: 3rem">
    <h1>Semester Grades</h1>
    History 152, Fall 2025, Danielle Bennett

    <h3>Student Name: {{ context["student_name"] }}</h3>

    <p>Breakdown of Final Score </p>

    <ul>
        <li>Midterm Score: {{ context["midterm_grade"] }} </li>
        <li>Writing Score: {{ context["writing_score"] }} ({{ context["writing_assignments"] }} out of 6)</li>
        <li>Final Paper Score: {{ context["paper_score"] }} </li>
        <li>Discussion Score: {{context["discussion_score"] }} </li>
    </ul>

    <br>
    <strong>Total:</strong> {{ context["total_points"] }} points

    <h3>Final Grade: {{ context["total_points"] }}/400 ({{ context["percent"] }}% {{ context["grade"] }})
</body>
</html>