from flask import *
from database import *
import uuid
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail


public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('index.html')

@public.route('/login',methods=['get','post'])
def login():

	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['uname']=res[0]['username']
			if res[0]['user_type']=='admin':
				flash("login successfully....!")
				return redirect(url_for('admin.admin_home'))
			elif res[0]['user_type']=='staff':
				q="select * from staff where username='%s'"%(session['uname'])
				res=select(q)
				session['staff_id']=res[0]['staff_id']
				flash("login successfully....!")
				return redirect(url_for('staff.staffhome'))
			elif res[0]['user_type']=='user':
				
				q="select * from customer where username='%s'"%(session['uname'])
				res=select(q)
				if res:
					session['customer_id']=res[0]['customer_id']
					customer_id=session['customer_id']
					q="select * from subscription where customer_id='%s'"%(session['customer_id'])
					r=select(q)
					if not r:
						flash("Please!complete your registration fee....!")
						return redirect(url_for('public.public_subscription',customer_id=customer_id))
					else:
						# plan_id=r[0]['plan_id']
						# q="select * from plan where plan_id='%s'"%(plan_id)
						# res=select(q)
						# if res:
						# 	from datetime import datetime
						# 	todate=datetime.today().strftime('%m/%d/%Y')
			
						# 	start_date = datetime.strptime(res[0]['rdate'], "%m/%d/%Y")
						# 	end_date = datetime.strptime(todate, "%m/%d/%Y")

			# /////////////////////////

							# string_input_with_date = "25/10/2017"
							# past = datetime.strptime(start_date, "%d/%m/%Y")
							# present = datetime.now()
							# if start_date.date() > present.date():
							
							# 	flash("book returned")
							# 	return redirect(url_for('user.userviewrentrequest'))
							# else:
							# 	print(start_date, "   ",end_date)
							# 	val=(end_date-start_date).days
							# 	print(val)
							# 	out=(val//30)+1
							# 	print(out)

						# else:
						flash("login successfully....!")
						return redirect(url_for('user.userhome'))
		else:
			flash("INVALID USERNAME OR PASSWORD")
	return render_template('login.html')


@public.route('/user_register',methods=['get','post'])
def user_register():
	if 'submit' in request.form:
		fname=request.form['fn']
		lname=request.form['ln']
		phone=request.form['ph']
		email=request.form['em']
		house=request.form['hn']
		district=request.form['dis']
		pincode=request.form['pin']
		pwd=request.form['pwd']
		q="select * from login where username='%s'"%(email)
		res=select(q)
		if res:
			flash("username is already exist")
		else:
			q="INSERT INTO `login` VALUES('%s','%s','user')"%(email,pwd)
			insert(q)
			q1="INSERT INTO `customer` VALUES(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(email,fname,lname,phone,email,house,district,pincode)
			insert(q1)
			flash('registered')
			return redirect(url_for('public.user_register'))

	return render_template("user_register.html")

