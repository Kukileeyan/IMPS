console.log('JavaScript is connected!');

window.addEventListener("blur", () => {
    document.title = "Idle";
  });

  window.addEventListener("focus", () => {
    document.title = "Welcome To IETI Marikina!"
  });

  // Function to handle tab switching
  function openFloor(evt, floorName) {
    var i, tabcontent, tablinks;
    
    // Hide all images
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }

    // Remove active class from all buttons
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the selected floor image and add active class to the button
    document.getElementById(floorName).style.display = "block";
    evt.currentTarget.className += " active";

    // Update the iframe with the selected floor image
    var iframe = document.getElementById("floorImage");
    iframe.src = "{% static 'Images/" + floorName + ".png' %}";
  }