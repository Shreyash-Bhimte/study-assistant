import { useReducer, useRef, useEffect } from "react";
import { uploadFile, askQuestion } from "../lib/api";

const initialState = {
  documentText: null,
  charCount: 0,
  messages: [],
  isLoading: false,
  error: null,
};

function reducer(state, action) {
  switch (action.type) {
    case "UPLOAD_START":
      return { ...state, isLoading: true, error: null };
    case "UPLOAD_SUCCESS":
      return { ...state, isLoading: false, documentText: action.text, charCount: action.charCount };
    case "UPLOAD_ERROR":
      return { ...state, isLoading: false, error: action.error };
    case "ASK_START":
      return {
        ...state,
        isLoading: true,
        error: null,
        messages: [...state.messages, { role: "user", content: action.question }],
      };
    case "ASK_SUCCESS":
      return {
        ...state,
        isLoading: false,
        messages: [...state.messages, { role: "assistant", content: action.answer }],
      };
    case "ASK_ERROR":
      return { ...state, isLoading: false, error: action.error };
    case "CLEAR":
      return initialState;
    default:
      return state;
  }
}

export function useStudySession() {
  const [state, dispatch] = useReducer(reducer, initialState);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [state.messages]);

  async function handleUpload(file) {
    dispatch({ type: "UPLOAD_START" });
    try {
      const data = await uploadFile(file);
      dispatch({ type: "UPLOAD_SUCCESS", text: data.text, charCount: data.char_count });
    } catch (err) {
      dispatch({ type: "UPLOAD_ERROR", error: err.message });
    }
  }

  async function handleAsk(question) {
    dispatch({ type: "ASK_START", question });
    try {
      const data = await askQuestion(state.documentText, question);
      dispatch({ type: "ASK_SUCCESS", answer: data.answer });
    } catch (err) {
      dispatch({ type: "ASK_ERROR", error: err.message });
    }
  }

  function clearSession() {
    dispatch({ type: "CLEAR" });
  }

  return { state, bottomRef, handleUpload, handleAsk, clearSession };
}