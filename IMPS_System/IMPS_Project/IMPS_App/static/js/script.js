console.log('JavaScript is connected!');

window.addEventListener("blur", () => {
    document.title = "Idle";
  });

  window.addEventListener("focus", () => {
    document.title = "Welcome To IETI Marikina!"
  });