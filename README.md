# CICD-2 Sample Template

Use this `README.md` as the standard structure for future labs.


## Testing and Coverage 

app/main.py coverage report
The report came back with 86% of code covered with lines 32-34, 51, and 60 missing coverage

One important untested behaviour is line 32-34 which is an IntegrityError for when a loan already exists. This matter that we test it because if we don't write test for these lines we can't be sure that they are operating as intended
