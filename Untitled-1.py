<!DOCTYPE html>
<html>
<head>
    <title>Cookie Chatbot</title>
</head>
<body>
    <h2>Cookie Chatbot</h2>

    <input type="text" id="userInput" placeholder="Type a message">
    <button onclick="sendMessage()">Send</button>

    <div id="chat"></div>

    <script>
        function sendMessage() {
            let input = document.getElementById("userInput").value;
            let chat = document.getElementById("chat");

            let reply = "I don't understand.";

            if (input.toLowerCase() === "hello") {
                reply = "Hello!";
            } else if (input.toLowerCase() === "how are you") {
                reply = "I'm fine!";
            }

            chat.innerHTML += `<p><b>You:</b> ${input}</p>`;
            chat.innerHTML += `<p><b>Bot:</b> ${reply}</p>`;

            document.getElementById("userInput").value = "";
        }
    </script>
</body>
</html>