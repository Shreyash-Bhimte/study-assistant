import { useStudySession } from "./hooks/useStudySession";
import FileUpload from "./components/FileUpload";
import ChatWindow from "./components/ChatWindow";
import Toolbar from "./components/Toolbar";
import FlashCards from "./components/FlashCards";
import styles from "./App.module.css";

export default function App() {
  const { state, bottomRef, handleUpload, handleAsk, handleSummarise, handleFlashcards, clearSession } = useStudySession();

  return (
    <div className={styles.layout}>
      <aside className={styles.sidebar}>
        <h1 className={styles.logo}>StudyAI</h1>
        <FileUpload
          onUpload={handleUpload}
          isLoading={state.isLoading}
          fileName={state.fileName}
        />
        {state.charCount > 0 && (
          <div>
            <p className={styles.charCount}>{state.charCount.toLocaleString()} characters</p>
            <p className={styles.charCount}>~{Math.round(state.charCount / 4).toLocaleString()} tokens</p>
          </div>
        )}
        {state.error && <p className={styles.error}>{state.error}</p>}
        {state.documentText && (
          <button className={styles.clearBtn} onClick={clearSession}>Clear session</button>
        )}
      </aside>
      <main className={styles.main}>
        {!state.documentText ? (
          <p className={styles.empty}>Upload a document to get started.</p>
        ) : (
          <div className={styles.panel}>
            <Toolbar
              onSummarise={handleSummarise}
              onFlashcards={handleFlashcards}
              isLoading={state.isLoading}
              hasDocument={!!state.documentText}
            />
            {state.summary && (
              <div className={styles.summary}>
                <h2 className={styles.summaryTitle}>Summary</h2>
                <p className={styles.summaryText}>{state.summary}</p>
              </div>
            )}
            <FlashCards cards={state.flashcards} />
            <ChatWindow
              messages={state.messages}
              isLoading={state.isLoading}
              onAsk={handleAsk}
              bottomRef={bottomRef}
            />
          </div>
        )}
      </main>
    </div>
  );
}