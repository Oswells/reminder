### Reminder

#### Statement
I provide a free website for sending emails, do not use it for harassing others, spreading ads, etc. If I find you using it improperly, I have the right to terminate the service for you.  

#### What can it do
When running a program on a server, we often don't know when it stops.  Reminder can help you.  Just one line of code and send a message to your email when the program is finished.  

#### Installation
```shell
pip install emailreminder
```

#### Getting Started
You simply add decorators `reminder` to the functions you care about.
```python
# example
from email_reminder import reminder
@reminder(email=your_email, url='https://www.zjunjie.top/email', language='Chinese')
def train():
    train code

if __name__ == '__main__':
    train()
```
An email will be sent to you when the run completes or terminates unexpectedly.  The parameters `email` and `url` are required, `language` supports Chinese and English. you can add any other parameters, and any additional parameterreminders will appear in your email.  

#### Details
I offer a free website:https://www.zjunjie.top/email. Of course, you can build your own website for personal use.
The purpose of this decorator is to submit a POST request to the `url` with the data content of {'email':your_email, 'mode':'remind', 'filepath':os.getcwd(),'csrfmiddlewaretoken':csrftoken, 'error':error, ...}
