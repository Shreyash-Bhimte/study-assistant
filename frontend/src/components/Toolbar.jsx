import styles from "./Toolbar.module.css";

export default function Toolbar({ onSummarise, isLoading, hasDocument }) {
  return (
    <div className={styles.toolbar}>
      <button
        className={styles.btn}
        onClick={onSummarise}
        disabled={isLoading || !hasDocument}
      >
        Summarise
      </button>
    </div>
  );
}