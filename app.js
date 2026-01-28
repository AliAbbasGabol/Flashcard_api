const API_URL = 'https://aliabbasgabol.pythonanywhere.com/Flashcards';
const cardList = document.getElementById("cardList");

fetch(API_URL)
  .then(res => res.json())
  .then(data => {
    data.forEach(cardData => {
      const card = createCard(cardData);
      cardList.appendChild(card);
    });
  })
  .catch(err => console.error(err));

function createCard(data) {
  const scene = document.createElement("div");
  scene.className = "scene";

  const card = document.createElement("div");
  card.className = "card";

  const front = document.createElement("div");
  front.className = "card-face front";
  front.textContent = data.answer;

  const back = document.createElement("div");
  back.className = "card-face back";
  back.textContent = data.question;

  card.append(front, back);
  scene.appendChild(card);

  card.addEventListener("click", () => {
    card.classList.toggle("is-flipped");
  });

  return scene;
}
