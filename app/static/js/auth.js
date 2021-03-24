LOGIN_URL = "http://localhost:5000/auth/login"
SIGNUP_URL = "http://localhost:5000/auth/signup"


function login(username, password) {
	var requestOptions = {
  		method: 'GET'
	};

	return fetch(LOGIN_URL + "?username="+username+"&password="+password, requestOptions)
  		.then(response => response.json())
  		.then(result => {
  			console.log(result)
  			if (result.success == true) {
  				localStorage.setItem("token", result.token)
  			}
  			return result
  		})
  		.catch(error => console.log('error', error));
}

function signup(username, password, dob, phone_number) {
	
	var myHeaders = new Headers();
	myHeaders.append("Content-Type", "application/json");

	var raw = JSON.stringify({
  		"username": username,
  		"password": password,
  		"dob": dob,
  		"phone_number": phone_number
	});

	var requestOptions = {
  		method: 'POST',
  		headers: myHeaders,
  		body: raw,
	};

	return fetch(SIGNUP_URL, requestOptions)
  		.then(response => response.json())
  		.then(result => {
  			console.log(result)
  			if (result.success == true) {
  				localStorage.setItem("token", result.token)
  			}
  			return result
  		})
  		.catch(error => console.log('error', error));
}

function isLoggedIn() {
	if (localStorage.getItem("token")) {
		return true
	} 
	else {
		return false
	}
}

function getToken() {
	let token
	token = localStorage.getItem("token")
	return token
}