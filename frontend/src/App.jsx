import { useStudySession } from "./hooks/useStudySession";
import FileUpload from "./components/FileUpload";
import styles from "./App.module.css";

export default function App() {
  const { state, handleUpload, clearSession } = useStudySession();

  return (
    <div className={styles.layout}>
      <aside className={styles.sidebar}>
        <h1 className={styles.logo}>StudyAI</h1>
        <FileUpload onUpload={handleUpload} isLoading={state.isLoading} />
        {state.charCount > 0 && (
          <p className={styles.charCount}>{state.charCount.toLocaleString()} characters loaded</p>
        )}
        {state.error && <p className={styles.error}>{state.error}</p>}
        {state.documentText && (
          <button className={styles.clearBtn} onClick={clearSession}>
            Clear session
          </button>
        )}
      </aside>
      <main className={styles.main}>
        {!state.documentText ? (
          <p className={styles.empty}>Upload a document to get started.</p>
        ) : (
          <p className={styles.ready}>Document ready. Chat coming in Commit 6.</p>
        )}
      </main>
    </div>
  );
}