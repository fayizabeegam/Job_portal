document.getElementById('deleteJobBtn').addEventListener('click', function() {
    var jobId = this.getAttribute('data-job-id');
    // Show a confirmation dialog
    var confirmDelete = confirm('Are you sure you want to delete this job?');

    if (confirmDelete) {
        deleteJob(jobId);
    }
});

function deleteJob(jobId) {
    // Construct the URL using JavaScript
    var deleteUrl = '/recruiter/jobs/' + jobId + '/delete/';

    // Send an AJAX request to the delete_job_view
    $.ajax({
        type: 'POST',
        url: deleteUrl,
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
        },
        success: function (response) {
            console.log(response);
            if (response.success) {
                // Optionally, you can show a success message
                alert('Job deleted successfully');

                // Redirect to the recruiter dashboard
                window.location.replace(response.redirect_url);
            } else {
                // Handle other responses or errors
                console.error('Error deleting job:', response.error);
            }
        },
        error: function (error) {
            // Handle the error response
            console.error(error);
        }
    });
}
 /**************************************************************************/
 $(document).ready(function() {
    $('#toggleStatusBtn').click(function(e) {
        e.preventDefault();
        var user_id = $(this).data('user-id');

        $.ajax({
            type: 'POST',
            url: '{% url "update-jobseeker-status" user_id=jobseeker.user_id %}',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                is_active: true  // Set this to false if you want to deactivate
            },
            success: function(response) {
                console.log(response.message);

                // Optionally, update the button text or perform other UI changes
                $('#toggleStatusBtn').text(response.is_active ? 'Deactivate' : 'Activate');
            },
            error: function(response) {
                console.error(response.error);

                // Optionally, display an error message to the user
            }
        });
    });
});

/*********************************************************************** */









//  $(document).ready(function () {
//     $('#updateStatusForm').on('submit', function (e) {
//         e.preventDefault();

//         $.ajax({
//             type: 'POST',
//             url: $(this).data('status-url'),
//             data: $(this).serialize(),
//             success: function (data) {
//                 alert('Status updated successfully!');
//             },
//             error: function (error) {
//                 alert('Error updating status.');
//             }
//         });
//     });
// });