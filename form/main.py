'''
Tyrone Swinnie
Design for Web Programming
9/10/14
Simple Form Assignment
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response("test")
        # the firs thing I want to do is create the form for the page
        page_head = '''<!DOCTYPE HTML>
<html>
<head>
<title></title>

'''
        page_body = '''
<body>
<div class="container">
<form method ="GET" action="">
<h2 id="titleText">Get Your Car Loan Today!</h2>
<label>First Name:</label><input type="text" name="first" /><br>
<label>Last Name:</label><input type="text" name="last" /><br>


<label>How Much:</label><select name="small_loan">
  <option  value="$500 - $1000" >$500 - $1000</option>
    <option  value="$1000 - $2000" >$1000 - $2000</option>
        <option  value="$2000 - $3000" >$2000 - $3000</option>
</select>
<br>
<label>How Long:</label><select name="loan_date">
  <option  value="30 days - 60 days" >30 days - 60 days</option>
    <option  value="60 days - 90 days" >60 days - 90 days</option>
        <option  value="90 days - 120 days" >90 days - 120 days</option>
</select>
<label>Car Loan:</label><input type="checkbox" name= "car" value="Car Loan" style="margin-top: -9px;" /><br>

<br>
<input id="submit" type="submit" value="submit" />
<h3 id="confirmation">Your Confirmation</h3>




        '''
        page_close = '''
</form>
</div>
</body>
</html>
        '''

        #now that I have my form for the page I want to get information that the user input in to the form
        if self.request.GET:
            first_name = self.request.GET['first']  # this gets the value for the first name
            last_name = self.request.GET['last']  # this gets the last name value
            car_loan = self.request.GET['car']  # this gets the car loan check box value
            drop = self.request.GET['small_loan']  # this gets the drop down selection value
            loan = self.request.GET['loan_date']  # this gets the days for the loan value drop down
            # return the values that the user put in the form after the submit button
            self.response.write(page_head + page_body + first_name + ' ' + last_name + ' ' + car_loan + ' ' + drop + ' ' + loan + page_close)
        else:
            # if the user does not input any values then do this
            self.response.write(page_head + page_body + page_close)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
