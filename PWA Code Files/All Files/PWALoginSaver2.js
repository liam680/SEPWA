const form = document.getElementById('loginForm');
const messageBox = document.getElementById('messageBox');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const Username = document.getElementById('Username').value;
  const Password = document.getElementById('Password').value;


  const res = await fetch('/login',{
    method: 'POST',
    headers:{ 'Content-Type':'application/json' },
    body: JSON.stringify({ user_id: (1), Username, Password })
  });

  const data = await res.json();


  if (data.success) {
    messageBox.innerHTML = `<p> Login Successful. Welcome ${data.user_id}!</p>`;
   } else {
messageBox.innerHTML = `<p>Login Failed</p>`
}

  form.reset();
});

localStorage.setItem("Forecast Data", JSON.stringify(data));
let stored = JSON.parse(localStorage.getItem("Forecast Data"));








