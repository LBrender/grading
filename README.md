Running notes:

- To download data from Google Drive, make sure you get tab seperated values. Google uses tab seperated values by default, and if you c&p straight from the browser that's what you'll get. You'll also get a ton of blank lines at the end which will process as students with empty pdfs, so look out for that.

- Danielle teaches multiple classes these days. Before you run the command, make sure the correct information is in the template.

- The run command is
`python3 process_paper_grades.py`

- The writer automatically overwrites existing files, so if you need to fix and run again there's no need to delete old pdfs first. The pdf generation takes about three seconds per student, be patient. 

------------

Troubleshooting ideas:
pip3 install pdfkit
pip3 install jinja2
pip3 install wkhtmltopdf
^ This one takes FOREVER and I'm not sure it's necessary. try skipping it and see what happens?

In order to use pdfkit, you need wkhtmltopdf installed, which is kind of a pain. Go here: https://wkhtmltopdf.org/downloads.html, choose the one for mac, download the binary file and then open it. Your laptop's security settings might be a butt about it, but figure it out, it's worth it.

GENERAL
- When Danielle makes a csv from scratch (for midterm and final papers), she usually does "Link Brender". When she downloads from blackboard, it gives "Brender | Link". This fucks everything up every single time. It's currently set up so the paper ones work one way and the semester grades work the other way. Do not mess with this.
- There's a print statement in each process script that prints out the name and grade. Leave that in place because it's useful for entering into blackboard right away. Are the total points out of 100? If not, consider printing out the point numbers as well, it can be helpful for entering into blackboard.
- Make sure your rows and stuff are right. Sometimes Danielle changes the format of the rubric and it messes things up in both the script and the template.
- Did you update the total score?
- Is the class name correct in the template?
- Danielle is considering evaluating Part 1 on its actual merits rather than an up/down. What the hell do we do about that?

MIDTERM/PAPER
- For paper scores, when Danielle puts in a 0 you should replace it with a 6. Tier 6 is the lowest and it awards 0 points.
- If a student fails to submit part 1, Danielle will put 0 for that section, make sure you do not replace THAT with a 6.

SEMESTER
- Any assignments left blank you should populate with 0s. Just do a find and replace with two tabs until there are no more two tabs.
- Pay very careful attention to the semester scores csv you get from blackboard. The table headers need cleaning up and you can really fuck things up if you do it wrong.
