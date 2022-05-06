function validate(event){
            console.log('Form Submission')
            var error = document.getElementById('message');
            var message =  message;
            var values = event.target.elements;
            var name = values.name.value;
            var email = values.email.value;
            var password = event.password.value;
            var repassword = event.repassword.value;

            if (!name.trim()){ message= "Name is Required ."}
            else if(!email.trim()){message = "Email is Required ."}
            else if(!password.trim()){message = "Password is Required ."}
            else if(!repassword.trim()){message = "repassword is Required ."}
            else if(password.trim()!=!password.trim()){message = "password mismatch try again."}

            if(message){
            error.innerHTML = message
            error.hidden = false
            }
            else{
            error.innerHTML = ""
            error.hidden = true
            }

           console.log(name, email , phone , password , repassword)

    event.stopPropagation();
    return false


}