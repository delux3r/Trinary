const input = document.getElementById("query");

// Persist input across reloads
const STORAGE_KEY = 'trinary_query';

window.addEventListener('load', () => {
  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved) input.value = saved;
});

input.addEventListener('input', () => {
  localStorage.setItem(STORAGE_KEY, input.value);
});

input.addEventListener("keydown", e => {
  if (e.key === "Enter") {
    search();
  }
});

function search() {
  const q = input.value.trim();
  if (!q) return;
  localStorage.setItem(STORAGE_KEY, q);
  window.location.href =
    `http://127.0.0.1:5000/search?q=${encodeURIComponent(q)}`;
}

function go(url) {
  window.location.href = url;
}

// Google provider: search with the current query or open Google homepage
const googleBtn = document.getElementById('googleBtn');
if (googleBtn) {
  googleBtn.addEventListener('click', () => {
    const q = input.value.trim();
    localStorage.setItem(STORAGE_KEY, q);
    if (!q) {
      window.location.href = '#';
      return;
    }
    window.location.href = `https://www.google.com/search?q=${encodeURIComponent(q)}`;
  });
}