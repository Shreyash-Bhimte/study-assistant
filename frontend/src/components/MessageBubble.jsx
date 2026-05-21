import styles from "./MessageBubble.module.css";

export default function MessageBubble({ message }) {
  const isUser = message.role === "user";
  return (
    <div className={`${styles.bubble} ${isUser ? styles.user : styles.assistant}`}>
      {message.content}
    </div>
  );
}