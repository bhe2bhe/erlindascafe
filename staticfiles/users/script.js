const hamburger = document.querySelector(".hamburger");
const navBar = document.querySelector(".navbar");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navBar.classList.toggle("active");
})

document.querySelectorAll(".navbar a").forEach(n => n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navBar.classList.remove("active");
}))

// JavaScript to move the .intro div from left to right
let introDiv = document.querySelector('.intro');
let position = -introDiv.offsetWidth; // Start off-screen to the left
let direction = 1;
let maxPosition = 0; // Calculate the maximum position
let animationSpeed = 4; // Adjust the animation speed as needed

// JavaScript to move the .intro div from left to right after intro animation
setTimeout(function() {
    let introDiv = document.querySelector('.intro');
    let position = -introDiv.offsetWidth; // Start off-screen to the left
    let direction = 1;
    let maxPosition = 0; // Calculate the maximum position
    let animationSpeed = 4; // Adjust the animation speed as needed

    function moveIntro() {
        position += direction * animationSpeed;
        if (position >= maxPosition) {
            position = maxPosition; // Stop at the maximum position
            clearInterval(intervalID); // Stop the interval
        }
        introDiv.style.position = 'relative'; 
        introDiv.style.left = `${position}px`; // Move the div horizontally
        introDiv.style.opacity = 1; // Fade the div into view
    }
    
    let intervalID = setInterval(moveIntro, 2);
}, 400); // Adjust the delay as needed (2 seconds in this example)

document.addEventListener("DOMContentLoaded", function() {
    // Function to handle the intersection of the .our-story section
    function handleIntersection(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) { // If the .our-story section is intersecting with the viewport
                entry.target.style.opacity = '1'; // Change opacity to 1
                observer.unobserve(entry.target); // Stop observing once the opacity is changed
            }
        });
    }

    // Create an Intersection Observer instance
    let observer = new IntersectionObserver(handleIntersection, {
        root: null, // Use the viewport as the root
        rootMargin: '0px', // No margin
        threshold: 0.5 // Trigger when at least 50% of the element is visible
    });

    // Observe the .our-story section
    let ourStorySection = document.querySelector('.our-story');
    observer.observe(ourStorySection);
});


