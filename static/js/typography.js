function typeWriter() {
    // Declaring Variables for Type Effect
    const words = ["Sanjib Subedi", "Saroj Tharu", "Sher Bahadur Baral"];
    let count = 0; //Array counter
    let letterCount = 0; //Letter in a word counter
    let word = ""; //Iterated word of Array
    let text = ""; //Every letter in the word
    let timeOut = 70;
    let deleting = false; //Is declared for removing the text
    // Typing Effect function
    function loop() {
      if (count === words.length) {
        count = 0; //Keep looping after words are finished
      }
      word = words[count];
      if (deleting) {
        text = word.slice(0, --letterCount); //Deleting letters
      } else {
        text = word.slice(0, ++letterCount); //Adding letters
      }
      document.querySelector("#typing").textContent = text;
      timeOut = deleting ? 40 : 70;
      if (!deleting && text.length === word.length) {
        document.querySelector("#typing").textContent = text + "\xa0";
        timeOut = 2000;
        deleting = true;
      } else if (deleting && text.length === 0) {
        timeOut = 100;
        deleting = false;
        count++;
      }
      setTimeout(loop, timeOut);
    }
    loop();
  }
  typeWriter();