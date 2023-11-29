const localServer = 'http://127.0.0.1:5000/'

function checkLogin(email, password) {
    fetch(localServer + 'check-login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Specify the content type
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    })
        .then(res => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error('Network response was not ok.');
            }
        })
        .then(data => {
            if (data.authenticated === true) {
                console.log('Successful Login'); 
            } else {
                console.log('Login Failed');
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

function register(firstName, lastName, email, password) {
    fetch(localServer + 'create-user', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json' // Specify the content type
        },
        body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            email: email,
            password: password
        })
    })
        .then(res => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error('Network response was not ok.');
            }
        })
        .then(data => {
            console.log(data.id);
            if (data.id) {
                console.log('Successful Registration');
            } else {
                console.log('Unsuccessful Registration');
            }
        })
        .catch(error => {
            console.error('There was a problem with the put operation:', error);
        });
}
