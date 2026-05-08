// function applyJob(companyName) {
//     alert("You have successfully applied for " + companyName + "!");
// }

// function saveProfile(event) {
//     event.preventDefault();
//     alert("Profile updated successfully!");
// }

// function submitForm(event, message) {
//     // event.preventDefault();
//     alert(message);
//     return true;
// }

document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll('.stat-number');
    
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            const speed = 200; // Lower is faster
            const inc = target / speed;

            if (count < target) {
                counter.innerText = Math.ceil(count + inc);
                setTimeout(updateCount, 1);
            } else {
                counter.innerText = target + "+";
            }
        };
        updateCount();
    });
});