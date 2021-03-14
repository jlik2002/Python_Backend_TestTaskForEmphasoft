CRUD on Django with jwt token

<h1>/user/create/ - for create account </h1>
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
  <p>}</p>

<h1>/user/authorization/ - for authorization to account </h1>
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
