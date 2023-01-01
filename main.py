from dialog_json import DialogJson
from answers import *

ans = Answers()
ans.operation_hour = "7:45-22:00"
ans.location = "Great Ormond Street Hospital for Children NHS Foundation Trust\n" \
           "Great Ormond Street\n" \
           "London\n" \
           "WC1N 3JH"

dj = DialogJson(ans)
dj.generate()
