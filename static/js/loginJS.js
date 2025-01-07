//login and registration button functions for displaying form 
var loginForm = document.getElementById("loginForm");
var registerForm = document.getElementById("registerForm");
var line =document.getElementById("line");

function register(){
  registerForm.style.transform = "translateX(0px)";
  loginForm.style.transform = "translateX(0px)";
  line.style.transform = "translateX(150px)";
}

function login(){
  registerForm.style.transform = "translateX(400px)";
  loginForm.style.transform = "translateX(400px)";
  line.style.transform = "translateX(0px)";
}

//form validations
function registerUser(){
  var name = document.getElementById('name').value;
    var nameReg = /^[A-Za-z\s]+$/;
    if(name!=""){
        if(!name.match(nameReg)){
          swal ( "Oops" ,"Name should only contain letters and spaces!" ,  "error" )
          // alert("Name should only contain letters and spaces");
          return false;
      }
    }
    
    var phone= document.getElementById('phone').value;
    var phoneReg = /^[7-9][0-9]{9}$/;
    if(phone!=""){
        if(!phone.match(phoneReg)){
          swal ( "Oops" ,"Phone number should start between 7-9 and should be exactly 10 digits!" ,  "error" )
          // alert("Phone number should start between 7-9 and should be exactly 10 digits .");
          return false;
      }
    }

    var email= document.getElementById('email').value;
    var emailReg = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if(email!=""){
        if(!email.match(emailReg)){
          swal ( "Oops" ,"Please enter a valid email id!" ,  "error" )
          // alert("Please enter a valid email id.");
          return false;
      }
    }

    var password= document.getElementById('password').value;
    var passReg = /^[^0-9][a-zA-Z0-9@$]{5}$/;
    if(password!=""){
        if(!password.match(passReg)){
          swal ( "Oops" ,"Password must be of 6 characters including characters and numbers but it cannot start with any number!" ,  "error" )
          // alert("Password must be of 6 characters including characters and numbers but it cannot start with any number.");
          return false;
      }
    }

    var address= document.getElementById('address').value;
    if(address==""){
      swal ( "Oops" ,"Address field cannot be empty!" ,  "error" )
          // alert("Address field cannot be empty.");
          return false;
    }

    var country= document.getElementById('country').value;
    if(country==""){
      swal ( "Oops" ,"Please select your Country!" ,  "error" )
          // alert("Please select your Country");
          return false;
    }

    var city= document.getElementById('city').value;
    if(city==""){
      swal ( "Oops" ,"Please select your City!" ,  "error" )
          // alert("Please select your City");
          return false;
    }

    return true;
}



function register_user(){
  url = "user_registration";
  var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value

    const data = new FormData();
    data.append("name", document.getElementById("name").value);
    data.append("phone", document.getElementById("phone").value);
    data.append("email", document.getElementById("email").value);
    data.append("password", document.getElementById("password").value);
    data.append("country", document.getElementById("country").value);
    data.append("city", document.getElementById("city").value);
    data.append("csrfmiddlewaretoken", csrfToken);

    fetch(url,{
        method:'POST',
        body:data
    }).then(function(response){
            return response.json(); 
    }).then(function(data){
            alert(data.message);
    });
}

function login_user(){
  url = "user_login";
  
  var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value
  const data = new FormData();
  data.append("username", document.getElementById("email").value);
  data.append("password", document.getElementById("password").value);
  data.append("csrfmiddlewaretoken", csrfToken);

  fetch(url,{
      method:'POST',
      body:data
  }).then(function(response){
          return response.json(); 
  }).then(function(data){
          alert(data.message);
  });
  console.log("inside script");
}