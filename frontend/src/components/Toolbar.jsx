import styles from "./Toolbar.module.css";


export default function Toolbar({ onSummarise, onFlashcards, isLoading, hasDocument }) {
  return (
    <div className={styles.toolbar}>
      <button className={styles.btn} onClick={onSummarise} disabled={isLoading || !hasDocument}>
        {isLoading ? "Working…" : "Summarise"}
      </button>
      <button className={styles.btn} onClick={onFlashcards} disabled={isLoading || !hasDocument}>
        {isLoading ? "Working…" : "Flashcards"}
      </button>
    </div>
  );
}