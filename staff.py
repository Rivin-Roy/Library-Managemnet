from flask import *
from database import *
import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta


staff=Blueprint('staff',__name__)

@staff.route('/staffhome')
def staffhome():
	return render_template('staffhome.html')


@staff.route('/staffviewprofile',methods=['get','post'])
def staffviewprofile():
	data={}
	sid=session['staff_id']
	q="select * from  staff where staff_id='%s' "%(sid)
	r=select(q)
	data['staff']=r
	if "update" in request.form:
		fna=request.form['fn']
		lna=request.form['ln']
		pla=request.form['pl']
		d=request.form['d']
		pho=request.form['ph']
		em=request.form['em']
		hn=request.form['hn']
		dis=request.form['dis']
		c=request.form['c']
		pin=request.form['pin']
		q="select * from login inner join staff using(username) where staff_id='%s'"%(sid)
		print(q)
		res=select(q)
		preuname=res[0]['username']
		q="update staff set username='%s', firstname='%s',lastname='%s',place='%s',dob='%s',phone='%s',email='%s',house='%s',district='%s',city='%s',pincode='%s' where staff_id='%s'"%(em,fna,lna,pla,d,pho,em,hn,dis,c,pin,sid)
		r=update(q)
		q="update login set username='%s'  where username='%s'"%(em,preuname)
		r=update(q)
		flash("update successfully")

		return redirect(url_for('staff.staffviewprofile'))
	return render_template('staffviewprofile.html',data=data)


@staff.route('/staffmanagebooks',methods=['get','post'])
def staffmanagebooks():
	data={}
	q="SELECT * FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id)where lstatus='active' and gstatus='active' "
	r=select(q)
	data['book']=r
	q="select * from language where lstatus='active' "
	r=select(q)
	data['lan']=r
	q="select * from  genre where gstatus='active' "
	r=select(q)
	data['gen']=r
	if "add" in request.form:
		lid=request.form['lid']
		gid=request.form['gid']
		bn=request.form['bn']
		a=request.form['a']
		d=request.form['d']
		i=request.files['i']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		

	
		qs="insert into book values(null,'%s','%s','%s','%s','%s','%s','0','innactive')"%(lid,gid,bn,a,path,d)
		insert(qs)
		flash("added successfully")
		return redirect(url_for('staff.staffmanagebooks'))
	if "action" in request.args:
		action=request.args['action']
		bid=request.args['bid']
	else:
		action=None
	if "update" in request.form:
		lid=request.form['lid']
		gid=request.form['gid']
		bn=request.form['bn']
		a=request.form['a']
		d=request.form['d']
		i=request.files['i']
		path="static/images"+str(uuid.uuid4())+i.filename
		i.save(path)
				
		q="update book set language_id='%s',genre_id='%s',bname='%s',author='%s',image='%s',description='%s' where book_id='%s'"%(lid,gid,bn,a,path,d,bid)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('staff.staffmanagebooks'))
	if action=="update":
		q="select * from  book where book_id='%s'"%(bid)
		r=select(q)
		data['updatebook']=r
	if action=="active":
		q="update book set status='inactive' where book_id='%s'"%(bid)
		update(q)
		flash("inactive successfully")

		return redirect(url_for('staff.staffmanagebooks'))
	if action=="inactive":
		q="update book set status='active' where book_id='%s'"%(bid)
		update(q)
		flash("active successfully")

		return redirect(url_for('staff.staffmanagebooks'))
	
	return render_template('staffmanagebooks.html',data=data)




@staff.route('/staffmanagepurchasedetails',methods=['get','post'])
def staffmanagepurchasedetails():
	data={}
	
	q="select * from book  "
	r=select(q)
	data['book']=r
	q="select * from  publisher  where pstatus='active' "
	r=select(q)
	data['pub']=r
	q="SELECT * FROM `purchase_master` INNER  JOIN`purchase_child` USING(`pmaster_id`)INNER JOIN `book` USING(`book_id`)INNER JOIN `publisher` USING(`publisher_id`) "
	r=select(q)
	data['view']=r

	if "add" in request.form:
		sid=session['staff_id']
		bid=request.form['bid']
		pid=request.form['pid']
		amt=request.form['amt']
		data['amt']=amt
		q=request.form['q']
		data['q']=q
		d=request.form['d']
		t=request.form['t']
		qs="insert into purchase_master values(null,'%s','%s','%s','%s')"%(pid,sid,d,t)
		id=insert(qs)
		qp="insert into purchase_child values(null,'%s','%s','%s','%s')"%(id,bid,amt,q)
		insert(qp)
		q="update book set qty='%s' where book_id='%s'"%(q,bid)
		update(q)
		q="update book set status='active' where book_id='%s'"%(bid)
		update(q)
		flash("Purchased successfully")
		return redirect(url_for('staff.staffmanagepurchasedetails'))
	
	
	return render_template('staffmanagepurchasedetails.html',data=data)


@staff.route('/staffviewdetails',methods=['get','post'])
def staffviewdetails():
	data={}
	rid=request.args['rid']

	q="SELECT * FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id) INNER JOIN `rent_child` USING(`book_id`) where rmaster_id='%s'"%(rid)
	r=select(q)
	data['book']=r
	
	return render_template('staffviewdetails.html',data=data)


