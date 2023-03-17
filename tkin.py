import json
a = '''Here is the Python dictionary for the request:

```
{
  "receiver": "raghubir yadav",
  "subject": "Not attending meet, please come to office tomorrow",
  "content": "Dear Raghubir Yadav,\n\nI wanted to inform you that I will not be able to attend the meeting scheduled for today. Could you please come to the office tomorrow afternoon to discuss the matter in person?\n\nBest regards,\n[Your Name]"
}
```
Please replace `[Your Name]` with your actual name.'''

dict = json.loads(a[a.index("{"): a.index("}")+1], strict=False)


# print(eval(a[a.index("{"): a.index("}")+1]))

d = {'subject': 'Not attending the meet today', 'content': "Dear Raghubir Yadav, \n\nI regret to inform you that I won't be able to attend the meeting today. However, I would like to meet you in the office tomorrow to discuss the matter at hand.\n\nKind regards,\nUser", 'receiver': 'raghubir yadav'}
print(d.get('content'))
