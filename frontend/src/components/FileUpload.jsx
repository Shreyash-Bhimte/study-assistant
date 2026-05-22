import styles from "./FileUpload.module.css";
export default function FileUpload({ onUpload, isLoading, fileName }) {
  function handleChange(e) {
    const file = e.target.files[0];
    if (file) onUpload(file);
  }

  return (
    <div className={styles.container}>
      <label className={styles.label}>
        {isLoading ? "Uploading…" : fileName ? `✓ ${fileName}` : "Upload PDF or .txt"}
        <input
          type="file"
          accept=".pdf,.txt"
          onChange={handleChange}
          disabled={isLoading}
          className={styles.input}
        />
      </label>
    </div>
  );
}