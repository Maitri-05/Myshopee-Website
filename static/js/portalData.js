// registration function
function register_client() {
  url = "client_registration";
  var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

  const data = new FormData();
  data.append("name", document.getElementById("name").value);
  data.append("mobile_number", document.getElementById("mobile_number").value);
  data.append("email", document.getElementById("email").value);
  data.append("password", document.getElementById("password").value);
  data.append("country", document.getElementById("country").value);
  data.append("city", document.getElementById("city").value);
  data.append("csrfmiddlewaretoken", csrfToken);

  fetch(url, {
    method: "POST",
    body: data,
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      alert(data.message);
    });
}

// login function
function login_client() {
  url = "client_login";

  var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  const data = new FormData();
  data.append("username", document.getElementById("email").value);
  data.append("password", document.getElementById("password").value);
  data.append("csrfmiddlewaretoken", csrfToken);

  fetch(url, {
    method: "POST",
    body: data,
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      if (data.location) {
        location.href = data.location;
      } else if (data.message) {
        alert(data.message);
      }
    });
  console.log("inside script");
}

// log out function
function log_out(){ 
  console.log("on log button click");
  url =  "client_logout";
  var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  const data = new FormData();
  data.append("csrfmiddlewaretoken",csrfToken);
  fetch(url, {
      method: 'POST',
      body: data,
  })
  .then(function (response) {
    return response.json();
  })
  .then(function(data){
    if (data.message) {
      alert(data.message);
    }if(data.location) {
      location.href = data.location;
    }
  });
}


// to add data
function product_form() {
  console.log("inside product_form")
  url = "add_product";
  var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  console.log(document.getElementById("product_name").value)
  console.log(document.getElementById("product_price").value)
  console.log(document.getElementById("product_description").value)
  console.log(document.getElementById("product_thumbnail").value)
  console.log(document.getElementById("min_order_quantity").value)
  const data = new FormData();
  data.append("product_name", document.getElementById("product_name").value);
  data.append("product_price", document.getElementById("product_price").value);
  data.append(
    "product_description",
    document.getElementById("product_description").value
  );
  //   data.append("product_availability", document.getElementById("product_availability").value);
  data.append(
    "product_thumbnail",
    document.getElementById("product_thumbnail").files[0]
  );
  data.append(
    "min_order_quantity",
    document.getElementById("min_order_quantity").value
  );
  data.append("csrfmiddlewaretoken", csrfToken);
  console.log(data)
  fetch(url, {
    method: "POST",
    body: data,
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      if (data.location) {
        location.href = data.location;
      } else if (data.message) {
        alert(data.message);
      }
    });
}

function update_prd_frm(){
  console.log("inside update_form")
  url = "update_product";
  var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[1].value;
  const productName = document.getElementById('product_name').value;
  const productPrice = document.getElementById('product_price').value;
  const productDescription = document.getElementById('product_description').value;
  const minOrderQuantity = document.getElementById('min_order_quantity').value;
  const data = new FormData();
  data.append("product_name", productName);
  data.append("product_price", productPrice);
  data.append("product_description", productDescription);
  data.append("min_order_quantity", minOrderQuantity);
  data.append("csrfmiddlewaretoken", csrfToken)
  console.log(data)
  fetch(url, {
    method: "POST",
    body: data,
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      if (data.location) {
        location.href = data.location;
      } else if (data.message) {
        alert(data.message);
      }
    });
}

//  script to delete a product 
  function delete_prd(productid){
    console.log("on delete button click");
    url =  `delete_product/${productid}`;
    var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    const data = new FormData();
    data.append("csrfmiddlewaretoken",csrfToken);
    console.log(csrfToken);
    fetch(url,{
      method:"POST",
      body:data
    })
    .then(function (response) {
      return response.json();
    })
    .then(function(data){
      if(data.message){
        document.getElementById(`${productid}`).remove();
        alert(data.message);
      }else if(data.location){
        location.href = data.location;
      }else if (data.message) {
        alert(data.message);
      }
    });
  }

function category_form(){
  console.log("inside category form")
  url = "add_category";
  var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  console.log(document.getElementById("category_name").value)
  console.log(document.getElementById("category_thumbnail").value)
  const data = new FormData();
  data.append("category_name", document.getElementById("category_name").value);
  data.append(
    "category_thumbnail",
    document.getElementById("category_thumbnail").files[0]
  );
  data.append("csrfmiddlewaretoken", csrfToken);
  console.log(data)
  fetch(url, {
    method: "POST",
    body: data,
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      if (data.location) {
        location.href = data.location;
      } else if (data.message) {
        alert(data.message);
      }
    });
}

function delete_category(categorytid){
  console.log("on delete button click");
  url =  `delete_category/${categorytid}`;
  var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  const data = new FormData();
  data.append("csrfmiddlewaretoken",csrfToken);
  console.log(csrfToken);
  fetch(url,{
    method:"POST",
    body:data
  })
  .then(function (response) {
    return response.json();
  })
  .then(function(data){
    if(data.message){
      alert(data.message);
    }if(data.location){
      location.href = data.location;
    }
  });
}