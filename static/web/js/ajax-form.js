$(function () {

    // Get the form.
    var form = $('#contact-form');

    // Get the messages div.
    var formMessages = $('.ajax-response');

    // Set up an event listener for the contact form.
    $(form).submit(function (e) {
        // Stop the browser from submitting the form.
        e.preventDefault();

        // Serialize the form data.
        var formData = $(form).serialize();

        // Submit the form using AJAX.
        $.ajax({
            type: 'POST',
            url: $(form).attr('action'),
            data: formData
        })
            .done(function (response) {
                // Make sure that the formMessages div has the 'success' class.
                $(formMessages).removeClass('error');
                $(formMessages).addClass('success');

                // Set the message text.
                $(formMessages).text(response);

                // Clear the form.
                $('#contact-form input,#contact-form textarea').val('');
            })
            .fail(function (data) {
                // Make sure that the formMessages div has the 'error' class.
                $(formMessages).removeClass('success');
                $(formMessages).addClass('error');

                // Set the message text.
                if (data.responseText !== '') {
                    $(formMessages).text(data.responseText);
                } else {
                    $(formMessages).text('Oops! An error occured and your message could not be sent.');
                }
            });
    });

});

var isLoading = false;
$(document).on("submit", "form.ajax", function (e) {
    e.preventDefault();
    var $this = $(this),
        data = new FormData(this),
        action_url = $this.attr("action");

    if (!isLoading) {
        isLoading = true;
        $.ajax({
            url: action_url,
            type: "POST",
            data: data,
            cache: false,
            contentType: false,
            processData: false,
            dataType: "json",
            success: function (data) {
                var status = data.status;
                var title = data.title;
                var message = data.message;
                var redirect = data.redirect;
                var redirect_url = data.redirect_url;
                if (status == true) {
                    title ? (title = title) : (title = "Success");
                    Swal.fire({
                        title: title,
                        html: message,
                        icon: "success",
                    }).then(function () {
                        redirect && (window.location.href = redirect_url);
                    });
                } else {
                    title ? (title = title) : (title = "An Error Occurred");
                    Swal.fire({
                        title: title,
                        html: message,
                        icon: "error",
                    });
                }
            },
            error: function (data) {
                var title = "An error occurred",
                    message = "something went wrong";
                Swal.fire({
                    title: title,
                    html: message,
                    icon: "error",
                });
            },
        }).then(function (response) {
            isLoading = false;
        });
    }
});