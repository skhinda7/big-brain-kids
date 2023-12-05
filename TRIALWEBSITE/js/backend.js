const localServer = 'http://127.0.0.1:5000/'
const token = localStorage.getItem('authToken')

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
                localStorage.setItem('authToken', data.token);
                console.log(data);
                window.location.replace('http://127.0.0.1:5500/TRIALWEBSITE/html/learning.html');
                console.log(data.token);
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
                checkLogin(email, password);
            } else {
                console.log('Unsuccessful Registration');
            }
        })
        .catch(error => {
            console.error('There was a problem with the PUT operation:', error);
        });
}

function checkSession() {

    return fetch(`${localServer}check-session?token=${token}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(res => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error('Network response was not ok.');
            }
        })
        .catch(error => {
            console.error('There was a problem with the GET operation:', error);
            return { authenticated: false }; // Return false in case of error
        });
}

function getScore() {

    return fetch(`${localServer}get-scores?token=${token}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(res => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error('Error')
            }
        })
        .catch(error => {
            console.error('There was a problem with the GET operation:', error);
            return { authenticated: false }; // Return false in case of error
        });
}

async function getQuestion(operation, isDynamic) {

    return fetch(`${localServer}get-question?operation=${operation}&dynamic=${isDynamic}&id=${token}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(res => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error('Error')
            }
        })
        .then(data => {
            return data;
        })
        .catch(error => {
            console.error('There was a problem with the GET op:', error);
        })
}

async function handleScore(operation, answerList) {
    return fetch(`${localServer}process-score`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            id: token,
            operation: operation,
            answerList: answerList,
        })
    })
        .then(res => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error('Error')
            }
        })
        .catch(error => {
            console.error('Error processing score:', error);
        });
}

function processScore(operation, answer) {
    const userAnswer = document.getElementById('user-answer').value.trim();

    if (userAnswer !== '') {
        if (userAnswer === answer) {
            displayBanner('correctBanner');
            setTimeout(() => {
                handleScore(operation, [0]);
            }, 3000);
        } else {
            displayBanner('wrongBanner');
            setTimeout(() => {
                handleScore(operation, [1]);
            }, 3000);
        }
    } else {
        displayBanner('noAnswerBanner');
    }

    checkMastery(operation);
}

function checkMastery(operation) {
    getScore()
        .then(res => {
            if (res[operation] >= 0.98) {
                displayCompletionMessage();
            }
        })
}
function displayCompletionMessage() {
    // Show a completion message or banner indicating proficiency reached
    alert('Congratulations! You have reached the proficiency level. You will now be redirected to the learning hub.');
    window.location.replace('http://127.0.0.1:5500/TRIALWEBSITE/html/learning.html');
}
function displayBanner(bannerId) {
    const banners = document.querySelectorAll('.banner');
    banners.forEach(banner => {
        banner.classList.add('hidden');
    });

    const bannerToShow = document.getElementById(bannerId);
    bannerToShow.classList.remove('hidden');
}

function logOut() {
    localStorage.removeItem('authToken');

    alert('You have successfully logged out');

    return window.location.replace('http://127.0.0.1:5500/TRIALWEBSITE/html/homepage.html');
}

