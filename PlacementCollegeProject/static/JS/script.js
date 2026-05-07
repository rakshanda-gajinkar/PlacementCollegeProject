function applyJob(companyName) {
    alert("You have successfully applied for " + companyName + "!");
}

function saveProfile(event) {
    event.preventDefault();
    alert("Profile updated successfully!");
}

function submitForm(event, message) {
    event.preventDefault();
    alert(message);
}