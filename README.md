# Scripts

## AutoEmailSender.py
**Description:** This is an automated email sender that utlises python's smtplib library which utlises SMTP to send emails. 587 is the default port used to ensure that SMTPS (secure) is used. It uses MIME to format the the email.

**Use**: Enter your gmail id and password under the "Email Configuration" section. In the case that the email is set to 2FA, generating an app password may be the best approach to ensuring there are no authentication issues.

## wordFrequencyCounter.py
**Description:** This is a word frequency calculator, that can calculate and print the frequency of each word in a given text file. The counter checks for punctuation and spacing while parsing each word ensuring an accurate frequency count. 

**Use**: Ensure that the *string* library is installed. The user must set the path to the txt file to be read in. 