@staff.route('/staffviewrentrequest',methods=['get','post'])
def staffviewrentrequest():
	data={}
	q="SELECT * FROM rent_master INNER JOIN customer USING (customer_id)INNER JOIN rent_child USING (rmaster_id)  "
	r=select(q)
	data['book']=r
	if "action" in request.args:
		action=request.args['action']
		rid=request.args['rid']
		cid=session['staff_id']
		bookid=request.args['bookid']
	else:
		action=None
	
	if action=="accept":
		q="update  rent_master set status='accept' where rmaster_id='%s' "%(rid)
		r=update(q)
		q="update book set qty=qty-1 where book_id='%s'"%(bookid)
		update(q)
		flash(" accepted successfully")
		return redirect(url_for('staff.staffviewrentrequest'))
	
	if action=="confirm":
		q="update  rent_master set status='confirm' where rmaster_id='%s' "%(rid)
		r=update(q)
		flash(" returned successfully")
		return redirect(url_for('staff.staffviewrentrequest'))



	if action=="reject":
		q="update  rent_master set status='reject' where rmaster_id='%s' "%(rid)
		r=update(q)
		flash(" rejected successfully")
		return redirect(url_for('staff.staffviewrentrequest'))
		
	if action=="picked":
		q="update  rent_master set status='picked' where rmaster_id='%s' "%(rid)
		r=update(q)
		flash(" picked successfully")
		return redirect(url_for('staff.staffviewrentrequest'))
	if action=="dpicked":
		q="update  rent_master set status='not picked' where rmaster_id='%s' "%(rid)
		r=update(q)
		flash(" Book Renting Cancelled")
		return redirect(url_for('staff.staffviewrentrequest'))


	if "r_id" in request.args:
		r_id= request.args['r_id']
		date_after_month = datetime.today()+ relativedelta(months=1)
		fromdate=datetime.today().strftime('%d/%m/%Y')
		enddate=date_after_month.strftime('%m/%d/%Y')
		q="update  rent_master set rdate='%s' where rmaster_id='%s' "%(enddate,r_id)
		r=update(q)
		flash(" return date added successfully")
		return redirect(url_for('staff.staffviewrentrequest'))


	return render_template('staffviewrentrequest.html',data=data)


@staff.route('/staffselectreturndate',methods=['get','post'])
def staffselectreturndate():
	data={}
	
	if "add" in request.form:
		rid=request.args['rid']
		rd=request.form['rd']

		q="update  rent_master set rdate='%s' where rmaster_id='%s' "%(rd,rid)
		r=update(q)
		flash(" return date added successfully")
		return redirect(url_for('staff.staffviewrentrequest'))
	
	return render_template('staffselectreturndate.html',data=data)

@staff.route('/staffaddfine',methods=['get','post'])
def staffaddfine():
	data={}
	q="SELECT * FROM fine_category where fcstatus='active'  "
	r=select(q)
	data['cat']=r
	q="SELECT * FROM fine INNER JOIN fine_category USING (fcategory_id)INNER JOIN rent_master USING (rmaster_id)  "
	r=select(q)
	data['book']=r	
	if "add" in request.form:
		fid=request.form['fid']
		fa=request.form['fa']
		rid=request.args['rid']

		q="insert into fine values(null,'%s','%s','%s','fine-add')"%(fid,rid,fa)
		r=insert(q)
		flash(" fine added successfully")
		return redirect(url_for('staff.staffaddfine'))
	
	return render_template('staffaddfine.html',data=data)



@staff.route('/staffviewpayment',methods=['get','post'])
def staffviewpayment():
	data={}
	q="SELECT * FROM `payment` INNER JOIN `rent_master` USING(`rmaster_id`)INNER JOIN `rent_child` USING(`rmaster_id`) INNER JOIN BOOK USING(BOOK_ID)INNER JOIN customer USING(customer_id)"
	r=select(q)
	data['book']=r
	return render_template('staffviewpayment.html',data=data)



@staff.route('/staffviewcustomerdetails',methods=['get','post'])
def staffviewcustomerdetails():
	data={}
	q="SELECT * FROM customer"
	r=select(q)
	data['view']=r
	return render_template('staffviewcustomerdetails.html',data=data)

@staff.route('/staffmanagepublisher',methods=['get','post'])
def staffmanagepublisher():
	data={}
	
	if "add" in request.form:
		p=request.form['p']
		pho=request.form['ph']
		em=request.form['em']
		dis=request.form['dis']
		c=request.form['c']
		pin=request.form['pin']
		

	
		qs="insert into publisher values(null,'%s','%s','%s','%s','%s','%s','active')"%(em,p,pho,c,dis,pin)
		insert(qs)
		flash("added successfully")
		return redirect(url_for('staff.staffmanagepublisher'))
	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None
	if "update" in request.form:
		p=request.form['p']
		pho=request.form['ph']
		em=request.form['em']
		dis=request.form['dis']
		c=request.form['c']
		pin=request.form['pin']
		
		q="update publisher set email='%s',publisher='%s',phone='%s',city='%s',district='%s',pincode='%s' where publisher_id='%s'"%(em,p,pho,c,dis,pin,pid)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('staff.staffmanagepublisher'))
	if action=="update":
		q="select * from  publisher where publisher_id='%s'"%(pid)
		r=select(q)
		data['updatepublisher']=r
	if action=="active":
		q="update publisher set pstatus='inactive' where publisher_id='%s'"%(pid)
		update(q)
		flash("inactive successfully")
		return redirect(url_for('staff.staffmanagepublisher'))
	if action=="inactive":
		q="update publisher set pstatus='active' where publisher_id='%s'"%(pid)
		update(q)
		flash("active successfully")
		return redirect(url_for('staff.staffmanagepublisher'))
	q="select * from publisher "
	r=select(q)
	data['publisher']=r
	return render_template('staffmanagepublisher.html',data=data)

@staff.route('/staffviewsub',methods=['get','post'])
def staffviewsub():
	data={}

	q="SELECT * FROM `subscription` INNER JOIN plan USING(plan_id) INNER JOIN customer USING(customer_id)"
	r=select(q)
	data['book']=r
	
	return render_template('staffviewsub.html',data=data)