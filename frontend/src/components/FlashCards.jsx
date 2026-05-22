import { useState } from "react";
import styles from "./FlashCards.module.css";

function Card({ question, answer }) {
  const [flipped, setFlipped] = useState(false);
  return (
    <div className={styles.cardScene} onClick={() => setFlipped(!flipped)}>
      <div className={`${styles.card} ${flipped ? styles.flipped : ""}`}>
        <div className={styles.front}>
          <p>{question}</p>
        </div>
        <div className={styles.back}>
          <p>{answer}</p>
        </div>
      </div>
    </div>
  );
}

export default function FlashCards({ cards }) {
  if (!cards.length) return null;
  return (
    <div className={styles.container}>
      <h2 className={styles.title}>Flashcards</h2>
      <div className={styles.grid}>
        {cards.map((card, i) => (
          <Card key={i} question={card.question} answer={card.answer} />
        ))}
      </div>
    </div>
  );
}