document.addEventListener("DOMContentLoaded" ,()=>
{
    console.log("Curriculum Vitae has been uplpoaded");
});


// // ====== Dark / Light Mode ======
// const toggleBtn = document.getElementById("theme-toggle");
// const body = document.body;

// if (localStorage.getItem("theme") === "dark") {
//   body.classList.add("dark-mode");
//   toggleBtn.textContent = "☀️";
// }

// toggleBtn.addEventListener("click", () => {
//   body.classList.toggle("dark-mode");
//   const isDark = body.classList.contains("dark-mode");
//   toggleBtn.textContent = isDark ? "☀️" : "🌙";
//   localStorage.setItem("theme", isDark ? "dark" : "light");
// });

// ====== Animate Skill Bars on Scroll ======
const skillBars = document.querySelectorAll(".skill-progress");

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.width = entry.target.getAttribute("style").match(/width:\s*(\d+%)/)[1];
      }
    });
  },
  { threshold: 0.3 }
);

skillBars.forEach((bar) => {
  const originalWidth = bar.style.width;
  bar.style.width = "0";
  observer.observe(bar);
});


// Dark/light mode toggle
const toggleBtn = document.getElementById("theme-toggle");
const main = document.querySelector(".main-content");

if (localStorage.getItem("mode") === "dark") {
  document.body.classList.add("dark");
  main.style.background = "#121212";
  main.style.color = "#f0f0f0";
  toggleBtn.textContent = "☀️";
}

toggleBtn.addEventListener("click", () => {
  const isDark = document.body.classList.toggle("dark");
  main.style.background = isDark ? "#121212" : "#fafafa";
  main.style.color = isDark ? "#f0f0f0" : 

"#333";
  toggleBtn.textContent = isDark ? "☀️" : "🌙";
  localStorage.setItem("mode", isDark ? "dark" : "light");
});

// Animate language bars
const bars = document.querySelectorAll(".lang-progress");
bars.forEach(bar => {
  const width = bar.style.width;
  bar.style.width = "0";
  setTimeout(() => (bar.style.width = width), 500);
});
