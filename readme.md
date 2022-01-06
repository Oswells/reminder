### Reminder

#### Statement
I provide a free website for sending emails, do not use it for harassing others, spreading ads, etc. If I find you using it improperly, I have the right to terminate the service for you.  

#### What can it do
When running a program on a server, we often don't know when it stops.  `reminder` can help you.  Just one line of code and a email will be sent to you when the program is finished.  

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
An email will be sent to you when the program runs completes or terminates unexpectedly.  
[Click here for more demos and en example of email you will receive.](./demo/)

#### Parameters
These parameters are required for `reminder`.
+ url:str
+ email:str

These parameters are optional for `reminder`.
+ language:str['ch','Chinese' for Chinese and 'en','English' for English]
+ files:List[filepath or dirpath]

These parameters cannot be passed into `reminder` as parameters.
+ mode
+ FilePath
+ Error
+ CostTime
+ Ppid
+ csrfmiddlewaretoken

You can pass any other parameters into `reminder`, and all these parameters will appear in your eamil.

#### Details
I offer a free website:https://www.zjunjie.top/email. Of course, you can build your own website for personal use.
The purpose of this decorator is to submit a POST request to the `url` with the data content of {'email':your_email, 'mode':'remind', 'FilePath':os.getcwd(),'csrfmiddlewaretoken':csrftoken, 'Error':error, ...}

#### TODO
+ Make email look better: Now I don't know how to send an email with CSS style, I add style, but it doesn't display properly. 