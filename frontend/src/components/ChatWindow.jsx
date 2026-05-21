import { useState } from "react";
import MessageBubble from "./MessageBubble";
import styles from "./ChatWindow.module.css";

export default function ChatWindow({ messages, isLoading, onAsk, bottomRef }) {
  const [input, setInput] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    if (!input.trim() || isLoading) return;
    onAsk(input.trim());
    setInput("");
  }

  return (
    <div className={styles.container}>
      <div className={styles.messages}>
        {messages.length === 0 && (
          <p className={styles.hint}>Ask a question about your document.</p>
        )}
        {messages.map((msg, i) => (
          <MessageBubble key={i} message={msg} />
        ))}
        {isLoading && <p className={styles.thinking}>Thinking…</p>}
        <div ref={bottomRef} />
      </div>
      <form className={styles.form} onSubmit={handleSubmit}>
        <input
          className={styles.input}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question…"
          disabled={isLoading}
        />
        <button className={styles.btn} type="submit" disabled={isLoading || !input.trim()}>
          Send
        </button>
      </form>
    </div>
  );
}