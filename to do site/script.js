const auth = document.getElementById("auth");
const app = document.getElementById("app");
const list = document.getElementById("list");
const titleInput = document.getElementById("titleInput");
const contentInput = document.getElementById("contentInput");
const tagInput = document.getElementById("tagInput");

let notes = JSON.parse(localStorage.getItem("notes")) || [];

function login() {
  const user = document.getElementById("user").value;
  const pass = document.getElementById("pass").value;

  if (!user || !pass) return;
  localStorage.setItem("auth", JSON.stringify({ user }));
я
  showApp();
}

function logout() {
  localStorage.removeItem("auth");
  showAuth();
}


function showApp() {
  auth.style.display = "none";
  app.style.display = "block";
  renderNotes();
}

function showAuth() {
  auth.style.display = "block";
  app.style.display = "none";
}


function addNote() {
  const title = titleInput.value.trim();
  const content = contentInput.value.trim();
  const tag = tagInput.value.trim();

  if (!title && !content) return;

  notes.push({ title, content, tag });

  saveNotes();
  renderNotes();

  titleInput.value = "";
  contentInput.value = "";
  tagInput.value = "";
}

function deleteNote(index) {
  notes.splice(index, 1);
  saveNotes();
  renderNotes();
}

function saveNotes() {
  localStorage.setItem("notes", JSON.stringify(notes));
}

function renderNotes() {
  list.innerHTML = "";

  notes.forEach((n, i) => {
    const li = document.createElement("li");

    li.innerHTML = `
      <b>${n.title}</b>
      <p>${n.content}</p>
      <small>#${n.tag}</small>
      <br>
      <button onclick="deleteNote(${i})">delete</button>
    `;

    list.appendChild(li);
  });
}

if (localStorage.getItem("auth")) {
  showApp();
} else {
  showAuth();
}