@public.route('/forgotpassword',methods=['get','post'])
def forgotpassword():
	data={}
	if "forgot" in request.form:
		


		uname=request.form['un']
		phone=request.form['p']
		

		q="select * from login  where username='%s' and user_type='staff'"%(uname)
		r=select(q)
		print(r)
		if r:
			session['username']=r[0]['username']
			q="select * from  staff inner join login using(username) where username='%s' and phone='%s' "%(uname,phone)
			res=select(q)
			print(res)
			if res:
				print(res)
				flash("verified")
				email=res[0]['email']
				print(email)
				rd=random.randrange(1000,9999,4)
				msg=str(rd)
				session['rd']=rd

				print(rd)
				try:
					gmail = smtplib.SMTP('smtp.gmail.com', 587)
					gmail.ehlo()
					gmail.starttls()
					gmail.login('projectsriss2020@gmail.com','messageforall')
				except Exception as e:
					print("Couldn't setup email!!"+str(e))

				msg = MIMEText(msg)

				msg['Subject'] = 'OTP FOR password RECOVRY'

				msg['To'] = email

				msg['From'] = 'projectsriss2020@gmail.com'

				try:
					gmail.send_message(msg)
					print(msg)
					flash("EMAIL SENED SUCCESFULLY")
					return redirect(url_for('public.setotp'))


				except Exception as e:
					print("COULDN'T SEND EMAIL", str(e))
					return redirect(url_for('public.forgotpassword'))
			


				return redirect(url_for('public.setotp'))
			else:
				flash("invalid password")
				return redirect(url_for('public.forgotpassword'))
				
		else:
			q="select * from login inner join customer using(username)  where username='%s' and phone='%s'"%(uname,phone)
			res1=select(q)		
			if res1:
				session['username']=res1[0]['username']
				email=res1[0]['email']

				flash("verified")
				rd=random.randrange(1000,9999,4)
				data['rd']=rd
				print(rd)
				session['rd']=rd
				msg=str(rd)

				print(rd)
				try:
					gmail = smtplib.SMTP('smtp.gmail.com', 587)
					gmail.ehlo()
					gmail.starttls()
					gmail.login('projectsriss2020@gmail.com','messageforall')
				except Exception as e:
					print("Couldn't setup email!!"+str(e))

				msg = MIMEText(msg)

				msg['Subject'] = 'OTP FOR password RECOVRY'

				msg['To'] = email

				msg['From'] = 'projectsriss2020@gmail.com'

				try:
					gmail.send_message(msg)
					print(msg)
					flash("EMAIL SENED SUCCESFULLY")
					return redirect(url_for('public.setotp'))


				except Exception as e:
					print("COULDN'T SEND EMAIL", str(e))
					return redirect(url_for('public.forgotpassword'))
			


				return redirect(url_for('public.setotp'))
			else:
				flash("invalid password")
				return redirect(url_for('public.forgotpassword'))	

	return render_template('forgotpassword.html',data=data)

@public.route('/setotp',methods=['get','post'])
def setotp():
	rd=session['rd']
	if "otp" in request.form:
		otp=request.form['otp']
		if int(otp)==int(rd):
			return redirect(url_for('public.setpassword'))
		else:
			flash("invalid otp")
			return redirect(url_for('public.forgotpassword'))



	return render_template('setotp.html')

@public.route('/setpassword',methods=['get','post'])
def setpassword():

	if "conform" in request.form:
		new_pas=request.form['new_pas']
		con_pas=request.form['con_pas']
		username=session['username']
		print(username)

		if new_pas==con_pas :
			q="update login set password='%s' where username='%s'"%(con_pas,username)
			r=update(q)
			print(r)

			flash("verified successfully")
			flash(" password changed successfully")
			return redirect(url_for('public.login'))
		else:
			flash("sorry! password mismatched ")
			return redirect(url_for('public.setpassword'))
	return render_template('setpassword.html')

@public.route('/public_reg_fee',methods=['get','post'])
def public_reg_fee():
	data={}
	cid=request.args['cid']
	amount=request.args['amount']	
	plan=request.args['plan']
	print(plan)	
	data['amount']=amount
	customer_id=session['customer_id']

	if "payment" in request.form:
		date_after_month = datetime.today()+ relativedelta(months=int(plan))
		fromdate=datetime.today().strftime('%d/%m/%Y')
		print(fromdate)
		enddate=date_after_month.strftime('%d/%m/%Y')	
		print(enddate)
		if fromdate<=enddate:
			
			q="insert into subscription values(null,'%s','%s',curdate(),'%s')"%(customer_id,cid,enddate)
			insert(q)
			print('hhhhhhhhhhhhhhhh')
			print(q)
			flash("successfully complete your subscription")
			return redirect(url_for('public.login'))	
		else:
			flash("expired")
			return redirect(url_for('public.public_subscription'))		
	return render_template('public_reg_fee.html',data=data)

@public.route('/public_subscription')
def public_subscription():
	data={}

	q="select * from plan"
	r=select(q)
	data['view']=r
	return render_template('public_subscription.html',data=data)
