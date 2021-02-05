
#import twilio

#accountSid = 'AC04bfbed3f9e9a5f3e47c094798bf7828'
#authToken = '3c7b1fbf59283034479890c803e3ffe4'
#twilioClient = TwilioRestClient(accountSid, authToken)
#myTwilioNumber = 7875041144
#destCellPhone =8421348474
#myMessage = twilioClient.messages.create(body="whatever", from_=7875041144, to=8421348474)


import way2sms

q = way2sms.sms('7875041144','sumeru')
q.send('8421348474', 'hello')
n = q.msgSentToday()
q.logout()