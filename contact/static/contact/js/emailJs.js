//Contact form linked to EmailJS
src="https://cdn.jsdelivr.net/npm/emailjs-com@2/dist/email.min.js"
	(function(){
        emailjs.init("user_dYXdGeorqYYUJK0lclK57");
    })();

//contact form linked to private email using EmailJs
//variables that are used to clear the form after submission see below function(response)
let firstNameInput = document.getElementById("fname");
let secondNameInput = document.getElementById("lname");
let emailInput = document.getElementById("email");
let subjectInput = document.getElementById("subject");
let messageInput = document.getElementById("message");
//allows for the passing of parameters from contact form to the EmailJS service
function sendMail(contactForm) {
    emailjs.send("gmail", "template_sns9k32", this, {
        "fname": contactForm.firstname.value,
        "lname": contactForm.lastname.value,
        "email": contactForm.email.value,
        "subject": contactForm.subject.value,
        "message": contactForm.message.value,
    })
        //responses after the submission of form: SUCCESS / ERROR
        .then(
            function (response) {
                //values that clear the contact form after successful submission of form
                firstNameInput.value = '';
                secondNameInput.value = '';
                emailInput.value = '';
                subjectInput.value = '';
                messageInput.value = '';
                console.log("SUCCESS", response);
            },
            function (error) {
                console.log("ERROR", error);
            }
        );
    return false;
}