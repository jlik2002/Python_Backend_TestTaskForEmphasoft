CRUD on Django with jwt token

<h1>/user/create/ - for create account <b>POST</b> </h1>
  <b>data</b>
  <p>{</p>
   <p>  "email":"test@gmail.com",</p>
   <p>  "login":"way",</p>
   <p>  "password":"qwerty",</p>
   <p>  "firstname":"petya",</p>
   <p>  "lastname":"hulif"</p>
  <p>}</p>
  
  lastname and first name - optional
  
  <b>responses code 201</b>
  <p>{</p>
   <p>  "id":6,</p>
   <p>  "email":"test@gmail.com",</p>
   <p>  "login":"way",</p>
   <p>  "firstname":"petya",</p>
   <p>  "lastname":"hulif"</p>
   <p>  "date_created":"2021-03-11T00:43:59.851049Z",</p>
   <p>  "is_active":"true"</p>
  <p>}</p>

<h1>/user/authorization/ - for authorization to account <b>POST</b> </h1>
<b>data</b>
  <p>{</p>
   <p>  "login":"way",</p>
   <p>  "password":"qwerty",</p>
  <p>}</p>
 <b>responses code 200</b>
  <p>{</p>
  <p>"name": "way", </p>
    <p>"token": "eyJ0eXAiOiJKV1QiLCc....." </p>
  <p>}</p>

<p>For use this need add to headers "Authorization":"SuperSecreetToken" + token</p>

<h1>/user/get_me/ - for take info about account <b>GET</b> </h1>
<b>responses code 200</b>
  <p>{</p>
   <p>  "id":6,</p>
   <p>  "email":"test@gmail.com",</p>
   <p>  "login":"way",</p>
   <p>  "firstname":"petya",</p>
   <p>  "lastname":"hulif"</p>
   <p>  "date_created":"2021-03-11T00:43:59.851049Z",</p>
   <p>  "is_active":"true"</p>
  <p>}</p>
  
<h1>/user/change/ - for change info about account <b>PUT</b> </h1>
  <p>data is any for change (email,login,firstname,lastname,password)</p>
  <b>responses code 200</b>
  <p>{</p>
   <p>  "id":6,</p>
   <p>  "email":"test@gmail.com",</p>
   <p>  "login":"way",</p>
   <p>  "firstname":"petya",</p>
   <p>  "lastname":"hulif"</p>
   <p>  "date_created":"2021-03-11T00:43:59.851049Z",</p>
   <p>  "is_active":"true"</p>
  <p>}</p>
  
<h1>/user/remove/ - for remove account <b>POST</b> </h1>
  <b>data</b>
  <p>{</p>
   <p>  "id":7</p>
  <p>}</p>
  <b>responses code 200</b>
  <p>{</p>
   <p>  "id":7,</p>
   <p>  "email":"test@gmail.com",</p>
   <p>  "login":"way",</p>
   <p>  "firstname":"petya",</p>
   <p>  "lastname":"hulif"</p>
   <p>  "date_created":"2021-03-11T00:43:59.851049Z",</p>
   <p>  "is_active":"false"</p>
  <p>}</p>
  
<h1>/user/active/ - for remove account <b>POST</b> </h1>
  <b>data</b>
  <p>{</p>
   <p>  "id":7</p>
  <p>}</p>
  <b>responses code 200</b>
  <p>{</p>
   <p>  "id":7,</p>
   <p>  "email":"test@gmail.com",</p>
   <p>  "login":"way",</p>
   <p>  "firstname":"petya",</p>
   <p>  "lastname":"hulif"</p>
   <p>  "date_created":"2021-03-11T00:43:59.851049Z",</p>
   <p>  "is_active":"true"</p>
  <p>}</p>
  
<h1>/user/delete/ - for delete account <b>POST</b> </h1>
  <b>data</b>
  <p>{</p>
   <p>  "id":7</p>
  <p>}</p>
  <b>responses code 200</b>
  <p>{</p>
   <p>  "status":"OK, user delete"</p>
  <p>}</p>
