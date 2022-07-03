from flask import *
from database import *
from datetime import datetime
from dateutil.relativedelta import relativedelta


user=Blueprint('user',__name__)

@user.route('/userhome')
def userhome():
	return render_template('userhome.html')


@user.route('/userviewbook',methods=['get','post'])
def userviewbook():
	data={}
	q="SELECT * FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id) where lstatus='active' and gstatus='active' and status='active' "
	r=select(q)
	data['book']=r

	if "action" in request.args:
		action=request.args['action']
		bid=request.args['bid']
		cid=session['customer_id']
	else:
		action=None
	
	if action=="rentrequest":

		q="SELECT * FROM rent_master INNER JOIN `rent_child` USING(`rmaster_id`)  where rent_master.status='pending' and book_id='%s' "%(bid)
		r=select(q)

		if r:
			flash("you cannot send rent request")
			return redirect(url_for('user.userviewbook'))


		else :
			q="SELECT COUNT(`customer_id`) as cnt FROM `rent_master` WHERE (`customer_id`='%s' and  status='return-pending')or(`customer_id`='%s' and  status='accept')or(`customer_id`='%s' and  status='pending')or(`customer_id`='%s' and  status='request-send')"%(cid,cid,cid,cid)
			res=select(q)
			print(q)
			if res:
				cnt=res[0]['cnt']
				print(cnt)
				if cnt>=3:
					print("qqqqqqqqqqq")
					flash("Request cannot send")
					return redirect(url_for('user.userviewbook'))

				else:
					qs="insert into rent_master values(null,'%s','',curdate(),'pending')"%(cid)
					id=insert(qs)
					
					qp="insert into rent_child values(null,'%s','%s')"%(id,bid)
					insert(qp)
					flash("rent requested successfully")
					return redirect(url_for('user.userviewbook'))
			# else:
			# 	qs="insert into rent_master values(null,'%s','',curdate(),'pending')"%(cid)
			# 	id=insert(qs)

			# 	qp="insert into rent_child values(null,'%s','%s')"%(id,bid)
			# 	insert(qp)
			# 	flash("rent requested successfully")
			# 	return redirect(url_for('user.userviewbook'))
	if "search" in request.form:
		book=request.form['book']+"%"
		q="SELECT * FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id) where lstatus='active' and gstatus='active' and status='active' and bname like '%s'"%(book) 

		# q="select *  FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id) where bname like '%s'"%(book)
		print(q)
		r=select(q)
		if r:
			data['search']=r
			print(data['search'])
		else:
			flash("NO MATCHED RESULTS FOUND")


	return render_template('userviewbook.html',data=data)


