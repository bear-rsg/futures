// This script sets and gets author details (e.g. name, email, social media profile)
// stored in cookies (if exists), so users don't have to repeat each time they post


//
// SET cookie data
//

// Set cookies data when submitting 'vision create' and 'response create' forms
$('#vision-create-submit, #response-create-submit').on('click', function(e){
    // Prevent form submission
    e.preventDefault();
    // Setting used for all cookies
    var cookieSettings = 'expires=Mon, 31 Dec 2050 23:59:59 GMT; path=/; Secure;'
    // Create cookies for author data
    document.cookie = `authorName=${$('#id_author_name').val()}; ${cookieSettings}`;
    document.cookie = `authorEmail=${$('#id_author_email').val()}; ${cookieSettings}`;
    document.cookie = `authorSocial=${$('#id_author_social').val()}; ${cookieSettings}`;
    // Submit the form
    $(this).closest('form').submit();
});


//
// GET cookie data
//

// Generic function for getting cookie data
function getCookie(name) {
    // Convert cookies string to list
    var c_list = document.cookie.split("; "),
        i = 0,
        c,
        c_name,
        c_value;
    // Loop through cookies list to find a match
    for (i = 0; i < c_list.length; i++) {
        // Find cookie
        c = c_list[i].split('=');
        c_name = c[0];
        c_value = c[1];
        // Return cookie value if cookie name matches
        if (c_name === name) {
            return c_value;
        }
    }
    // If no cookie found with given name, return null
    return null;
}

// Get author data from cookies and apply to form fields
// (this works in both 'vision create' and 'response create' forms)
$('#id_author_name').val(getCookie('authorName'));
$('#id_author_email').val(getCookie('authorEmail'));
$('#id_author_social').val(getCookie('authorSocial'));
