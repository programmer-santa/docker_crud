// This file contains the JavaScript code for the frontend application.

// Function to fetch appointments from the backend
async function fetchAppointments() {
    const response = await fetch('/api/appointments');
    const appointments = await response.json();
    displayAppointments(appointments);
}

// Function to display appointments in the frontend
function displayAppointments(appointments) {
    const appointmentsList = document.getElementById('appointments-list');
    appointmentsList.innerHTML = '';

    appointments.forEach(appointment => {
        const listItem = document.createElement('li');
        listItem.textContent = `${appointment.client_name} - ${appointment.date} at ${appointment.time}`;
        appointmentsList.appendChild(listItem);
    });
}

// Event listener for creating a new appointment
document.getElementById('create-appointment-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await fetch('/api/appointments', {
        method: 'POST',
        body: formData,
    });
    if (response.ok) {
        fetchAppointments();
        event.target.reset();
    }
});

// Initial fetch of appointments when the page loads
document.addEventListener('DOMContentLoaded', fetchAppointments);