@user.route('/userviewrentrequest',methods=['get','post'])
def userviewrentrequest():
	data={}
	customer_id=session['customer_id']
	q="SELECT * FROM rent_master INNER JOIN customer USING (customer_id)INNER JOIN rent_child USING (rmaster_id) where customer_id='%s'"%(customer_id)
	r=select(q)
	data['book']=r
	if "action" in request.args:
		action=request.args['action']
		rid=request.args['rid']
		bookid=request.args['bookid']
	else:
		action=None
	
	if action=="send":
		q="update  rent_master set status='request-send' where rmaster_id='%s' "%(rid)
		r=update(q)
		
		flash(" send rent request successfully")
		return redirect(url_for('user.userviewrentrequest'))
	if action=="cancel":
		q="update  rent_master set status='cancel' where rmaster_id='%s' "%(rid)
		r=update(q)
		
		flash(" cancelled successfully")
		return redirect(url_for('user.userviewrentrequest'))

	if action=="returnbook":
		# q="update  rent_master set status='return-pending' where rmaster_id='%s' "%(rid)
		# r=update(q)
		q="update book set qty=qty+1 where book_id='%s'"%(bookid)
		update(q)		
		q="select * from rent_master where rmaster_id='%s'" %(rid)
		res=select(q)
		if res:
			from datetime import datetime
			todate=datetime.today().strftime('%m/%d/%Y')
			
			start_date = datetime.strptime(res[0]['rdate'], "%m/%d/%Y")
			end_date = datetime.strptime(todate, "%m/%d/%Y")

			# /////////////////////////

			string_input_with_date = "25/10/2017"
			# past = datetime.strptime(start_date, "%d/%m/%Y")
			present = datetime.now()
			if start_date.date() > present.date():

				q="update  rent_master set status='return-pending' where rmaster_id='%s' "%(rid)
				r=update(q)
			
				flash("book returned")
				return redirect(url_for('user.userviewrentrequest'))
			else:

				q="select * from fine_category "
				res=select(q)
				famount=res[0]['fine_amount']
				print(famount)
				print(start_date, "   ",end_date)
				val=(end_date-start_date).days
				print(val)
				out=(val//30)+1
				print(out)
				print(famount)
				print("^^^^^^^^^^^^66")
				if out==0:
					fine=famount
				else:
					fine=int(out)*int((famount))

				print(fine)
				data['fine']=fine
				flash(" Late Return You have Fine")
				return redirect(url_for('user.usermakepayment',rid=rid,fine=fine))
			# /////////////////////////
			
	return render_template('userviewrentrequest.html',data=data)


@user.route('/userviewprofile',methods=['get','post'])
def userviewprofile():
	data={}
	cid=session['customer_id']
	q="select * from customer where customer_id='%s' "%(cid)
	r=select(q)
	data['customer']=r
	if "update" in request.form:
		fna=request.form['fn']
		lna=request.form['ln']
		pho=request.form['ph']
		em=request.form['em']
		hn=request.form['hn']
		dis=request.form['dis']
		pin=request.form['pin']
		q="select * from login inner join customer using(username) where customer_id='%s'"%(cid)
		print(q)
		res=select(q)
		preuname=res[0]['username']
		q="update customer set username='%s', first_name='%s',last_name='%s',phone='%s',email='%s',house='%s',district='%s',pincode='%s' where customer_id='%s'"%(em,fna,lna,pho,em,hn,dis,pin,cid)
		r=update(q)
		q="update login set username='%s'  where username='%s'"%(em,preuname)
		r=update(q)
		flash("update successfully")

		return redirect(url_for('user.userviewprofile'))
	return render_template('userviewprofile.html',data=data)

@user.route('/userviewfine',methods=['get','post'])
def userviewfine():
	data={}
	q="SELECT *,`fine`.`status` AS fstatus FROM fine INNER JOIN fine_category USING (fcategory_id)INNER JOIN rent_master USING (rmaster_id)  "
	r=select(q)
	data['book']=r
	
	return render_template('userviewfine.html',data=data)

@user.route('/usermakepayment',methods=['get','post'])
def usermakepayment():
	data={}
	rid=request.args['rid']
	total=request.args['fine']
	data['total']=total
	if "payment" in request.form:
		q="insert into payment values(null,'%s','%s',curdate())"%(rid,total)
		insert(q)
		q="update rent_master set status='paid' where rmaster_id='%s'"%(rid)
		update(q)
		flash("paid successfully")
		return redirect(url_for('user.userviewrentrequest'))
	return render_template('usermakepayment.html',data=data)


@user.route('/userviewdetails',methods=['get','post'])
def userviewdetails():
	data={}
	rid=request.args['rid']

	q="SELECT * FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id) INNER JOIN `rent_child` USING(`book_id`) where rmaster_id='%s'"%(rid)
	r=select(q)
	data['book']=r
	
	return render_template('userviewdetails.html',data=data)


@user.route('/userviewpayment',methods=['get','post'])
def userviewpayment():
	data={}
	rid=request.args['rid']

	q="SELECT * FROM `payment` INNER JOIN `rent_master` USING(`rmaster_id`) inner join customer using(customer_id) where rmaster_id='%s'"%(rid)
	r=select(q)
	data['book']=r
	
	return render_template('userviewpayment.html',data=data)
@user.route('/userviewpayments',methods=['get','post'])
def userviewpayments():
	data={}
	cid=session['customer_id']

	q="SELECT * FROM `payment` INNER JOIN `rent_master` USING(`rmaster_id`)INNER JOIN `rent_child` USING(`rmaster_id`) INNER JOIN BOOK USING(BOOK_ID)inner join customer using(customer_id) where customer_id='%s'"%(cid)
	r=select(q)
	data['book']=r
	
	return render_template('userviewpayment.html',data=data)
@user.route('/userviewsubpayments',methods=['get','post'])
def userviewsubpayments():
	data={}
	cid=session['customer_id']

	q="SELECT * FROM `subscription` INNER JOIN plan USING(plan_id) INNER JOIN customer USING(customer_id) where customer_id='%s'"%(cid)
	r=select(q)
	data['book']=r
	
	return render_template('userviewsubpayments.html',data=data)


	 
